"""
Character management logic for D&D characters.
Handles character creation, updates, retrieval, and listing.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
import datetime


@dataclass
class Character:
    """Represents a D&D character with life points, properties, and magic points."""
    
    character_id: str
    name: str
    current_hp: int
    max_hp: int
    current_magic_points: int
    max_magic_points: int
    properties: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.UTC).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.UTC).isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert character to dictionary."""
        return asdict(self)
    
    def update_timestamp(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.datetime.now(datetime.UTC).isoformat()


class CharacterManager:
    """Manages D&D characters in memory."""
    
    def __init__(self):
        self._characters: Dict[str, Character] = {}
    
    def set_character(
        self,
        character_id: str,
        name: str,
        current_hp: int,
        max_hp: int,
        current_magic_points: int,
        max_magic_points: int,
        properties: Optional[Dict[str, Any]] = None
    ) -> Character:
        """
        Create or completely replace a character.
        
        Args:
            character_id: Unique identifier for the character
            name: Character name
            current_hp: Current hit points
            max_hp: Maximum hit points
            current_magic_points: Current magic points
            max_magic_points: Maximum magic points
            properties: Dictionary of character properties (strength, dexterity, etc.)
        
        Returns:
            The created/updated Character object
        
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
        
        character = Character(
            character_id=character_id,
            name=name,
            current_hp=current_hp,
            max_hp=max_hp,
            current_magic_points=current_magic_points,
            max_magic_points=max_magic_points,
            properties=properties or {}
        )
        
        self._characters[character_id] = character
        return character
    
    def get_character(self, character_id: str) -> Character:
        """
        Retrieve a character by ID.
        
        Args:
            character_id: Unique identifier for the character
        
        Returns:
            The Character object
        
        Raises:
            ValueError: If character not found
        """
        if character_id not in self._characters:
            raise ValueError(f"Character with ID '{character_id}' not found")
        
        return self._characters[character_id]
    
    def update_character(
        self,
        character_id: str,
        name: Optional[str] = None,
        current_hp: Optional[int] = None,
        max_hp: Optional[int] = None,
        current_magic_points: Optional[int] = None,
        max_magic_points: Optional[int] = None,
        properties: Optional[Dict[str, Any]] = None
    ) -> Character:
        """
        Update specific fields of an existing character.
        
        Args:
            character_id: Unique identifier for the character
            name: New character name (optional)
            current_hp: New current hit points (optional)
            max_hp: New maximum hit points (optional)
            current_magic_points: New current magic points (optional)
            max_magic_points: New maximum magic points (optional)
            properties: Dictionary of properties to update/add (optional)
        
        Returns:
            The updated Character object
        
        Raises:
            ValueError: If character not found or invalid values provided
        """
        character = self.get_character(character_id)
        
        # Update fields if provided
        if name is not None:
            character.name = name
        
        if max_hp is not None:
            if max_hp < 1:
                raise ValueError("Maximum HP must be at least 1")
            character.max_hp = max_hp
        
        if current_hp is not None:
            if current_hp < 0:
                raise ValueError("Current HP cannot be negative")
            if current_hp > character.max_hp:
                raise ValueError("Current HP cannot exceed maximum HP")
            character.current_hp = current_hp
        
        if max_magic_points is not None:
            if max_magic_points < 0:
                raise ValueError("Maximum magic points cannot be negative")
            character.max_magic_points = max_magic_points
        
        if current_magic_points is not None:
            if current_magic_points < 0:
                raise ValueError("Current magic points cannot be negative")
            if current_magic_points > character.max_magic_points:
                raise ValueError("Current magic points cannot exceed maximum magic points")
            character.current_magic_points = current_magic_points
        
        if properties is not None:
            # Update/merge properties
            character.properties.update(properties)
        
        character.update_timestamp()
        return character
    
    def list_characters(self) -> List[Character]:
        """
        List all characters.
        
        Returns:
            List of all Character objects
        """
        return list(self._characters.values())
    
    def delete_character(self, character_id: str) -> None:
        """
        Delete a character by ID.
        
        Args:
            character_id: Unique identifier for the character
        
        Raises:
            ValueError: If character not found
        """
        if character_id not in self._characters:
            raise ValueError(f"Character with ID '{character_id}' not found")
        
        del self._characters[character_id]


# Global character manager instance
_character_manager = CharacterManager()


def get_character_manager() -> CharacterManager:
    """Get the global character manager instance."""
    return _character_manager
