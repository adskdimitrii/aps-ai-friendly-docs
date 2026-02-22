#!/usr/bin/env bash
set -euo pipefail

# generate_readme_summary.sh
# Uses Claude Code CLI to generate content summaries for domain README files.
#
# Usage:
#   ./generate_readme_summary.sh acc          # single domain
#   ./generate_readme_summary.sh oauth        # another domain
#   ./generate_readme_summary.sh --all        # all domain folders

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

MARKER_START="<!-- GENERATED:CONTENT_SUMMARY:START -->"
MARKER_END="<!-- GENERATED:CONTENT_SUMMARY:END -->"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

die() { echo "ERROR: $*" >&2; exit 1; }

check_prerequisites() {
  command -v claude >/dev/null 2>&1 || die "'claude' CLI not found in PATH. Install it first."
}

# Return list of domain folders (directories that contain at least one subdir with .md files)
list_domain_folders() {
  for dir in "$SCRIPT_DIR"/*/; do
    [ -d "$dir" ] || continue
    local name
    name="$(basename "$dir")"
    # skip hidden dirs
    [[ "$name" == .* ]] && continue
    # check if any subdirectory has .md files
    if has_docs "$dir"; then
      echo "$name"
    fi
  done
}

# Check if a domain folder has doc subdirectories with .md files
has_docs() {
  local domain_path="$1"
  for sub in "$domain_path"/*/; do
    [ -d "$sub" ] || continue
    # look for at least one .md file that is not _url_index.md
    if compgen -G "$sub"/*.md >/dev/null 2>&1; then
      local count
      count=$(find "$sub" -maxdepth 1 -name '*.md' ! -name '_url_index.md' | wc -l)
      if [ "$count" -gt 0 ]; then
        return 0
      fi
    fi
  done
  return 1
}

# ---------------------------------------------------------------------------
# Build the file listing for a domain folder (token-efficient format)
# ---------------------------------------------------------------------------

build_file_listing() {
  local domain_path="$1"
  local domain_name
  domain_name="$(basename "$domain_path")"

  echo "Domain: $domain_name"
  echo ""

  for sub in "$domain_path"/*/; do
    [ -d "$sub" ] || continue
    local sub_name
    sub_name="$(basename "$sub")"

    # Collect .md basenames (excluding _url_index.md)
    local files=()
    while IFS= read -r f; do
      files+=("$f")
    done < <(find "$sub" -maxdepth 1 -name '*.md' ! -name '_url_index.md' -exec basename {} .md \; | sort)

    local count=${#files[@]}
    [ "$count" -eq 0 ] && continue

    echo "=== $sub_name ($count files) ==="
    for f in "${files[@]}"; do
      echo "  $f"
    done
    echo ""
  done
}

# ---------------------------------------------------------------------------
# Build the prompt for Claude
# ---------------------------------------------------------------------------

build_prompt() {
  local domain_name="$1"
  local file_listing="$2"

  cat <<'PROMPT_TEMPLATE'
You are analyzing a documentation repository for Autodesk Platform Services (APS).

Below is a listing of Markdown doc files within the "DOMAIN_PLACEHOLDER" domain folder, grouped by subdirectory. Your task is to produce a concise **Content Summary** section for the README.

**File naming conventions by subdirectory type:**
- `http-docs/`: Files follow the pattern `http-{service}-{resource}-{METHOD}` (e.g., `http-admin-accounts-accountidprojects-GET`). The HTTP method (GET, POST, PATCH, DELETE) is the last segment.
- `how-to-docs/`: Files are named `{service}-{task-description}` (e.g., `cost-attach-cost-file-s3`, `assets-manage-assets`). These are tutorial/how-to guides.
- `developers-guide-docs/`: Files are named `{topic}-{subtopic}` or just `{topic}` (e.g., `App-types-native`, `overview`). These are conceptual/guide docs.
- `reference-docs/`: Files are named by API class/extension (e.g., `Extensions-BimWalkExtension`, `Autodesk.Viewing.Document`). These are API reference docs.

**Instructions:**
1. Group the files into logical **topic areas** (e.g., "Cost Management", "Admin & Projects", "Issues & RFIs", "Authentication Flows").
2. For each topic area, write a brief description of what's available and give an approximate file count.
3. **Link to files using relative Markdown links.** The format is `[human-readable name](subdirectory/filename.md)`. For example: `[Get 2-Legged Token](how-to-docs/get-2-legged-token.md)`, `[GET /authorize](http-docs/http-authorize-GET.md)`. When listing many files in a topic area, link to representative/important ones and mention the count of others. Do NOT include links to external URLs — only relative paths to `.md` files in the repo.
4. Output **only raw Markdown** — no code fences, no preamble, no commentary outside the Markdown.
5. Use `## Content Summary` as the top heading, and `###` for each topic area.
6. Keep the total output **under 150 lines**.
7. Be concise but informative. An AI agent or developer should be able to read this summary and quickly know what documentation is available and where to find it within the repo.

**File listing:**

PROMPT_TEMPLATE

  # Replace placeholder and append listing
  echo "$file_listing"
}

# ---------------------------------------------------------------------------
# Insert/replace summary in README
# ---------------------------------------------------------------------------

insert_summary_into_readme() {
  local readme_path="$1"
  local summary="$2"
  local domain_name="$3"

  # Write the full block (markers + content) to a temp file for safe insertion
  local block_file
  block_file="$(mktemp)"
  {
    echo "$MARKER_START"
    echo "$summary"
    echo "$MARKER_END"
  } > "$block_file"

  if [ ! -f "$readme_path" ]; then
    # Create new README with header + summary
    {
      echo "# APS $domain_name Friendly Docs"
      echo ""
      cat "$block_file"
    } > "$readme_path"
    rm -f "$block_file"
    echo "  Created $readme_path with content summary."
    return
  fi

  # Check if markers already exist (idempotent replacement)
  if grep -qF "$MARKER_START" "$readme_path" && grep -qF "$MARKER_END" "$readme_path"; then
    # Replace between markers (inclusive): keep lines outside markers, substitute block
    local tmp
    tmp="$(mktemp)"
    local skip=0
    while IFS= read -r line; do
      if [ "$line" = "$MARKER_START" ]; then
        cat "$block_file"
        skip=1
        continue
      fi
      if [ "$line" = "$MARKER_END" ]; then
        skip=0
        continue
      fi
      if [ "$skip" -eq 0 ]; then
        echo "$line"
      fi
    done < "$readme_path" > "$tmp"
    mv "$tmp" "$readme_path"
    rm -f "$block_file"
    echo "  Updated existing summary markers in $readme_path."
    return
  fi

  # No markers — insert before "## Source" section if it exists, else append
  if grep -qE '^## Source' "$readme_path"; then
    local tmp
    tmp="$(mktemp)"
    while IFS= read -r line; do
      if [[ "$line" =~ ^"## Source" ]]; then
        cat "$block_file"
        echo ""
      fi
      echo "$line"
    done < "$readme_path" > "$tmp"
    mv "$tmp" "$readme_path"
    rm -f "$block_file"
    echo "  Inserted summary before ## Source in $readme_path."
  else
    # Append
    echo "" >> "$readme_path"
    cat "$block_file" >> "$readme_path"
    rm -f "$block_file"
    echo "  Appended summary to $readme_path."
  fi
}

# ---------------------------------------------------------------------------
# Process a single domain
# ---------------------------------------------------------------------------

process_domain() {
  local domain_name="$1"
  local domain_path="$SCRIPT_DIR/$domain_name"

  echo "Processing: $domain_name"

  # Validate
  [ -d "$domain_path" ] || die "Folder '$domain_name' does not exist."
  has_docs "$domain_path" || die "Folder '$domain_name' has no doc subdirectories with .md files."

  # Build file listing
  local file_listing
  file_listing="$(build_file_listing "$domain_path")"

  # Build prompt (replace placeholder)
  local prompt
  prompt="$(build_prompt "$domain_name" "$file_listing")"
  prompt="${prompt//DOMAIN_PLACEHOLDER/$domain_name}"

  # Call Claude CLI
  echo "  Calling Claude CLI to generate summary..."
  local summary tmp_stderr claude_exit_code stderr_output
  tmp_stderr="$(mktemp)"
  summary="$(echo "$prompt" | claude -p --output-format text 2>"$tmp_stderr")"
  claude_exit_code=$?
  stderr_output="$(cat "$tmp_stderr")"
  rm -f "$tmp_stderr"
  if [ $claude_exit_code -ne 0 ]; then
    if echo "$stderr_output" | grep -qiE '(not logged in|sign in|log in|login|authenticate|unauthorized|401|api key|account)'; then
      die "Claude authentication required. Please sign in by running 'claude' interactively and completing the login flow, then re-run this script."
    fi
    die "Claude CLI call failed for '$domain_name'.${stderr_output:+ Error: $stderr_output}"
  fi

  # Validate output
  [ -n "$summary" ] || die "Claude returned empty output for '$domain_name'."

  # Strip leading/trailing code fences if Claude wrapped output despite instructions
  summary="$(echo "$summary" | sed '/^```\(markdown\)\{0,1\}$/d')"

  # Insert into README
  local readme_path="$domain_path/README.md"
  insert_summary_into_readme "$readme_path" "$summary" "$domain_name"

  echo "  Done: $domain_name"
  echo ""
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

main() {
  [ $# -ge 1 ] || die "Usage: $0 <domain-folder> | --all"

  check_prerequisites

  if [ "$1" = "--all" ]; then
    echo "Processing all domain folders..."
    echo ""
    local domains
    domains="$(list_domain_folders)"
    [ -n "$domains" ] || die "No domain folders with docs found."
    while IFS= read -r domain; do
      process_domain "$domain"
    done <<< "$domains"
    echo "All domains processed."
  else
    process_domain "$1"
  fi
}

main "$@"
