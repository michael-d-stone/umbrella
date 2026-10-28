"""Experimental local capability discovery; declarations never execute code."""

import argparse
import json
import os
from pathlib import Path
import sys


class DiscoveryError(ValueError):
    """The selected tree cannot produce a complete, valid discovery result."""


def _unique_fields(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DiscoveryError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


def _token(value):
    return isinstance(value, str) and bool(value) and not any(c.isspace() for c in value)


def _validate(data):
    if not isinstance(data, dict) or set(data) != {
        'manifest_version', 'id', 'name', 'capabilities'
    }:
        raise DiscoveryError('expected exactly manifest_version, id, name, capabilities')
    if type(data['manifest_version']) is not int or data['manifest_version'] != 1:
        raise DiscoveryError('manifest_version must be integer 1')
    if not _token(data['id']):
        raise DiscoveryError('id must be a nonempty string without whitespace')
    if not isinstance(data['name'], str) or not data['name'].strip():
        raise DiscoveryError('name must be a nonempty string')
    capabilities = data['capabilities']
    if not isinstance(capabilities, list) or not all(_token(c) for c in capabilities):
        raise DiscoveryError('capabilities must be a list of nonempty strings without whitespace')
    if len(set(capabilities)) != len(capabilities):
        raise DiscoveryError('capabilities must be unique')
    return {**data, 'capabilities': sorted(capabilities)}


def discover(root):
    """Read manifests under root, raising on any error rather than returning partial data."""
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise DiscoveryError('scan root must be an existing directory, not a symbolic link')
    modules = []
    seen = set()

    def walk_error(error):
        raise error

    try:
        for directory, directories, filenames in os.walk(root, onerror=walk_error, followlinks=False):
            directories[:] = sorted(
                name for name in directories if not (Path(directory) / name).is_symlink()
            )
            if 'umbrella-module.json' not in filenames:
                continue
            path = Path(directory) / 'umbrella-module.json'
            if path.is_symlink():
                continue
            try:
                data = _validate(json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_unique_fields))
            except (ValueError, UnicodeError) as error:
                raise DiscoveryError(f'{path}: {error}') from error
            if data['id'] in seen:
                raise DiscoveryError(f"{path}: duplicate module ID: {data['id']}")
            seen.add(data['id'])
            modules.append(data)
    except OSError as error:
        raise DiscoveryError(str(error)) from error
    return sorted(modules, key=lambda module: module['id'])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path, help='directory containing application declarations')
    args = parser.parse_args(argv)
    try:
        modules = discover(args.root)
    except DiscoveryError as error:
        print(f'discovery error: {error}', file=sys.stderr)
        return 1
    print(json.dumps(modules, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
