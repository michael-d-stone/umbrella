# Identity

Status: Foundational requirement; protocol unresolved.

Universal umbrellaID identities must work across domains and support shared records, relationships, and history without requiring applications to surrender their local identities or storage.

An application must be able to retain its local identifiers. Mapping those identifiers to an umbrellaID must be explicit and governed by a future authorization and consent model. A capability declaration does not establish an identity, prove domain ownership, or authenticate anyone. Experimental module IDs are not umbrellaIDs.

Open decisions include identifier syntax and uniqueness, issuance, domain trust, authentication, account linking and unlinking, collision handling, delegation, key rotation, recovery, migration, and privacy. The relationship between people, organizations, devices, and service identities also requires review. No identifier encoding or trust authority is selected here.

Identity sharing must be optional. Cross-domain correlation and historical identity links need explicit privacy and retention decisions. No identity service is implemented in this repository.
