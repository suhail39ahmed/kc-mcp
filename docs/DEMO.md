# Demo — kc-mcp

Loom / screen recording script (**60–90 seconds**). Speak calmly; show the terminal, not slides.

## Setup (before record)

```bash
cd kc-mcp
python -m venv .venv && source .venv/bin/activate
pip install -e .
# clear scrollback; font size ~16–18pt; dark theme
```

## Exact click / type script

1. Open terminal at repo root. Say: *"This is kc-mcp — Offline Knowledge Center tools for coding agents — search, cite, and quiz over l…"*
2. Type `make demo` **or** walk the commands below one by one.
1. Run `python -m kc_mcp --help` — wait for JSON / output.
2. Run `python -m kc_mcp topics` — wait for JSON / output.
3. Run `python -m kc_mcp search "key vault managed identity"` — wait for JSON / output.
4. Run `python -m kc_mcp quiz "MCP"` — wait for JSON / output.
3. Scroll the JSON briefly. Call out one concrete field (citation path, `human_approval_required`, findings, report path, etc.).
4. Close with: *"Offline fixtures only — clone it, `make demo`, adopt the pattern."* Link the GitHub repo in the Loom description.

## Talking points (pick 2)

- Who it's for: Azure AI SAs, platform engineers, and educators who want agents to cite **their** teaching content.
- What it is NOT: Not a production vector database or hosted RAG platform
- Honest MVP: no fabricated production metrics

## Outro card (last 3s)

`github.com/suhail39ahmed/kc-mcp`
