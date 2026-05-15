# Architecture Axis

Use this directory for product architecture-specific backup/restore behavior.

- `tidbx/` - TiDBX managed architecture, platform automation, internal service boundaries, cloud-provider integration, and control-plane behavior.
- `classic/` - Classic customer-managed deployments, including TiUP, Kubernetes/TiDB Operator, and self-managed cloud or bare-metal clusters.

Do not duplicate raw ticket content here. Put raw cases under `references/cases/`, then promote reusable architecture-specific learnings into this directory.
