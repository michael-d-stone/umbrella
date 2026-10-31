# Contributing

Start by reading the vision, architecture, and foundational decision. Preserve application independence, explicit sharing, headless use, and replaceable dependencies. Prefer small, understandable changes and standard-library solutions where practical. Do not introduce Docker, Kubernetes, microservice infrastructure, or unnecessary dependencies into the initial scaffold.

Run the discovery checks with Python 3.11.2 (the tested baseline):

```sh
python3 -m unittest discover -s poc/tests -v
python3 poc/discover.py examples
```

No dependency installation is needed. Future deployments must pin component versions and provide reproducible procedures; this experiment supplies no deployment stack.

Mark proposals and unresolved decisions clearly. Architecture changes should explain their motivation and consequences in a decision record. PostgreSQL–Git synchronization requires a specified and reviewed protocol before implementation. Never test against existing production databases, services, or application data.

Independent developers can use the experimental declaration in `docs/specifications/modules.md` without submitting their application to this repository. Project approval, maintenance, or merging application code is not a compatibility requirement.

License selection is pending: all rights are reserved until a license is selected. Do not assume a public repository grants open-source reuse rights. Do not add a LICENSE file or source license identifiers before the owner selects a license. Before the first public release, GPLv3, AGPLv3, and Apache 2.0 will be evaluated against FOSS, independent third-party modules, and long-term software freedom goals. Contribution licensing terms must be resolved before accepting external code contributions.
