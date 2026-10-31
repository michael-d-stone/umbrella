# Umbrella — Decision Register

**As of:** 2026-10-30  
Statuses reflect conversation intent, *not* implementation completion.

| ID | Status | Decision / direction | Notes |
| --- | --- | --- | --- |
| U-001 | **Accepted** | Umbrella is a small, shared foundation, not a universal replacement app. | Identity, relationships, access, provenance, history. |
| U-002 | **Accepted** | Build for personal usefulness first; StashOS and SlutOS are initial integrations. | Universal contract stays small. |
| U-003 | **Accepted** | Independently developed apps can integrate without asking for core changes. | Optional standalone / siloed operation. |
| U-004 | **Accepted** | Stable `umbrellaID`s enable cross-domain references. | Not a universal domain schema; exact ID design open. |
| U-005 | **Accepted** | Relationships and provenance persist across application domains. | Edge schema / permissions open. |
| U-006 | **Accepted target** | Umbrella's live transactional authority is PostgreSQL. | Existing media-analysis SQLite need not be migrated immediately. |
| U-007 | **Accepted design intent** | One meaningful saved action maps to one logical Git commit. | Journal protocol not implemented/designed in detail. |
| U-008 | **Accepted design intent** | Durable journal/outbox coordinates Postgres actions and Git history. | Atomicity/retry/reconciliation still open. |
| U-009 | **Accepted design intent** | Deletion/lifecycle history uses tombstones where appropriate. | Hard-delete/privacy rules open. |
| U-010 | **Accepted** | ZFS snapshots are a supplementary recovery layer. | Backups and tested restores still required. |
| U-011 | **Accepted** | One responsive UI covers different devices and distances. | Near / Touch / Couch modes. |
| U-012 | **Accepted** | Remember view mode separately per device; user can override. | Independent of screen dimensions. |
| U-013 | **Agreed direction** | Build the primary UI as a web app. | Local native/helper components remain possible. |
| U-014 | **Agreed direction** | Private VPN + HTTPS + nginx + application API. | Network/cert/auth details undecided. |
| U-015 | **Open** | Run server on existing Debian computer or Raspberry Pi 4. | No host chosen. |
| U-016 | **Proposed later** | Installable PWA/app window for app-like couch experience. | Chromium app-window pattern also available. |
| U-017 | **Open** | Frontend framework. | Deliberately deferred. |
| U-018 | **Open** | Detailed integration API, identity schema, permission design and repo layout. | Keep app independence central. |
| U-019 | **Proposed later** | Interactive AI workbench. | Not part of initial build. |

## Conflict resolution / migration notes

Older SlutOS/media-analyzer discussions mentioned **SQLite** as the working store and **PostgreSQL** as a possible future destination. The explicit later Umbrella architecture discussions (2026-10-28) chose PostgreSQL as the **Umbrella target**. This is a temporal distinction; it should not be rewritten as if earlier tools already use PostgreSQL.

Earlier design exploration sometimes used SlutOS and Umbrella interchangeably as the shared connective layer. The more recent architecture differentiates **Umbrella** (common layer) from **StashOS** (media application) and **SlutOS** (observation/pattern application). Precise ownership is still subject to design.
