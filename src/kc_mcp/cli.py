"""CLI for local demos without a full MCP transport."""
from __future__ import annotations

import argparse
import json
import sys

from .server import KnowledgeCenter


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="kc-mcp", description="Knowledge Center tool CLI (MCP-shaped)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="search_lessons")
    s.add_argument("query")
    s.add_argument("--top-k", type=int, default=3)

    g = sub.add_parser("get", help="get_clip_notes")
    g.add_argument("topic")

    sub.add_parser("topics", help="list_topics")

    q = sub.add_parser("quiz", help="quiz_me")
    q.add_argument("topic")

    sub.add_parser("tools", help="List tool schemas as JSON")

    args = p.parse_args(argv)
    kc = KnowledgeCenter()
    if args.cmd == "search":
        out = kc.call("search_lessons", {"query": args.query, "top_k": args.top_k})
    elif args.cmd == "get":
        out = kc.call("get_clip_notes", {"topic": args.topic})
    elif args.cmd == "topics":
        out = kc.call("list_topics", {})
    elif args.cmd == "quiz":
        out = kc.call("quiz_me", {"topic": args.topic})
    elif args.cmd == "tools":
        out = {"tools": kc.list_tools()}
    else:
        return 2
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
