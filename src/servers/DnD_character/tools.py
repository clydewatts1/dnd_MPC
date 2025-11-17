"""Tool definitions for the Dungeons & Dragons Character MCP Server."""

from mcp.types import Tool
from src.servers.DnD_character.character_manager import get_character_manager


# Tool: Set Character (Create or Replace)
SET_CHARACTER_TOOL = Tool(
    name="Set Character",
    description="Create a new character or completely replace an existing one with new data",
    inputSchema={
        "type": "object",
        "properties": {
            "characterId": {
                "type": "string",
                "description": "Unique identifier for the character",
            },
            "name": {
                "type": "string",
                "description": "Character name",
            },
            "currentHp": {
                "type": "integer",
                "description": "Current hit points",
            },
            "maxHp": {
                "type": "integer",
                "description": "Maximum hit points",
            },
            "currentMagicPoints": {
                "type": "integer",
                "description": "Current magic points",
            },
            "maxMagicPoints": {
                "type": "integer",
                "description": "Maximum magic points",
            },
            "properties": {
                "type": "object",
                "description": "Character properties (e.g., strength, dexterity, intelligence, etc.)",
                "additionalProperties": True,
            },
        },
        "required": ["characterId", "name", "currentHp", "maxHp", "currentMagicPoints", "maxMagicPoints"],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "characterId": {"type": "string"},
            "name": {"type": "string"},
            "currentHp": {"type": "integer"},
            "maxHp": {"type": "integer"},
            "currentMagicPoints": {"type": "integer"},
            "maxMagicPoints": {"type": "integer"},
            "properties": {"type": "object"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"},
        },
        "required": ["characterId", "name", "currentHp", "maxHp", "currentMagicPoints", "maxMagicPoints", "createdAt", "updatedAt"],
    },
)


# Tool: Get Character
GET_CHARACTER_TOOL = Tool(
    name="Get Character",
    description="Retrieve a character by their unique identifier",
    inputSchema={
        "type": "object",
        "properties": {
            "characterId": {
                "type": "string",
                "description": "Unique identifier for the character",
            },
        },
        "required": ["characterId"],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "characterId": {"type": "string"},
            "name": {"type": "string"},
            "currentHp": {"type": "integer"},
            "maxHp": {"type": "integer"},
            "currentMagicPoints": {"type": "integer"},
            "maxMagicPoints": {"type": "integer"},
            "properties": {"type": "object"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"},
        },
        "required": ["characterId", "name", "currentHp", "maxHp", "currentMagicPoints", "maxMagicPoints", "createdAt", "updatedAt"],
    },
)


# Tool: Update Character
UPDATE_CHARACTER_TOOL = Tool(
    name="Update Character",
    description="Update specific fields of an existing character",
    inputSchema={
        "type": "object",
        "properties": {
            "characterId": {
                "type": "string",
                "description": "Unique identifier for the character",
            },
            "name": {
                "type": "string",
                "description": "New character name (optional)",
            },
            "currentHp": {
                "type": "integer",
                "description": "New current hit points (optional)",
            },
            "maxHp": {
                "type": "integer",
                "description": "New maximum hit points (optional)",
            },
            "currentMagicPoints": {
                "type": "integer",
                "description": "New current magic points (optional)",
            },
            "maxMagicPoints": {
                "type": "integer",
                "description": "New maximum magic points (optional)",
            },
            "properties": {
                "type": "object",
                "description": "Properties to update/add (optional)",
                "additionalProperties": True,
            },
        },
        "required": ["characterId"],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "characterId": {"type": "string"},
            "name": {"type": "string"},
            "currentHp": {"type": "integer"},
            "maxHp": {"type": "integer"},
            "currentMagicPoints": {"type": "integer"},
            "maxMagicPoints": {"type": "integer"},
            "properties": {"type": "object"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"},
        },
        "required": ["characterId", "name", "currentHp", "maxHp", "currentMagicPoints", "maxMagicPoints", "createdAt", "updatedAt"],
    },
)


# Tool: List Characters
LIST_CHARACTERS_TOOL = Tool(
    name="List Characters",
    description="List all characters in the system",
    inputSchema={
        "type": "object",
        "properties": {},
        "required": [],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "characters": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "characterId": {"type": "string"},
                        "name": {"type": "string"},
                        "currentHp": {"type": "integer"},
                        "maxHp": {"type": "integer"},
                        "currentMagicPoints": {"type": "integer"},
                        "maxMagicPoints": {"type": "integer"},
                        "properties": {"type": "object"},
                        "createdAt": {"type": "string"},
                        "updatedAt": {"type": "string"},
                    },
                },
            },
            "count": {"type": "integer"},
        },
        "required": ["characters", "count"],
    },
)


# Tool: Delete Character
DELETE_CHARACTER_TOOL = Tool(
    name="Delete Character",
    description="Delete a character by their unique identifier",
    inputSchema={
        "type": "object",
        "properties": {
            "characterId": {
                "type": "string",
                "description": "Unique identifier for the character",
            },
        },
        "required": ["characterId"],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "characterId": {"type": "string"},
            "deleted": {"type": "boolean"},
        },
        "required": ["characterId", "deleted"],
    },
)


TOOLS = {
    SET_CHARACTER_TOOL.name: SET_CHARACTER_TOOL,
    GET_CHARACTER_TOOL.name: GET_CHARACTER_TOOL,
    UPDATE_CHARACTER_TOOL.name: UPDATE_CHARACTER_TOOL,
    LIST_CHARACTERS_TOOL.name: LIST_CHARACTERS_TOOL,
    DELETE_CHARACTER_TOOL.name: DELETE_CHARACTER_TOOL,
}


def get_tool(name: str) -> Tool | None:
    """Get a tool by name."""
    return TOOLS.get(name)


def get_all_tools() -> list[Tool]:
    """Get a list of all available tools."""
    return list(TOOLS.values())


def execute_set_character(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the set character functionality.
    
    Args:
        arguments: Dictionary containing character data
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    character_id = arguments.get("characterId")
    if not character_id:
        raise ValueError("Missing required argument: characterId")
    
    name = arguments.get("name")
    if not name:
        raise ValueError("Missing required argument: name")
    
    current_hp = arguments.get("currentHp")
    max_hp = arguments.get("maxHp")
    current_magic_points = arguments.get("currentMagicPoints")
    max_magic_points = arguments.get("maxMagicPoints")
    properties = arguments.get("properties", {})
    
    if current_hp is None:
        raise ValueError("Missing required argument: currentHp")
    if max_hp is None:
        raise ValueError("Missing required argument: maxHp")
    if current_magic_points is None:
        raise ValueError("Missing required argument: currentMagicPoints")
    if max_magic_points is None:
        raise ValueError("Missing required argument: maxMagicPoints")
    
    manager = get_character_manager()
    character = manager.set_character(
        character_id=character_id,
        name=name,
        current_hp=current_hp,
        max_hp=max_hp,
        current_magic_points=current_magic_points,
        max_magic_points=max_magic_points,
        properties=properties
    )
    
    result = character.to_dict()
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": f"Character '{result['name']}' (ID: {result['character_id']}) created/updated\n"
                   f"HP: {result['current_hp']}/{result['max_hp']}\n"
                   f"Magic Points: {result['current_magic_points']}/{result['max_magic_points']}\n"
                   f"Properties: {result['properties']}",
        }
    ]
    
    return contents, result


def execute_get_character(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the get character functionality.
    
    Args:
        arguments: Dictionary containing characterId
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    character_id = arguments.get("characterId")
    if not character_id:
        raise ValueError("Missing required argument: characterId")
    
    manager = get_character_manager()
    character = manager.get_character(character_id)
    result = character.to_dict()
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": f"Character: {result['name']} (ID: {result['character_id']})\n"
                   f"HP: {result['current_hp']}/{result['max_hp']}\n"
                   f"Magic Points: {result['current_magic_points']}/{result['max_magic_points']}\n"
                   f"Properties: {result['properties']}\n"
                   f"Created: {result['created_at']}\n"
                   f"Updated: {result['updated_at']}",
        }
    ]
    
    return contents, result


def execute_update_character(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the update character functionality.
    
    Args:
        arguments: Dictionary containing character updates
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    character_id = arguments.get("characterId")
    if not character_id:
        raise ValueError("Missing required argument: characterId")
    
    manager = get_character_manager()
    character = manager.update_character(
        character_id=character_id,
        name=arguments.get("name"),
        current_hp=arguments.get("currentHp"),
        max_hp=arguments.get("maxHp"),
        current_magic_points=arguments.get("currentMagicPoints"),
        max_magic_points=arguments.get("maxMagicPoints"),
        properties=arguments.get("properties")
    )
    
    result = character.to_dict()
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": f"Character '{result['name']}' (ID: {result['character_id']}) updated\n"
                   f"HP: {result['current_hp']}/{result['max_hp']}\n"
                   f"Magic Points: {result['current_magic_points']}/{result['max_magic_points']}\n"
                   f"Properties: {result['properties']}",
        }
    ]
    
    return contents, result


def execute_list_characters(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the list characters functionality.
    
    Args:
        arguments: Dictionary (empty for list all)
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    manager = get_character_manager()
    characters = manager.list_characters()
    
    character_list = [char.to_dict() for char in characters]
    result = {
        "characters": character_list,
        "count": len(character_list)
    }
    
    if not character_list:
        text = "No characters found."
    else:
        lines = [f"Found {len(character_list)} character(s):\n"]
        for char_dict in character_list:
            lines.append(
                f"- {char_dict['name']} (ID: {char_dict['character_id']}): "
                f"HP {char_dict['current_hp']}/{char_dict['max_hp']}, "
                f"MP {char_dict['current_magic_points']}/{char_dict['max_magic_points']}"
            )
        text = "\n".join(lines)
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": text,
        }
    ]
    
    return contents, result


def execute_delete_character(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the delete character functionality.
    
    Args:
        arguments: Dictionary containing characterId
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    character_id = arguments.get("characterId")
    if not character_id:
        raise ValueError("Missing required argument: characterId")
    
    manager = get_character_manager()
    manager.delete_character(character_id)
    
    result = {
        "characterId": character_id,
        "deleted": True
    }
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": f"Character with ID '{character_id}' has been deleted.",
        }
    ]
    
    return contents, result
