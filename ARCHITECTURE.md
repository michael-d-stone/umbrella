# Umbrella — Architecture and Boundaries

**Snapshot:** 2026-10-30

## What Umbrella is

A **shared foundation** that keeps identity, relationships, access, provenance, and meaningful history durable across applications. The motivating problem is not merely retaining data bytes: years later, files and records should still have discoverable **meaning, context, origin, relationships, and revision history**.

Umbrella itself stays deliberately small. StashOS, SlutOS, Etsy tools, and future applications can have their own interfaces, data structures, and development schedules.

## Guiding decisions (accepted)

1. **Personal usefulness first:** build what directly helps the owner, beginning with StashOS and SlutOS. Do not overbuild a universal platform before those apps are useful.
2. **Universal identity, not universal schema:** Umbrella assigns or recognizes stable, addressable `umbrellaID`s. It does not dictate how every kind of record must be modeled internally.
3. **Applications are independently useful:** other developers can build compatible software without needing permission from Umbrella's author or modifications to its core.
4. **Sharing is optional:** an application can operate standalone or within a silo; Umbrella participation should not require publishing every piece of its data to every other app.
5. **Relationships cross domains:** a media item, a file, an event, a purchase, or a person may be linked when there is useful meaning in that relationship. The exact relationship vocabulary is extensible.
6. **History is not casually overwritten:** corrections, reversions, and deletions preserve context; derived AI interpretations are not silently promoted to observed facts.
7. **Open-source and approachability matter:** integration should be a comprehensible contract, not a need to rewrite an app around one framework.

## Logical responsibilities

### Umbrella's small common layer

- Resolve stable identity, including references to external application identities.
- Carry basic type/domain metadata so a record can be understood without forcing a common payload schema.
- Express relationships between identified records.
- Define access boundaries and permissions for shared data (authorization mechanism not designed yet).
- Record provenance, timestamps, durable actions, and lifecycle history.
- Provide integration/retrieval contracts that apps can use voluntarily.

### Application-owned domains

- App-specific records, fields, indexes, workflows, search, editing, playback, and user experience.
- Domain-specific interpretation and validation.
- Ability to continue operating without depending on every other Umbrella app.

### Not an immediate Umbrella requirement

- One universal record table containing all domain data.
- One mandatory database/schema/service/repository for every application.
- An interactive AI workbench (an optional, later-stage idea).
- Migrating all old tools before useful applications can exist.

## Example of a cross-app relationship

An application might know a video by its own database ID and filesystem path. Umbrella's stable identity gives that item an addressable shared referent. A SlutOS observation may then point to that referent without copying the StashOS video schema or having to adopt StashOS's internal ID.

**Unspecified:** How the shared identifier is minted, how types are registered, exactly how relationship edges are stored, and what API/authorization calls are needed.

## Integration contract: intent, not finalized protocol

A minimum useful contract likely exposes:

- Stable identity and the app/domain that owns a record.
- A type or capability descriptor without a universal rigid schema.
- Shared relationship operations and referent resolution.
- Explicit access rules for what the requesting app may read/change.
- Origin/provenance and change/history information.

Endpoint names, authentication, versioning, schema evolution, transport, and standalone/offline reconciliation are **open**. Do not treat the list as a finished API.
