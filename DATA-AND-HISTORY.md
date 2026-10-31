# Umbrella — Data, Identity, and Durable History

**Snapshot:** 2026-10-30

## 1. Identity and provenance

**Accepted intent:** Every shareable record can have a stable `umbrellaID` that remains meaningful even if its filename, location, label, or owning app-specific ID changes. Identity is cross-domain; detailed domain schemas remain independent.

Separate at least conceptually:

- Stable Umbrella identity.
- Native source/app identifier(s).
- Filesystem path(s), which may change.
- File content hashes, which identify content but are not necessarily the same thing as conceptual object identity.
- Provenance: source, ingest method, observations, edits and the version of tools/models that produced *derived* information when applicable.

**Open:** ID format, collision policy, import/export/merge behavior, multi-device creation, deduplication rules, type registration, and relation representation.

## 2. PostgreSQL and current tools

**Accepted Umbrella target direction:** PostgreSQL is the authority for Umbrella's live transactional state and queries. This does **not** mean every existing tool has already migrated to PostgreSQL.

Existing media/audio analysis work was described as using SQLite; that is a current implementation fact of a separate tool, not a contradiction of Umbrella's later PostgreSQL architecture decision. Database boundaries, schemas, migrations, and multi-app ownership remain open.

Do **not** expose PostgreSQL directly to browser clients. Umbrella/backend services mediate access.

## 3. Git and the saved-action journal

**Accepted design intent (2026-10-28):** one meaningful saved action corresponds to one logical Git commit so history can be inspected and reconstructed at the level of user actions, not only as opaque database rows.

PostgreSQL and Git do different jobs:

| Component | Intended responsibility |
| --- | --- |
| PostgreSQL | Live, transactional/queryable state |
| Durable journal/outbox | Safely coordinate saved actions and the production of corresponding history entries |
| Git | Human-inspectable, versioned logical history |
| ZFS | Filesystem-level snapshots and recovery |

**Important:** A database transaction and a Git commit are not naturally one atomic operation. A durable handoff/journal (or outbox) is the chosen *architectural intention*, not an implemented protocol. It must tolerate interruption, retry, duplication, and repair without silently losing actions.

**Open technical design:** action envelope, unique action/change IDs, serialization, ordering, retry/idempotency, crash recovery, reconciliation, concurrent writers, Git repository partitioning, and database-to-Git divergence handling. Do not claim a tested implementation exists yet.

## 4. Edits and deletion

**Accepted:** corrections and deletion should leave an auditable lifecycle instead of making inconvenient history vanish. Tombstones are the intended mechanism for representing deletion while retaining the fact it happened.

**Open:** privacy-sensitive permanent erasure, cascading effects, restoration/reversal, tombstone payload, retention, and legal/privacy exceptions.

## 5. ZFS and backup

ZFS snapshots provide a recovery layer for filesystems/datasets, including relevant datasets for the database and projects. They are complementary to Git and PostgreSQL, not substitutes for a planned backup and restore procedure.

**Do not assume** a raw filesystem snapshot of a live database is by itself a complete, tested disaster-recovery plan. Backup consistency, replication/off-machine backups, recovery point expectations, and restore tests are open.

## 6. Source observations vs. interpretation

Keep human observations, imported facts, and AI/algorithm-derived suggestions distinguishable. Preserve provenance and algorithm/model version where feasible; the user remains the authority on personal interpretations. This is especially important for SlutOS analysis and future suggestions.
