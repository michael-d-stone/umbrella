# Architecture

## Agreed foundations

- Universal umbrellaID identities across domains.
- PostgreSQL for transactional structured data.
- A durable journal coordinating PostgreSQL and Git.
- One Git commit per meaningful saved user action.
- Permanent logical history, including revisions, tombstones, and restorations.
- ZFS snapshots as an additional recovery mechanism.
- Independent modules and optional data sharing.
- FOSS-first components, open standards, and replaceable dependencies.
- Reproducible deployments, pinned versions, and user-controlled upgrades.
- Optional AI interfaces and first-class headless operation; a dashboard is optional.

Applications must run standalone, retain their own storage, and control exposed information and capabilities. Umbrella participation must not require project approval, project maintenance, or merging application code. PostgreSQL is Umbrella's structured transactional store; it is not a mandate to replace each application's storage.

## Conceptual boundaries

An independent application's optional adapter declares capabilities. A discovery interface finds declarations. A future authorization and sharing boundary governs actual access. Identity and records can then participate in shared relationships and history according to explicit agreements. Discovery is not trust, identity verification, permission, or execution.

The future journal coordinates database and Git persistence. This is a requirement, not an implemented dual-write mechanism. Git provides meaningful action history; ZFS snapshots provide an additional recovery layer, not a replacement for the journal or logical history.

## Proposed only

The proof of concept uses local JSON declarations and a Python command-line reader to test discovery independently of application code. Its format, file placement, and naming are experiments, not stable interoperability standards. It intentionally has no dependency installation, plugin imports, network calls, database writes, or Git writes.

## Unresolved

Identity format, issuance, domain trust, authentication, linking, recovery, and delegation remain open. Authorization, relationship schemas, record formats, exposure contracts, consent, revocation, retention, and export also require design.

The journal protocol must specify ordering, durability, action boundaries, identifiers, idempotency, concurrency, crash recovery, Git representation, and reconciliation. The meaning of a meaningful saved user action, especially across applications, is unresolved. No PostgreSQL–Git synchronization may be implemented until that protocol is specified and reviewed.

Permanent logical history creates open questions about sensitive data, deletion requirements, encryption, and access to historical records. Snapshot scheduling, off-site recovery, supported deployment versions, and upgrade/rollback procedures are also unresolved. No final implementation is implied here.

See the [decision record](docs/decisions/0001-foundational-architecture.md) and [specifications](docs/specifications/modules.md).
