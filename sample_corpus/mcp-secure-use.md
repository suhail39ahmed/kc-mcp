# MCP Secure Use Patterns

Topic: Model Context Protocol
Tags: mcp, security, agents, tools

## Key points
- MCP servers expose tools; treat every tool as privileged API surface.
- Least privilege: narrow tools, dry-run defaults, human approval for mutating actions.
- Never return raw secrets from tools; redact and audit log all invocations.
- Prefer fixture/offline modes for demos so agents cannot touch production.
- Validate tool arguments; reject path traversal and unexpected shell injection.

## Clip notes
Reel covered: MCP threat model for enterprise SA — tools that call Azure must be dry-run by default.
