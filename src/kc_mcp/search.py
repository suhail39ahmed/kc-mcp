"""Embedding-free TF-IDF-ish keyword search over markdown corpus."""
from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

TOKEN = re.compile(r"[a-z0-9][a-z0-9\-_/]+", re.I)


@dataclass
class Doc:
    path: Path
    title: str
    topic: str
    tags: list[str]
    text: str
    tokens: Counter


def _parse_meta(text: str) -> tuple[str, str, list[str]]:
    title = "Untitled"
    topic = ""
    tags: list[str] = []
    for line in text.splitlines()[:20]:
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.lower().startswith("topic:"):
            topic = line.split(":", 1)[1].strip()
        elif line.lower().startswith("tags:"):
            tags = [t.strip() for t in line.split(":", 1)[1].split(",") if t.strip()]
    return title, topic, tags


def load_corpus(corpus_dir: Path) -> list[Doc]:
    docs: list[Doc] = []
    for path in sorted(corpus_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        title, topic, tags = _parse_meta(text)
        tokens = Counter(t.lower() for t in TOKEN.findall(text))
        docs.append(Doc(path, title, topic, tags, text, tokens))
    return docs


def _tfidf_scores(query: str, docs: list[Doc]) -> list[tuple[float, Doc]]:
    q_tokens = [t.lower() for t in TOKEN.findall(query)]
    if not q_tokens or not docs:
        return []
    n = len(docs)
    df: Counter = Counter()
    for d in docs:
        df.update(set(d.tokens))
    idf = {t: math.log((n + 1) / (df[t] + 1)) + 1.0 for t in set(q_tokens)}
    scored: list[tuple[float, Doc]] = []
    for d in docs:
        score = 0.0
        length = sum(d.tokens.values()) or 1
        tagset = {x.lower() for x in d.tags}
        for t in q_tokens:
            tf = d.tokens[t] / length
            score += tf * idf.get(t, 0.0)
            if t in tagset or t in d.topic.lower():
                score += 0.15
        if score > 0:
            scored.append((score, d))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored


def search_lessons(query: str, docs: list[Doc], top_k: int = 3) -> list[dict]:
    hits = _tfidf_scores(query, docs)[:top_k]
    return [
        {
            "title": d.title,
            "topic": d.topic,
            "tags": d.tags,
            "path": str(d.path.name),
            "score": round(score, 4),
            "snippet": d.text[:240].replace("\n", " ") + "...",
        }
        for score, d in hits
    ]


def get_clip_notes(topic_or_file: str, docs: list[Doc]) -> dict | None:
    key = topic_or_file.lower().strip()
    for d in docs:
        if key in d.path.stem.lower() or key in d.topic.lower() or key in d.title.lower():
            return {
                "title": d.title,
                "topic": d.topic,
                "tags": d.tags,
                "path": d.path.name,
                "notes": d.text,
            }
    return None


def list_topics(docs: list[Doc]) -> list[dict]:
    return [{"topic": d.topic or d.title, "file": d.path.name, "tags": d.tags} for d in docs]


def quiz_me(topic: str, docs: list[Doc]) -> dict:
    note = get_clip_notes(topic, docs)
    if not note:
        return {"error": f"No lesson found for '{topic}'", "questions": []}
    lines = [ln.strip("- ").strip() for ln in note["notes"].splitlines() if ln.strip().startswith("- ")]
    questions = []
    for i, point in enumerate(lines[:3], 1):
        questions.append(
            {
                "id": i,
                "prompt": f"True or False / short answer: {point[:120]}...",
                "hint": "Review the Key points section of the lesson.",
            }
        )
    if not questions:
        questions = [{"id": 1, "prompt": f"Summarize the main idea of: {note['title']}", "hint": "See clip notes."}]
    return {"topic": note["topic"], "title": note["title"], "questions": questions}
