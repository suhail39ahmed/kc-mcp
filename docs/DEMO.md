# Demo — kc-mcp

## 60s script
1. `python -m kc_mcp.cli topics` — show 5 lessons
2. `python -m kc_mcp.cli search "databricks rag"` — show ranked hits with scores
3. `python -m kc_mcp.cli quiz "foundry"` — show offline quiz JSON

## Talking points
- Citations via file path + snippet
- No embeddings required for MVP teaching corpus
- Same tool shapes can later wrap real MCP SDK transport
