"""Behavioral checks with independent applications in temporary directories."""

import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from discover import DiscoveryError, discover, main


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def manifest(self, folder='external-app', **changes):
        data = {
            'manifest_version': 1,
            'id': 'org.thirdparty.notes',
            'name': 'Third-party Notes',
            'capabilities': ['notes.write', 'notes.read'],
        }
        data.update(changes)
        path = self.root / folder / 'umbrella-module.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data), encoding='utf-8')
        return path

    def test_external_application_added_and_disconnected_without_source_edits(self):
        self.assertEqual(discover(self.root), [])
        path = self.manifest()
        self.assertEqual(discover(self.root), [{
            'manifest_version': 1,
            'id': 'org.thirdparty.notes',
            'name': 'Third-party Notes',
            'capabilities': ['notes.read', 'notes.write'],
        }])
        path.unlink()
        self.assertEqual(discover(self.root), [])

    def test_deterministic_multiple_applications(self):
        self.manifest('z', id='z.app')
        self.manifest('a', id='a.app', capabilities=[])
        first = discover(self.root)
        self.assertEqual([m['id'] for m in first], ['a.app', 'z.app'])
        self.assertEqual(first, discover(self.root))

    def test_duplicate_ids_fail(self):
        self.manifest('one')
        self.manifest('two')
        with self.assertRaisesRegex(DiscoveryError, 'duplicate module ID'):
            discover(self.root)

    def test_invalid_declarations_fail(self):
        for changes in [
            {'manifest_version': True}, {'manifest_version': 2},
            {'id': ''}, {'id': 'space here'}, {'name': '  '},
            {'capabilities': 'notes.read'}, {'capabilities': [1]},
            {'capabilities': ['a', 'a']}, {'capabilities': ['']},
            {'extra': 'unsupported'},
        ]:
            with self.subTest(changes=changes):
                self.manifest(**changes)
                with self.assertRaises(DiscoveryError):
                    discover(self.root)

    def test_malformed_json_and_duplicate_fields_fail(self):
        path = self.manifest()
        for content in ['{', '[]', '{}', '{"id":"a","id":"b"}']:
            with self.subTest(content=content):
                path.write_text(content, encoding='utf-8')
                with self.assertRaises(DiscoveryError):
                    discover(self.root)

    def test_symlink_files_and_directories_are_excluded(self):
        path = self.manifest('outside')
        scan = self.root / 'scan'
        scan.mkdir()
        (scan / 'umbrella-module.json').symlink_to(path)
        (scan / 'linked-app').symlink_to(path.parent, target_is_directory=True)
        self.assertEqual(discover(scan), [])
        with self.assertRaises(DiscoveryError):
            discover(scan / 'linked-app')

    def test_missing_root_fails(self):
        with self.assertRaises(DiscoveryError):
            discover(self.root / 'missing')

    def test_unreadable_manifest_fails(self):
        self.manifest()
        with patch.object(Path, 'read_text', side_effect=PermissionError('unreadable')):
            with self.assertRaisesRegex(DiscoveryError, 'unreadable'):
                discover(self.root)

    def test_cli_failure_has_no_partial_output(self):
        self.manifest('valid')
        self.manifest('invalid', manifest_version=99)
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            code = main([str(self.root)])
        self.assertEqual(code, 1)
        self.assertEqual(stdout.getvalue(), '')
        self.assertIn('discovery error:', stderr.getvalue())

    def test_cli_success_json(self):
        self.manifest()
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.assertEqual(main([str(self.root)]), 0)
        self.assertEqual(json.loads(stdout.getvalue()), discover(self.root))


if __name__ == '__main__':
    unittest.main()
