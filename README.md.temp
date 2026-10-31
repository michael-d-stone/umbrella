# Umbrella

**Make life palatable. Take the power back.**

Umbrella is a FOSS-first, self-hosted platform for making technology easier to use and reducing dependence on constantly changing applications and infrastructure.

It lets independently developed applications participate in shared identity, records, relationships, and history. Each application can still run alone, keep its own storage, and choose which information and capabilities to expose. Compatibility does not require project approval, maintenance by Umbrella, or merging an application into this repository.

Umbrella aims to connect the tools people already use through explicit, user-controlled agreements. It differs in intent from an application suite with a fixed catalog or a platform that requires applications to move into its storage and lifecycle. These are design commitments, not claims of completed functionality. A dashboard is optional; headless use is a first-class requirement. AI may be an interface, never a prerequisite.

## Current status

This repository contains foundational documentation and a local manifest-discovery proof of concept. It is not a working identity, authorization, sharing, history, or synchronization platform. Specifications clearly separate agreed requirements from proposals and open decisions.

## Try discovery

Requires Python 3.11.2 (the tested baseline); no third-party packages, servers, containers, or database are needed.

```sh
python3 poc/discover.py examples
python3 -m unittest discover -s poc/tests -v
```

To discover an existing application, place its declaration in an `umbrella-module.json` file beneath a directory you select, then run `python3 poc/discover.py /path/to/that/directory`. This only reads declarations and prints JSON; it does not run applications or enable sharing. See [the proof of concept](poc/README.md) and [module compatibility](docs/specifications/modules.md).

## Design and participation

Start with [the vision](VISION.md), [architecture](ARCHITECTURE.md), and [foundational decision](docs/decisions/0001-foundational-architecture.md). See [contributing](CONTRIBUTING.md) before proposing changes. No production deployment is provided. Future deployments must use pinned components, reproducible procedures, and user-controlled upgrades.

## License status

License: Undecided — all rights reserved until a license is selected.

FOSS-first describes Umbrella's intended direction; no open-source license is granted yet. Before the first public release, we will evaluate GPLv3, AGPLv3, and Apache 2.0 against the goals of FOSS, independent third-party modules, and long-term software freedom. No LICENSE file or source license identifiers will be added until a license is selected.
