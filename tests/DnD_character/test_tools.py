"""
Unit tests for DnD_character tools.
"""

import sys
import os
import unittest

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.servers.DnD_character import tools
from src.servers.DnD_character.character_manager import CharacterManager

class TestCharacterTools(unittest.TestCase):
    """Unit tests for the DnD_character tools."""

    def setUp(self):
        """Set up for the tests."""
        self.manager = tools.get_character_manager()
        self.manager.characters.clear()

    def test_set_and_get_character(self):
        """Test setting and getting a character."""
        args = {"name": "Gandalf", "life_points": {"current": 100, "max": 100}, "magic_store": {"current": 50, "max": 50}, "properties": {"class": "Wizard"}}
        set_result, _ = tools.execute_set_character(args)
        self.assertEqual(set_result[0]["status"], "success")

        get_result, _ = tools.execute_get_character({"name": "Gandalf"})
        self.assertEqual(get_result[0]["name"], "Gandalf")
        self.assertEqual(get_result[0]["properties"]["class"], "Wizard")

    def test_update_character(self):
        """Test updating a character."""
        args = {"name": "Aragorn", "life_points": {"current": 120, "max": 120}}
        tools.execute_set_character(args)

        update_args = {"name": "Aragorn", "properties": {"title": "King of Gondor"}}
        update_result, _ = tools.execute_update_character(update_args)
        self.assertEqual(update_result[0]["status"], "success")

        get_result, _ = tools.execute_get_character({"name": "Aragorn"})
        self.assertEqual(get_result[0]["properties"]["title"], "King of Gondor")

    def test_list_characters(self):
        """Test listing characters."""
        tools.execute_set_character({"name": "Legolas"})
        tools.execute_set_character({"name": "Gimli"})

        list_result, _ = tools.execute_list_characters({})
        self.assertEqual(len(list_result), 2)
        self.assertIn("Legolas", [c["name"] for c in list_result])

    def test_delete_character(self):
        """Test deleting a character."""
        tools.execute_set_character({"name": "Boromir"})
        delete_result, _ = tools.execute_delete_character({"name": "Boromir"})
        self.assertEqual(delete_result[0]["status"], "success")

        with self.assertRaises(ValueError):
            tools.execute_get_character({"name": "Boromir"})

if __name__ == '__main__':
    unittest.main()
