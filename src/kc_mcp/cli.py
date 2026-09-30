"""CLI for local demos without a full MCP transport."""
from __future__ import annotations

import argparse
import json
import sys

from .server import KnowledgeCenter


def _print_text(cmd: str, out: dict) -> None:
    """Screenshot-friendly text view (fixtures only — no fake metrics)."""
    if cmd == "topics":
        print("kc-mcp · topics (sample_corpus/)")
        print("-" * 52)
        for t in out.get("topics", []):
            tags = ", ".join(t.get("tags", []))
            print(f"  • {t.get('topic', '?'):<28}  {t.get('file', '')}")
            if tags:
                print(f"      tags: {tags}")
        print("-" * 52)
        print(f"{len(out.get('topics', []))} lessons · offline fixtures")
        return
    if cmd == "search":
        results = out.get("results", [])
        print(f"kc-mcp · search → {len(results)} hit(s)")
        print("-" * 52)
        for i, r in enumerate(results, 1):
            score = r.get("score", 0)
            print(f"  {i}. {r.get('title', '?')}  (score {score:.4f})")
            print(f"     cite: {r.get('path', '')} · topic: {r.get('topic', '')}")
            snip = (r.get("snippet") or "").replace("\n", " ")
            if len(snip) > 90:
                snip = snip[:87] + "..."
            print(f"     {snip}")
        print("-" * 52)
        return
    if cmd == "quiz":
        qs = out.get("questions", [])
        print(f"kc-mcp · quiz · {out.get('topic', '?')}")
        print(f"  {out.get('title', '')}")
        print("-" * 52)
        for q in qs:
            print(f"  Q{q.get('id')}: {q.get('prompt', '')}")
            print(f"       hint: {q.get('hint', '')}")
        print("-" * 52)
        print(f"{len(qs)} questions · generated from lesson notes")
        return
    if cmd == "get":
        print(f"kc-mcp · get · {out.get('topic', out.get('title', '?'))}")
        print("-" * 52)
        body = out.get("notes") or out.get("content") or json.dumps(out, indent=2)
        print(body if isinstance(body, str) else json.dumps(body, indent=2))
        return
    if cmd == "tools":
        tools = out.get("tools", [])
        print(f"kc-mcp · {len(tools)} tool schema(s)")
        for t in tools:
            name = t.get("name", t) if isinstance(t, dict) else t
            desc = t.get("description", "") if isinstance(t, dict) else ""
            print(f"  • {name}" + (f" — {desc}" if desc else ""))
        return
    print(json.dumps(out, indent=2))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="kc-mcp", description="Knowledge Center tool CLI (MCP-shaped)")
    p.add_argument(
        "--format",
        choices=("json", "text"),
        default="json",
        help="json (default, machine-friendly) or text (screenshot-friendly)",
    )
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
    if args.format == "text":
        _print_text(args.cmd, out)
    else:
        print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
