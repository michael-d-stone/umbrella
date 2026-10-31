# Umbrella — Architecture Notes

**Working snapshot:** 2026-10-30  
**Status:** Reconstructed design record; not a specification or implemented-system description.

Umbrella is the small, reusable foundation underneath independently useful applications. It gives records stable identity, lets applications express meaningful relationships, controls shared access, and preserves history and provenance. It is **not** a giant application that absorbs every specialized tool.

The near-term purpose is personal: make **StashOS** and **SlutOS** useful. The foundation should still be small and general enough that independent developers can make their own applications Umbrella-compatible without asking for permission or requiring core changes.

## Where to read

| Document | Contents |
| --- | --- |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Purpose, layers, boundaries, and integration principles |
| [DATA-AND-HISTORY.md](DATA-AND-HISTORY.md) | `umbrellaID`, PostgreSQL, Git, journal, tombstones, ZFS |
| [APPLICATIONS.md](APPLICATIONS.md) | StashOS, SlutOS, external integrations and what stays separate |
| [UI-AND-DEPLOYMENT.md](UI-AND-DEPLOYMENT.md) | Web UI, Near/Touch/Couch modes, nginx, HTTPS, VPN, host choices |
| [DECISIONS.md](DECISIONS.md) | Accepted decisions vs. directions vs. proposals |
| [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) | What remains undecided; no premature implementation choices |

## How to read the status labels

- **Accepted:** The user explicitly chose this direction in conversations.
- **Direction:** A working architecture choice discussed and agreed as a default, but not final implementation detail.
- **Proposal:** A possible feature, tool, or design idea; not approved as a requirement.
- **Open:** No settled decision or no enough evidence to call it settled.

## Schematic (conceptual, not deployment topology)

```text
Independently useful applications / external sources
     |                  |                  |
  StashOS             SlutOS          future apps
     \                  |                  /
       optional Umbrella integration contract
             | identity / type / access
             | relationships / provenance / time
             | durable actions / history
             v
       PostgreSQL transactional state
       journal/outbox -> Git logical history
       file/object storage -> ZFS snapshots
```

An app may remain independent, or may opt into sharing only some records/relationships. **No box here dictates a microservice, process, language, or database schema.**

## Sources and limits

This snapshot consolidates the Umbrella conversation of **2026-10-30**, three Project sources all titled `Responsive view modes.txt`, and prior Umbrella discussions (particularly **2026-10-28–29**) recoverable from conversation context. Earlier SlutOS discussions supplied additional background on existing media-analysis work.

This is a **first pass**, not an exhaustive audit of every prior Project conversation or all files on the Debian machine. In particular, any code repositories and older Project-source attachments that were not accessible in this pass have **not** been reviewed. When source discussions disagreed across time, later explicit Umbrella choices are described as target architecture, while existing tool implementations are described separately.
