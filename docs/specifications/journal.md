# Durable journal

Status: Required architecture; protocol not yet specified or reviewed.

The journal must coordinate PostgreSQL transactional structured data and Git history. Each meaningful saved user action must correspond to one Git commit. Logical history must preserve revisions, tombstones, and restorations. ZFS snapshots add recovery options but do not replace this coordination.

## Required review before implementation

A protocol proposal must define:

- What constitutes a meaningful saved action and how it is identified across retries and applications.
- Journal durability, representation, ordering, and acknowledgement conditions.
- PostgreSQL transaction boundaries and Git commit contents and references.
- Idempotency, concurrency, conflict handling, and prevention of duplicate action commits.
- Recovery after interruption at every persistence boundary, including disk-full and unavailable-store conditions.
- Reconciliation and detection of missing, duplicated, or divergent records and commits.
- Tombstone and restoration semantics, sensitive-data handling, and historical access controls.
- Snapshot consistency, restore coordination, and operational recovery verification.

These are questions to resolve, not a chosen sequence of writes or an implied distributed transaction design. A reviewed specification should include invariants, a failure matrix, and testable recovery scenarios.

Do not implement PostgreSQL–Git synchronization until its protocol is specified and reviewed. The current discovery experiment never opens PostgreSQL, writes a journal, creates commits, or takes snapshots.
