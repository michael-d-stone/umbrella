# Independent modules

Status: Requirements plus an experimental discovery format; no stable module protocol yet.

## Requirements

An application can be developed and released independently, run standalone, and retain its own storage. It decides which records and capabilities it can expose. No approval, code merger, registry listing, or maintenance by Umbrella is required. A module may be a small adapter beside an existing application rather than a rewrite.

## Making an existing application compatible

For this experiment, create a UTF-8 `umbrella-module.json` beside your application or in a separate adapter directory:

```json
{
  "manifest_version": 1,
  "id": "org.example.notes",
  "name": "Independent Notes",
  "capabilities": ["org.example.notes.read"]
}
```

Run `python3 /path/to/umbrella/poc/discover.py /path/to/adapter-parent`. The application and its data can stay outside Umbrella's repository. Removing the manifest from the scanned tree removes it from subsequent discovery. The example uses an illustrative capability name, not a standardized or implemented records API.

Version 1 requires exactly these four fields. `manifest_version` is integer 1; `id` is a nonempty string with no whitespace; `name` is a nonempty string; `capabilities` is a list of unique nonempty strings with no whitespace. Empty capability lists are allowed. IDs must be unique within one scan. These checks are local experiment rules, not global identity guarantees. Module IDs are not umbrellaIDs.

Only files named `umbrella-module.json` under the selected root are read. Symbolic-link files and directories are excluded. Discovery sorts paths and capabilities for consistent output. Invalid declarations, duplicate IDs, missing roots, or unreadable manifests produce an error and no partial result. Declarations are untrusted metadata, never code to load or commands to run.

## Siloing, selective sharing, and disconnection

Today discovery shares no records and invokes no capability. To keep an application entirely outside discovery, omit its manifest or keep it outside selected directories. Discovery itself grants no access.

The future integration contract must default to no sharing and let users grant selected information and capabilities to selected recipients. The manifest is an advertisement, not consent. Existing applications should preserve their standalone interfaces and keep adapters optional. Do not implement a speculative authorization mechanism as if it were agreed.

Future disconnection must revoke future access, stop integration activity, and leave standalone storage usable. Treatment of already shared copies, in-flight actions, identity links, and permanent history needs specification; removing a declaration alone cannot revoke previously issued credentials or erase copies. This proof of concept issues no credentials.

## Open decisions

Capability schemas and version negotiation, transport, authentication, consent, revocation, domain trust, interoperability tests, and record mapping remain unresolved. A future protocol must allow independent implementations without a central approval gate.
