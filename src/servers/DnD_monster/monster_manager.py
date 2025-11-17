"""
Monster management logic for D&D monsters.
Handles monster creation, updates, retrieval, and listing.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
import datetime


@dataclass
class Monster:
    """Represents a D&D monster with life points, properties, and magic points."""
    
    monster_id: str
    name: str
    current_hp: int
    max_hp: int
    current_magic_points: int
    max_magic_points: int
    properties: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.UTC).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.UTC).isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert monster to dictionary."""
        return asdict(self)
    
    def update_timestamp(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.datetime.now(datetime.UTC).isoformat()


class MonsterManager:
    """Manages D&D monsters in memory."""
    
    def __init__(self):
        self._monsters: Dict[str, Monster] = {}
    
    def set_monster(
        self,
        monster_id: str,
        name: str,
        current_hp: int,
        max_hp: int,
        current_magic_points: int,
        max_magic_points: int,
        properties: Optional[Dict[str, Any]] = None
    ) -> Monster:
        """
        Create or completely replace a monster.
        
        Args:
            monster_id: Unique identifier for the monster
            name: Monster name
            current_hp: Current hit points
            max_hp: Maximum hit points
            current_magic_points: Current magic points
            max_magic_points: Maximum magic points
            properties: Dictionary of monster properties (strength, dexterity, etc.)
        
        Returns:
            The created/updated Monster object
        
        Raises:
            ValueError: If HP or magic points are invalid
        """
        if max_hp < 1:
            raise ValueError("Maximum HP must be at least 1")
        if current_hp < 0:
            raise ValueError("Current HP cannot be negative")
        if current_hp > max_hp:
            raise ValueError("Current HP cannot exceed maximum HP")
        if max_magic_points < 0:
            raise ValueError("Maximum magic points cannot be negative")
        if current_magic_points < 0:
            raise ValueError("Current magic points cannot be negative")
        if current_magic_points > max_magic_points:
            raise ValueError("Current magic points cannot exceed maximum magic points")
        
        monster = Monster(
            monster_id=monster_id,
            name=name,
            current_hp=current_hp,
            max_hp=max_hp,
            current_magic_points=current_magic_points,
            max_magic_points=max_magic_points,
            properties=properties or {}
        )
        
        self._monsters[monster_id] = monster
        return monster
    
    def get_monster(self, monster_id: str) -> Monster:
        """
        Retrieve a monster by ID.
        
        Args:
            monster_id: Unique identifier for the monster
        
        Returns:
            The Monster object
        
        Raises:
            ValueError: If monster not found
        """
        if monster_id not in self._monsters:
            raise ValueError(f"Monster with ID '{monster_id}' not found")
        
        return self._monsters[monster_id]
    
    def update_monster(
        self,
        monster_id: str,
        name: Optional[str] = None,
        current_hp: Optional[int] = None,
        max_hp: Optional[int] = None,
        current_magic_points: Optional[int] = None,
        max_magic_points: Optional[int] = None,
        properties: Optional[Dict[str, Any]] = None
    ) -> Monster:
        """
        Update specific fields of an existing monster.
        
        Args:
            monster_id: Unique identifier for the monster
            name: New monster name (optional)
            current_hp: New current hit points (optional)
            max_hp: New maximum hit points (optional)
            current_magic_points: New current magic points (optional)
            max_magic_points: New maximum magic points (optional)
            properties: Dictionary of properties to update/add (optional)
        
        Returns:
            The updated Monster object
        
        Raises:
            ValueError: If monster not found or invalid values provided
        """
        monster = self.get_monster(monster_id)
        
        # Update fields if provided
        if name is not None:
            monster.name = name
        
        if max_hp is not None:
            if max_hp < 1:
                raise ValueError("Maximum HP must be at least 1")
            monster.max_hp = max_hp
        
        if current_hp is not None:
            if current_hp < 0:
                raise ValueError("Current HP cannot be negative")
            if current_hp > monster.max_hp:
                raise ValueError("Current HP cannot exceed maximum HP")
            monster.current_hp = current_hp
        
        if max_magic_points is not None:
            if max_magic_points < 0:
                raise ValueError("Maximum magic points cannot be negative")
            monster.max_magic_points = max_magic_points
        
        if current_magic_points is not None:
            if current_magic_points < 0:
                raise ValueError("Current magic points cannot be negative")
            if current_magic_points > monster.max_magic_points:
                raise ValueError("Current magic points cannot exceed maximum magic points")
            monster.current_magic_points = current_magic_points
        
        if properties is not None:
            # Update/merge properties
            monster.properties.update(properties)
        
        monster.update_timestamp()
        return monster
    
    def list_monsters(self) -> List[Monster]:
        """
        List all monsters.
        
        Returns:
            List of all Monster objects
        """
        return list(self._monsters.values())
    
    def delete_monster(self, monster_id: str) -> None:
        """
        Delete a monster by ID.
        
        Args:
            monster_id: Unique identifier for the monster
        
        Raises:
            ValueError: If monster not found
        """
        if monster_id not in self._monsters:
            raise ValueError(f"Monster with ID '{monster_id}' not found")
        
        del self._monsters[monster_id]


# Global monster manager instance
_monster_manager = MonsterManager()


def get_monster_manager() -> MonsterManager:
    """Get the global monster manager instance."""
    return _monster_manager
