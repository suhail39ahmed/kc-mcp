# Diagnosing Pipeline Failures

Topic: CI/CD Failures
Tags: azure-devops, github-actions, rca, devops

## Key points
- Separate infrastructure flakes (auth, runners) from test/build failures.
- Capture: failing step name, exit code, first ERROR/FATAL line, and recent change SHA.
- Suggested remediations should be gated behind human approval.
- Keep fixture logs for offline doctor tools so demos stay reproducible.
- Common Azure Pipelines: service connection expiry, NuGet/npm auth, flaky integration tests.

## Clip notes
Reel covered: turning a red pipeline into a structured RCA JSON without auto-applying fixes.
