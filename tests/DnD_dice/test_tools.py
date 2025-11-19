"""
Unit tests for DnD_dice tools.
"""

import sys
import os
import unittest

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.servers.DnD_dice import tools

class TestDiceTools(unittest.TestCase):
    """Unit tests for the DnD_dice tools."""

    def test_throw_dice_single(self):
        """Test throwing a single die."""
        args = {
            "notation": "1d6",
            "mcp_type": "event",
            "action": "roll",
            "rollId": "test-roll-1",
            "actor": "tester"
        }
        contents, result = tools.execute_throw_dice(args)
        
        # Check contents (text output)
        self.assertTrue(len(contents) > 0)
        self.assertIn("Rolled 1d6", contents[0]["text"])
        
        # Check result (structured output)
        self.assertEqual(result["notation"], "1d6")
        self.assertEqual(result["rollId"], "test-roll-1")
        self.assertTrue(result["result"].isdigit())
        val = int(result["result"])
        self.assertTrue(1 <= val <= 6)

    def test_throw_dice_multiple(self):
        """Test throwing multiple dice."""
        args = {
            "notation": "3d8",
            "mcp_type": "event",
            "action": "roll",
            "rollId": "test-roll-2",
            "actor": "tester"
        }
        contents, result = tools.execute_throw_dice(args)
        
        val = int(result["result"])
        self.assertTrue(3 <= val <= 24)

    def test_throw_dice_with_modifier(self):
        """Test throwing dice with a modifier."""
        args = {
            "notation": "2d10+5",
            "mcp_type": "event",
            "action": "roll",
            "rollId": "test-roll-3",
            "actor": "tester"
        }
        contents, result = tools.execute_throw_dice(args)
        
        val = int(result["result"])
        self.assertTrue(7 <= val <= 25)

    def test_invalid_dice_notation(self):
        """Test invalid dice notation."""
        args = {
            "notation": "invalid",
            "mcp_type": "event",
            "action": "roll",
            "rollId": "test-roll-4",
            "actor": "tester"
        }
        with self.assertRaises(ValueError):
            tools.execute_throw_dice(args)

if __name__ == '__main__':
    unittest.main()
