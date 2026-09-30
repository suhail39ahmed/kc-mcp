# Demo — kc-mcp

Honest, fixture-only demos. No fabricated stars, downloads, or production metrics.

## Static preview (README)

![30-second demo](../assets/demo-terminal.svg)

Regenerate after CLI changes:

```bash
pip install -e .
make demo-assets   # → assets/demo-terminal.svg from live fixture output
```

---

## Timed Loom script (60–90 seconds)

| Time | On screen | Say |
|------|-----------|-----|
| 0:00–0:08 | Repo root + large font terminal | "kc-mcp — offline Knowledge Center tools so coding agents can search, cite, and quiz over *your* lesson notes." |
| 0:08–0:20 | `python -m kc_mcp --format text topics` | "Five fixture lessons — Foundry, Databricks RAG, Key Vault, MCP secure use, pipeline failures. No cloud keys." |
| 0:20–0:45 | `python -m kc_mcp --format text search "key vault managed identity" --top-k 2` | "Search returns scored hits with file citations — here Key Vault ops is the top cite. Keyword/TF-IDF MVP, not a hosted RAG claim." |
| 0:45–1:10 | `python -m kc_mcp --format text quiz MCP` | "Quiz generates short prompts from the lesson. Same corpus the agent would search." |
| 1:10–1:25 | Optional: scroll `docs/cursor-mcp.example.json` | "Optional FastMCP stdio + Cursor mcp.json example in the repo." |
| 1:25–1:30 | Outro card | "Clone it, `make demo`. Fixture-first." |

### Exact commands (copy/paste while recording)

```bash
cd kc-mcp
python -m venv .venv && source .venv/bin/activate
pip install -e .
# clear scrollback; font ~16–18pt; dark theme; hide secrets

python -m kc_mcp --format text topics
python -m kc_mcp --format text search "key vault managed identity" --top-k 2
python -m kc_mcp --format text quiz MCP
# machine-check (also what CI runs):
make demo
```

### Talking points (pick 2)

- Who it's for: Azure AI SAs, platform engineers, educators who want agents to cite **their** teaching content.
- What it is NOT: not a production vector DB / hosted RAG platform; not connected to Instagram/YouTube by default.
- Honest MVP: offline fixtures only — no invented usage numbers.

### Outro card (last 3s)

`github.com/suhail39ahmed/kc-mcp`

---

## GIF / screenshot crop tips

- Record at 1280×720 or 1920×1080; crop to the terminal window only (no desktop clutter).
- Keep 2–3 commands visible; pause ~1s after each result before typing the next.
- Prefer `--format text` for Loom; JSON is fine for CI (`make demo`).
- Export: Loom share link + 5–8s GIF loop of the search result (Kap / Peek / `agg` from asciinema).
- Drop optional `assets/demo.gif` later; SVG already covers README until then.

---

## LinkedIn caption draft (manual post — do not auto-post)

Most agent repos I see are a chat UI or a README with no runnable path.

I open-sourced **kc-mcp** — MCP-shaped Knowledge Center tools over teaching notes:

- search with file citations · topics · quiz  
- `make demo` offline — no vector DB bill for the happy path  
- optional Cursor `mcp.json` / FastMCP stdio  

Intentionally **not** a hosted RAG SaaS. It's the pattern I use when agents need to cite *my* enablement content.

→ https://github.com/suhail39ahmed/kc-mcp  

Clone it. Run `make demo`. Tell me what corpus you'd plug in first.

#Azure #AI #MCP #DevOps #SolutionArchitecture #OpenSource

---

## Shot list (3 still frames if no Loom yet)

1. **Topics** — `--format text topics` with 5 lessons listed.  
2. **Search cite** — Key Vault hit with `cite: key-vault-ops.md` and score.  
3. **Quiz** — three MCP secure-use prompts.

Save under `assets/` when captured (`demo-frame-topics.png`, etc.).

---

## CI workflow (install once)

OAuth tokens without the `workflow` scope cannot push `.github/workflows/*`. The workflow YAML lives at [`docs/ci/demo.yml`](./ci/demo.yml).

To enable the README badge, copy it once (with a token that has `workflow`, or via the GitHub UI):

```bash
mkdir -p .github/workflows
cp docs/ci/demo.yml .github/workflows/demo.yml
git add .github/workflows/demo.yml
git commit -m "ci: enable make demo workflow"
git push
```
