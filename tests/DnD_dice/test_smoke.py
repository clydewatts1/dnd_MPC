"""
Smoke test for the DnD_dice server.
"""

import sys
import os
import unittest

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

class TestDiceServerSmoke(unittest.TestCase):
    """Smoke test for the DnD_dice server."""

    def test_import_server(self):
        """Test that the server can be imported."""
        try:
            from src.servers.DnD_dice import server
            self.assertIsNotNone(server)
        except ImportError as e:
            self.fail(f"Failed to import DnD_dice server: {e}")

    def test_create_server_instance(self):
        """Test that a Server instance can be created."""
        from src.servers.DnD_dice.server import server
        self.assertIsNotNone(server)

if __name__ == '__main__':
    unittest.main()
