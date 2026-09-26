.PHONY: help install demo test clean

help:
	@echo "Targets: install | demo | clean"

install:
	pip install -e .

demo:
	python -m kc_mcp topics >/tmp/kc-topics.json
	python -m kc_mcp search "databricks rag" --top-k 2 >/tmp/kc-search.json
	python -m kc_mcp quiz "foundry" >/tmp/kc-quiz.json
	@echo "✓ kc-mcp demo OK — topics/search/quiz wrote JSON under /tmp" 

clean:
	rm -rf .venv dist build *.egg-info reports labs out audit.log __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
