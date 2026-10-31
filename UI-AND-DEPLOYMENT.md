# Umbrella — UI and Deployment

**Snapshot:** 2026-10-30

## 1. Web interface as default

**Agreed direction:** Umbrella uses a responsive web application so the same system can be accessed from an iPhone, a Debian/i3wm desktop, tablets, and large displays. It should **feel like an application**, not a website that demands constant manual zoom or browser management.

Not every local capability has to be implemented in browser JavaScript. Media playback via mpv or privileged filesystem operations may need backend services or an optional local companion/helper. The concrete solution is **open**.

**Frontend framework:** not chosen. Avoid deciding React/Vue/etc. ahead of the actual UI work.

## 2. Screen size is not viewing distance

**Accepted:** Layout adapts to available viewport size *and* to user-selected viewing style/distance; the latter must not be inferred from screen size alone.

| Mode | Intended feel |
| --- | --- |
| **Near** | Normal desk distance; denser information, comfortable mouse/keyboard use |
| **Touch** | Finger-friendly targets and spacing, mobile/tablet interaction |
| **Couch** | Readability from roughly 10 feet, larger text and targets, fewer elements, keyboard/remote navigability |

**Accepted:** Remember the selected view mode **per device**, allowing manual override. A large monitor is not necessarily a television, and a particular device may be used differently at different times.

Candidate implementation techniques are CSS custom properties, Grid/Flexbox, container queries and shared component styling—**smart CSS**, not separate cloned applications. Actual type scales and control dimensions remain to be tested.

## 3. Browser chrome versus application chrome

Observed problem: page zoom can make website content readable from a couch while browser toolbars, address bars, and tabs remain hard to read under i3wm.

**Working solution:** optionally run Umbrella in Chromium's application-window mode or an installed PWA-style window. Give Umbrella its own legible in-app navigation/search controls, rather than requiring tiny browser UI for routine use. Ordinary browser mode should still work.

Example *pattern*, not an actual configured Umbrella address:

```sh
chromium --app=https://<your-private-umbrella-host>/
```

A PWA is a **later possibility**, not an immediate prerequisite.

## 4. Private deployment path

**Agreed default architecture:**

```text
Client browser/app window
  -> private VPN network
  -> HTTPS
  -> nginx (serves web UI / reverse-proxies API)
  -> Umbrella application API/services
  -> PostgreSQL and data storage
```

- Keep Umbrella private; do not expose its API/database directly to the public Internet.
- HTTPS still matters inside a VPN: browsers recognize HTTPS as a secure context and can use the associated secure web features.
- nginx is a reverse-proxy/web-serving default, not a commitment to a full frontend stack.
- Restrict network listeners/firewall rules so the VPN is a real access boundary; a VPN client installed on a server does not automatically make public listeners private.
- VPN product, DNS, certificate provisioning, authentication, and remote-device setup are **not chosen**. Tailscale was mentioned as an *example*, not a mandatory platform.

## 5. Hardware

**Candidates only:** Existing Debian computer **or** Raspberry Pi 4. Hardware choice, whether it is always on, and whether workloads should split across machines are unresolved. Do not commit to a Raspberry Pi performance profile before checking actual video/media workload and storage needs.

## 6. Visual character

A clean, spacious and highly legible UI; simple grouped search results, with usability from a phone close up or a couch at a distance. Typography explored includes Futura, Hind and Libre Baskerville, with Libre Baskerville currently the more comfortable serif candidate than Cormorant Garamond. These are aesthetic preferences, **not** a committed stylesheet or font license choice.
