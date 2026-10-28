# 0001: Foundational architecture

Status: Accepted foundational constraints; implementation protocols remain unresolved.

## Context

Umbrella must connect independently developed applications without taking over their storage, development, or ability to run alone. Users need durable history and control over sharing, upgrades, and recovery.

## Decision

Adopt universal umbrellaID identities across domains; PostgreSQL for transactional structured data; a durable journal coordinating PostgreSQL and Git; one Git commit per meaningful saved user action; and permanent logical revisions, tombstones, and restorations. Use ZFS snapshots as an additional recovery mechanism.

Modules remain independent and sharing is optional. Prefer FOSS components, open standards, and replaceable dependencies. Require reproducible deployments, pinned versions, and user-controlled upgrades. Headless operation is first class, dashboards optional, and AI an optional interface.

No central approval, Umbrella maintenance, or code merger is required for third-party compatibility. Applications retain their storage and standalone operation.

## Consequences

Discovery and authorization must be separate. Coordination across database and Git needs an explicit failure and recovery protocol before implementation. Permanent history requires careful treatment of sensitive data and retention. Reproducibility requires recording supported component versions before deployment is offered.

## Deferred

This decision does not select identity encodings, trust models, schemas, journal ordering, action boundaries, deployment topology, or snapshot policies. The local manifest experiment does not settle these decisions. PostgreSQL–Git synchronization awaits a specified and reviewed protocol. License selection is pending.
