# Databricks RAG Patterns

Topic: Databricks RAG
Tags: databricks, rag, vector-search, lakehouse

## Key points
- RAG on Databricks typically: Delta tables → embedding job → Vector Search → serving endpoint.
- Ground answers in Unity Catalog tables; cite source paths/ids in responses.
- Chunk by document semantics (headers), not arbitrary token windows alone.
- Eval: faithfulness to retrieved context, retrieval hit-rate, latency SLOs.
- Keep PII out of vector indexes unless classified and controlled.

## Clip notes
Reel covered: why "upload PDF → chat" is not enterprise RAG, and how UC governance maps to RAG.
