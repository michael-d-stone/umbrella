# Local discovery experiment

This independently testable experiment demonstrates that an external application can declare capabilities without modifying Umbrella. It does not implement identity, authorization, data sharing, plugin execution, persistence, or synchronization.

Tested with Python 3.11.2; uses only the standard library. From the repository root:

```sh
python3 poc/discover.py examples
python3 -m unittest discover -s poc/tests -v
```

Point the command at any directory containing third-party declarations, including one outside this repository. It recursively reads `umbrella-module.json` files and prints a deterministic JSON list. No registration in Umbrella source is necessary. The tests create applications in temporary directories to demonstrate this boundary.

A successful scan exits 0, including an empty scan. Invalid input exits 1 and writes an error to stderr without partial JSON on stdout. Symbolic links are excluded. Discovery reads metadata only; selecting a scan root is not a security sandbox against concurrent hostile filesystem changes. Scan directories you control. The manifest protocol is experimental; see the module specification for its rules and limitations.
