# Naming Guidelines

Source: https://aps.autodesk.com/en/docs/ssa/developers_guide/naming-guidelines/

---

# Naming Guidelines

When naming a secure service account (SSA), use a format that makes it clear to IT admins what the account is for.

**Note:**

- Include the project, company, or purpose in the name.
- Do not use generic names like **robot123** or **testBot**.
- Use hyphens or underscores to separate logical parts for readability.
- Use only lowercase letters (a–z), numbers (0–9), underscores (_), and hyphens (-).
- The name must start and end with a letter or number.
- Length should not exceed 100 characters.
- Do not use spaces, special characters (like @, !, #, $, etc.), or emojis.

We recommend the following format:

```
[service, integration, config]-[company]-[purpose]

```

Examples:

- service-acc-reports
- integration-mycompany-daily_datasync *(sections are separated by the dash character. ``daily_datasync`` is the purpose, which uses an underscore.)*
- config-admin_tasks *(company is omitted)*

This naming convention helps IT quickly identify its function and manage access/permissions appropriately.
