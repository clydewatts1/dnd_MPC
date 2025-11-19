"""
Unit tests for DnD_monster tools.
"""

import sys
import os
import unittest

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.servers.DnD_monster import tools
from src.servers.DnD_monster.monster_manager import MonsterManager

class TestMonsterTools(unittest.TestCase):
    """Unit tests for the DnD_monster tools."""

    def setUp(self):
        """Set up for the tests."""
        self.manager = MonsterManager()
        tools.monster_manager.monsters.clear()

    def test_set_and_get_monster(self):
        """Test setting and getting a monster."""
        args = {"name": "Goblin", "life_points": {"current": 15, "max": 15}}
        set_result, _ = tools.execute_set_monster(args)
        self.assertEqual(set_result[0]["status"], "success")

        get_result, _ = tools.execute_get_monster({"name": "Goblin"})
        self.assertEqual(get_result[0]["name"], "Goblin")
        self.assertEqual(get_result[0]["life_points"]["current"], 15)

    def test_update_monster(self):
        """Test updating a monster."""
        args = {"name": "Orc", "life_points": {"current": 30, "max": 30}}
        tools.execute_set_monster(args)

        update_args = {"name": "Orc", "properties": {"weapon": "Axe"}}
        update_result, _ = tools.execute_update_monster(update_args)
        self.assertEqual(update_result[0]["status"], "success")

        get_result, _ = tools.execute_get_monster({"name": "Orc"})
        self.assertEqual(get_result[0]["properties"]["weapon"], "Axe")

    def test_list_monsters(self):
        """Test listing monsters."""
        tools.execute_set_monster({"name": "Kobold"})
        tools.execute_set_monster({"name": "Troll"})

        list_result, _ = tools.execute_list_monsters({})
        self.assertEqual(len(list_result), 2)
        self.assertIn("Kobold", [c["name"] for c in list_result])

    def test_delete_monster(self):
        """Test deleting a monster."""
        tools.execute_set_monster({"name": "Beholder"})
        delete_result, _ = tools.execute_delete_monster({"name": "Beholder"})
        self.assertEqual(delete_result[0]["status"], "success")

        with self.assertRaises(ValueError):
            tools.execute_get_monster({"name": "Beholder"})

if __name__ == '__main__':
    unittest.main()
