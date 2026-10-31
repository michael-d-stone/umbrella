# Umbrella — Open Questions (Not Decisions)

**As of:** 2026-10-30

These are placeholders for decisions as the implementation gets real. They are intentionally **not** an instruction to design everything now.

## First: enough to make the initial apps work

1. **Identity:** ID format/creation, native-ID mapping, import and deduplication, object vs. file-content identity.
2. **Integration boundary:** minimal public API/SDK contract for registering or resolving identity, type, relationships, and access; how an app stays standalone or siloed.
3. **Application ownership:** what StashOS owns vs. what SlutOS observes/analyzes; what crosses the Umbrella boundary.
4. **Persistence topology:** which databases/schemas/processes belong to Umbrella vs. individual apps; migration strategy for existing SQLite-based analyzer data.
5. **Journal/Git implementation:** atomic handoff to outbox, action IDs, ordering, idempotency, Git repository placement, concurrency and recovery/reconciliation.
6. **Private hosting:** Debian or Raspberry Pi 4; VPN product, private DNS, TLS certificate source, authentication, host firewall rules.
7. **First UI slice:** what simple searchable, readable functionality to ship first, including Near/Touch/Couch testing and per-device settings.

## Later, when there is a concrete reason

- Tombstone policy vs. privacy-preserving permanent deletion; restore behavior.
- Off-host backups, PostgreSQL-consistent backups, restore testing, and ZFS replication.
- Local playback interface: browser-native playback vs. mpv and companion process.
- Video similarity/perceptual hashes and where computation runs.
- Whisparr connector versus fork (or no dependency).
- PWA installation/offline behavior.
- AI pattern suggestions, data/consent boundaries, and explainability.
- Interactive AI workbench (last-stage optional idea).

## Documentation process

When a discussion changes the architecture:

1. Add or change an entry in `DECISIONS.md` with a date and status.
2. Update the appropriate subject document rather than growing one giant notes file.
3. Keep discarded ideas or reversals visible as history instead of silently rewriting the past.
4. Commit the docs to Git when the relevant Umbrella repository is established/selected.

**Not yet done:** these files have not been added or committed to any existing GitHub/local repository. The Project source inventory available during this pass included three `Responsive view modes.txt` files, not a complete archive of all earlier materials.
