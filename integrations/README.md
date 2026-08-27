# Integrations

This directory describes public APIs, MCP servers, and service adapters that agents may use. It does not store credentials and it does not imply that a government agency has joined the project.

## Status vocabulary

- `planned`: an idea or target with no verified implementation
- `documented`: official documentation has been read and the capability is described
- `tested-read`: a read-only path was tested against a safe environment or public endpoint
- `tested-write`: a write path was tested with explicit permission and a non-production or reversible case
- `maintained`: a named contributor has a current recheck date and responds to breakage
- `retired`: the path is no longer safe or available

Never use `maintained` without a maintainer, evidence links, and a recheck date.

## Integration manifest

Every integration should document:

- Stable identifier and service name
- Official documentation and terms URLs
- Read and write capabilities separately
- Authentication and approval requirements
- Data sent and data returned
- Rate limits and duplicate behavior
- Error and outage behavior
- Human confirmation requirements
- Test evidence, date, and environment
- Maintainer and next recheck date

The starter manifest is `integrations/catalog.yaml`. It is intentionally empty. Add a real integration only after its documentation and scope are understood.

## MCP guidance

MCP is an interface shape, not a trust guarantee. Treat every tool as potentially capable of exposing data or causing an external effect. Label read and write tools separately. A write-capable tool must return a preview or dry-run result before a confirmation step.
