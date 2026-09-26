# kc-mcp

**Knowledge Center MCP-style tools** over a sample teaching corpus (Instagram reel lesson notes). Offline keyword / TF-IDF search — no embeddings, no cloud calls.

## What it is
- Local tool module + CLI shaped like MCP tools: `search_lessons`, `get_clip_notes`, `list_topics`, `quiz_me`
- 5 sample lesson notes under `sample_corpus/`
- Runs fully offline with fixtures

## What it is not
- Not a production vector DB / RAG platform
- Not a hosted MCP SaaS
- Not connected to Instagram or Azure by default

## Architecture

```
  Agent / CLI
       |
       v
  +------------------+
  |  kc_mcp.server   |  tools: search | get | topics | quiz
  +--------+---------+
           |
           v
  sample_corpus/*.md  (TF-IDF keyword index in-memory)
```

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m kc_mcp.cli topics
python -m kc_mcp.cli search "key vault managed identity"
python -m kc_mcp.cli quiz "MCP"
```

## Demo assets checklist
- [ ] `assets/demo.gif`
- [ ] `assets/architecture.png`
- [ ] See `scripts/record-demo-notes.md` and `docs/DEMO.md`

## License
MIT
