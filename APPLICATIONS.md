# Umbrella — Applications and Integrations

**Snapshot:** 2026-10-30

## Priority and scope

**Accepted:** Build Umbrella primarily to make the owner's own applications useful. The first two integration targets are **StashOS** and **SlutOS**. In parallel, make the *small* Umbrella contract sufficiently general that independent developers can integrate their apps. Avoid a broad platform implementation or interactive AI workbench now.

## StashOS — media domain

**Working direction:** a media catalog/metadata/discovery/playback application, developed as a clean-sheet, Stashapp-inspired system rather than simply turning existing Stashapp into Umbrella.

Features discussed or in related development work:

- Media inventory, scanning, metadata and tagging.
- Search and discovery (including a single search input returning grouped categories such as **Videos**, **Performers**, and **Movies**).
- Playback, with **mpv** discussed as a preferred playback path.
- Video similarity / perceptual hashing and duplicate or related-item discovery.
- FFmpeg-related processing, audio stream discovery, and **EBU R128 / LUFS** analysis using existing audio analyzer work.
- Potential scene markers, previews, thumbnails, and recommendations.

**Important distinction:** these are not all shipped features. The prior audio analysis implementation exists separately; integration choices, feature order, and how mpv works with a browser UI remain open.

### Whisparr

Whisparr is a specialized external tool whose functionality might be connected or forked. The aspiration to avoid fragile dependency on Whisparr was discussed; the connector-vs.-fork strategy is **open**. Do not equate Whisparr with Umbrella itself.

## SlutOS — observations, patterns, and improvement

**Working boundary:** SlutOS handles personally meaningful observations, analysis, patterns, relationships, and assistance based on data from across life and media contexts. It need not own the entire media catalog or duplicate StashOS's schema.

- Domain observations and user context remain distinguishable from model inference.
- AI may help recognize patterns and suggest relationships once quality data exists.
- User control, provenance, and explicit access boundaries are fundamental.
- Data may eventually include calendar events, receipts, and other non-media records; do not make the first release depend on integrating every such source.

**Open:** exact StashOS/SlutOS ownership boundaries, cross-app permissions, export and query mechanisms, and AI workflows.

## Other apps and developers

Umbrella should also allow future applications and tools—including existing Etsy work—to choose whether to share identities, relationships, and history. Each app need not adopt Umbrella's internal database or rewrite its domain model.

A future external developer should be able to say, in effect, “these are the identities/types I expose and these are the Umbrella capabilities I elect to use,” without requiring a special core change.

## Not a near-term dependency

An all-purpose interactive AI workbench. It remains optional and deliberately late-stage. The priority is useful apps plus a minimal universal foundation.
