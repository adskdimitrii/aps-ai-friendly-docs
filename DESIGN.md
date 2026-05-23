# Design Theory

This repo is an alternative to the hosted [`llms.txt`](https://aps.autodesk.com/llms.txt). The following explains why a local mirror can be meaningfully better for AI agents and the humans prompting them.

## Worked Example

> **Task:** *"Create an automation that gets all Issues from a project and then adds a comment to each open issue, reminding the person assigned to provide feedback."*

The two approaches to answering this question diverge immediately.

```text
┌──────────────────────────────────────────────┐  ┌──────────────────────────────────────────────┐
│  APPROACH A: llms.txt                        │  │  APPROACH B: Local Docs                      │
├──────────────────────────────────────────────┤  ├──────────────────────────────────────────────┤
│                                              │  │                                              │
│  1. Read glossary embedded in prompt         │  │  1. Read acc/README.md                       │
│  2. Identify API → acc_v1                    │  │     → Issues section lists direct file links │
│  3. curl CDN TOC JSON + jq to navigate tree  │  │                                              │
│  4. curl page headings + htmlq to parse      │  │  2. grep "comment" acc/http-docs/            │
│  5. curl full page text + htmlq to extract   │  │     → finds http-issues-comments-POST.md     │
│  6. curl additional pages if step 5 is thin  │  │                                              │
│  7. Compile answer from extracted fragments  │  │  3. Read 2 endpoint files                    │
│                                              │  │     → full schema + curl example, done       │
│  5–7 HTTP calls  │  live internet required   │  │                                              │
│  ~10–30 seconds  │  fails if offline         │  │  3 local ops  │  zero network calls          │
│                                              │  │  <1 second    │  works offline               │
└──────────────────────────────────────────────┘  └──────────────────────────────────────────────┘
```

With the local approach the relevant endpoints (`GET /issues`, `POST /issues/{id}/comments`) are found and read in three operations. The `llms.txt` approach requires a minimum of five HTTP round-trips to Autodesk CDN infrastructure before any code can be written.

The principles behind this difference are explained below.

---

## 1. Targeted Prompting

A prompt that links directly to a local file gives the agent its context in a single load — no search, no discovery loop.

```text
WITHOUT local docs                       WITH local docs
──────────────────────────────────────   ─────────────────────────────────────────
Prompt: "Add a comment to open issues"   Prompt: "Using acc/README.md, add a
                │                                 comment to each open issue"
                ▼                                        │
         Agent must discover:                            ▼
         - Which API covers issues?               Agent reads acc/README.md
         - Where are the endpoints?               Issues section → direct file links
         - What is the comment schema?                   │
                │                                        ▼
         Multiple search/fetch calls             Reads 2 endpoint files
                │                                        │
                ▼                                        ▼
         Eventually generates code               Generates code immediately
```

Each `README.md` in this repo is a curated index for its domain. Linking to one in a prompt is the equivalent of handing the agent a pre-filtered table of contents rather than asking it to search a library.

---

## 2. Reduced Tool Calls

With local docs, agents can use standard Unix tools — `grep`, `find`, `rg` — to perform precise, single-shot searches across all documentation. This collapses multi-step HTTP discovery chains into one shell command.

```text
  INTERNET APPROACH (llms.txt)              LOCAL APPROACH
  ──────────────────────────────────────    ─────────────────────────────────────
  fetch TOC JSON          (1 HTTP call)
  parse JSON with jq                        grep -r "comment" acc/http-docs/
  fetch page headings     (1 HTTP call)          │
  parse HTML with htmlq                          ▼
  fetch full page text    (1 HTTP call)     http-issues-comments-POST.md  ← found
  parse HTML with htmlq                     http-issues-comments-GET.md   ← found
  fetch linked subpages   (1–3 HTTP calls)
  deduplicate + compile                     read both files                (2 reads)
  ──────────────────────────────────────    ─────────────────────────────────────
  5–7 calls │ ~10–30s │ network dependent   3 ops  │  <1s  │  fully local
```

Fewer tool calls means lower latency, lower cost, and more of the agent's context budget available for actual reasoning and code generation.

---

## 3. Enterprise and Air-Gapped Environments

Many enterprise AI agent deployments run inside VPNs, corporate sandboxes, or CI/CD pipelines with restricted egress. The `llms.txt` approach depends on live HTTP access to multiple Autodesk CDN hostnames. In a restricted environment, those calls are silently blocked or return errors — the entire discovery chain fails.

```text
  ENTERPRISE ENVIRONMENT (restricted outbound traffic)

  llms.txt approach                        Local docs approach
  ──────────────────────────────────────   ──────────────────────────────────────
  Agent                                    Agent
    │                                        │
    ▼                                        ▼
  curl developer.doc.autodesk.com          grep / read local files
  curl developer.doc.config.autodesk.com     │
    │                                        ▼
    ▼                                      ✓ Endpoint schema found
  ✗ BLOCKED by firewall / proxy            ✓ Code generated
    │                                      ✓ Task complete
    ▼
  Task fails — no fallback
```

Local docs have no external dependencies at query time. The crawl that produced them is a one-time operation run by a developer with internet access; the agents that consume them need none.

---

## 4. Reproducibility

The `llms.txt` instructions and the CDN pages they point to can change at any time — a schema update, a renamed endpoint, or a restructured TOC will silently alter what the agent fetches and how it answers.

Local docs are a versioned snapshot. The docs an agent reads today are identical to the ones it read yesterday. Behaviour is deterministic and auditable. When Autodesk updates their docs, a deliberate re-crawl (see [CRAWL.md](CRAWL.md)) brings the snapshot forward — on your schedule, with a reviewable diff.

---

## 5. Token Efficiency

`llms.txt` is itself a large prompt (~several thousand tokens of instructions plus a glossary) that must be included or fetched before any question is answered. Each subsequent CDN page fetch adds more raw HTML that must be parsed and trimmed.

Loading a targeted local file — for example just [acc/http-docs/http-issues-comments-POST.md](acc/http-docs/http-issues-comments-POST.md) — puts only the relevant schema into context. Smaller context windows mean lower inference cost and faster time-to-answer, which compounds across large automations that need to consult many endpoints.

---

## Local Docs vs. Hosted llms.txt — Summary

| | Local Docs (this repo) | Hosted llms.txt |
|---|---|---|
| **Discovery speed** | Fast — grep/find in <1s | Slow — 5–7 HTTP round-trips |
| **Tool calls per question** | 2–3 local reads | 5–7 network fetches |
| **Works offline / air-gapped** | Yes | No |
| **Always up to date** | No — requires re-crawl | Yes — live from Autodesk |
| **Covers all APS APIs** | No — curated subset | Yes — full platform |
| **Consistent across time** | Yes — versioned snapshot | No — changes without notice |
| **Setup required** | Yes — crawl scripts to run | No |
| **Crawler maintenance** | Yes — breaks on site changes | No |
| **Targeted prompting** | Yes — link directly to files | No |
| **Token cost per query** | Low — load only what's needed | High — large prompt + raw HTML |
| **New/beta API coverage** | Only after re-crawl | Immediate |
| **Team consistency** | Only if repo is shared/pinned | Always consistent |
