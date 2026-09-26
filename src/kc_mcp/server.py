"""Tool module shaped like an MCP server (stdlib). Full MCP SDK optional later."""
from __future__ import annotations

import os
from pathlib import Path

from .search import get_clip_notes, list_topics, load_corpus, quiz_me, search_lessons

TOOLS = [
    {
        "name": "search_lessons",
        "description": "Keyword/TF-IDF search over Knowledge Center lesson notes.",
        "inputSchema": {
            "type": "object",
            "properties": {"query": {"type": "string"}, "top_k": {"type": "integer"}},
            "required": ["query"],
        },
    },
    {
        "name": "get_clip_notes",
        "description": "Return full clip notes for a topic or filename stem.",
        "inputSchema": {"type": "object", "properties": {"topic": {"type": "string"}}, "required": ["topic"]},
    },
    {
        "name": "list_topics",
        "description": "List available lesson topics in the corpus.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "quiz_me",
        "description": "Generate a short offline quiz for a topic.",
        "inputSchema": {"type": "object", "properties": {"topic": {"type": "string"}}, "required": ["topic"]},
    },
]


class KnowledgeCenter:
    def __init__(self, corpus_dir: Path | None = None):
        root = Path(__file__).resolve().parents[2]
        default = Path(os.environ.get("KC_CORPUS_DIR", str(root / "sample_corpus")))
        self.corpus_dir = Path(corpus_dir) if corpus_dir else default
        self.docs = load_corpus(self.corpus_dir)

    def call(self, name: str, arguments: dict) -> dict:
        if name == "search_lessons":
            return {"results": search_lessons(arguments["query"], self.docs, int(arguments.get("top_k", 3)))}
        if name == "get_clip_notes":
            note = get_clip_notes(arguments["topic"], self.docs)
            return note or {"error": "not found"}
        if name == "list_topics":
            return {"topics": list_topics(self.docs)}
        if name == "quiz_me":
            return quiz_me(arguments["topic"], self.docs)
        return {"error": f"unknown tool: {name}"}

    def list_tools(self) -> list[dict]:
        return TOOLS
