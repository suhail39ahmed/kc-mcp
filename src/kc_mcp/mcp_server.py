"""Optional MCP stdio server (requires: pip install -e '.[mcp]')."""
from __future__ import annotations

import sys


def main() -> None:
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError:
        print(
            "mcp package not installed. Run: pip install -e '.[mcp]'\n"
            "Or use the CLI: python -m kc_mcp tools",
            file=sys.stderr,
        )
        raise SystemExit(1) from None

    from .server import KnowledgeCenter

    mcp = FastMCP("kc-mcp")
    kc = KnowledgeCenter()

    @mcp.tool()
    def search_lessons(query: str, top_k: int = 3) -> dict:
        """Keyword/TF-IDF search over Knowledge Center lesson notes."""
        return kc.call("search_lessons", {"query": query, "top_k": top_k})

    @mcp.tool()
    def get_clip_notes(topic: str) -> dict:
        """Return full clip notes for a topic or filename stem."""
        return kc.call("get_clip_notes", {"topic": topic})

    @mcp.tool()
    def list_topics() -> dict:
        """List available lesson topics in the corpus."""
        return kc.call("list_topics", {})

    @mcp.tool()
    def quiz_me(topic: str) -> dict:
        """Generate a short offline quiz for a topic."""
        return kc.call("quiz_me", {"topic": topic})

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
