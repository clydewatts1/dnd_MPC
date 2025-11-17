"""Tool definitions for the Dungeons & Dragons Monster MCP Server."""

from mcp.types import Tool
from src.servers.DnD_monster.monster_manager import get_monster_manager


# Tool: Set Monster (Create or Replace)
SET_MONSTER_TOOL = Tool(
    name="Set Monster",
    description="Create a new monster or completely replace an existing one with new data",
    inputSchema={
        "type": "object",
        "properties": {
            "monsterId": {
                "type": "string",
                "description": "Unique identifier for the monster",
            },
            "name": {
                "type": "string",
                "description": "Monster name",
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
                "description": "Monster properties (e.g., strength, dexterity, armor class, etc.)",
                "additionalProperties": True,
            },
        },
        "required": ["monsterId", "name", "currentHp", "maxHp", "currentMagicPoints", "maxMagicPoints"],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "monsterId": {"type": "string"},
            "name": {"type": "string"},
            "currentHp": {"type": "integer"},
            "maxHp": {"type": "integer"},
            "currentMagicPoints": {"type": "integer"},
            "maxMagicPoints": {"type": "integer"},
            "properties": {"type": "object"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"},
        },
        "required": ["monsterId", "name", "currentHp", "maxHp", "currentMagicPoints", "maxMagicPoints", "createdAt", "updatedAt"],
    },
)


# Tool: Get Monster
GET_MONSTER_TOOL = Tool(
    name="Get Monster",
    description="Retrieve a monster by their unique identifier",
    inputSchema={
        "type": "object",
        "properties": {
            "monsterId": {
                "type": "string",
                "description": "Unique identifier for the monster",
            },
        },
        "required": ["monsterId"],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "monsterId": {"type": "string"},
            "name": {"type": "string"},
            "currentHp": {"type": "integer"},
            "maxHp": {"type": "integer"},
            "currentMagicPoints": {"type": "integer"},
            "maxMagicPoints": {"type": "integer"},
            "properties": {"type": "object"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"},
        },
        "required": ["monsterId", "name", "currentHp", "maxHp", "currentMagicPoints", "maxMagicPoints", "createdAt", "updatedAt"],
    },
)


# Tool: Update Monster
UPDATE_MONSTER_TOOL = Tool(
    name="Update Monster",
    description="Update specific fields of an existing monster",
    inputSchema={
        "type": "object",
        "properties": {
            "monsterId": {
                "type": "string",
                "description": "Unique identifier for the monster",
            },
            "name": {
                "type": "string",
                "description": "New monster name (optional)",
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
        "required": ["monsterId"],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "monsterId": {"type": "string"},
            "name": {"type": "string"},
            "currentHp": {"type": "integer"},
            "maxHp": {"type": "integer"},
            "currentMagicPoints": {"type": "integer"},
            "maxMagicPoints": {"type": "integer"},
            "properties": {"type": "object"},
            "createdAt": {"type": "string"},
            "updatedAt": {"type": "string"},
        },
        "required": ["monsterId", "name", "currentHp", "maxHp", "currentMagicPoints", "maxMagicPoints", "createdAt", "updatedAt"],
    },
)


# Tool: List Monsters
LIST_MONSTERS_TOOL = Tool(
    name="List Monsters",
    description="List all monsters in the system",
    inputSchema={
        "type": "object",
        "properties": {},
        "required": [],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "monsters": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "monsterId": {"type": "string"},
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
        "required": ["monsters", "count"],
    },
)


# Tool: Delete Monster
DELETE_MONSTER_TOOL = Tool(
    name="Delete Monster",
    description="Delete a monster by their unique identifier",
    inputSchema={
        "type": "object",
        "properties": {
            "monsterId": {
                "type": "string",
                "description": "Unique identifier for the monster",
            },
        },
        "required": ["monsterId"],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "monsterId": {"type": "string"},
            "deleted": {"type": "boolean"},
        },
        "required": ["monsterId", "deleted"],
    },
)


TOOLS = {
    SET_MONSTER_TOOL.name: SET_MONSTER_TOOL,
    GET_MONSTER_TOOL.name: GET_MONSTER_TOOL,
    UPDATE_MONSTER_TOOL.name: UPDATE_MONSTER_TOOL,
    LIST_MONSTERS_TOOL.name: LIST_MONSTERS_TOOL,
    DELETE_MONSTER_TOOL.name: DELETE_MONSTER_TOOL,
}


def get_tool(name: str) -> Tool | None:
    """Get a tool by name."""
    return TOOLS.get(name)


def get_all_tools() -> list[Tool]:
    """Get a list of all available tools."""
    return list(TOOLS.values())


def execute_set_monster(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the set monster functionality.
    
    Args:
        arguments: Dictionary containing monster data
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    monster_id = arguments.get("monsterId")
    if not monster_id:
        raise ValueError("Missing required argument: monsterId")
    
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
    
    manager = get_monster_manager()
    monster = manager.set_monster(
        monster_id=monster_id,
        name=name,
        current_hp=current_hp,
        max_hp=max_hp,
        current_magic_points=current_magic_points,
        max_magic_points=max_magic_points,
        properties=properties
    )
    
    result = monster.to_dict()
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": f"Monster '{result['name']}' (ID: {result['monster_id']}) created/updated\n"
                   f"HP: {result['current_hp']}/{result['max_hp']}\n"
                   f"Magic Points: {result['current_magic_points']}/{result['max_magic_points']}\n"
                   f"Properties: {result['properties']}",
        }
    ]
    
    return contents, result


def execute_get_monster(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the get monster functionality.
    
    Args:
        arguments: Dictionary containing monsterId
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    monster_id = arguments.get("monsterId")
    if not monster_id:
        raise ValueError("Missing required argument: monsterId")
    
    manager = get_monster_manager()
    monster = manager.get_monster(monster_id)
    result = monster.to_dict()
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": f"Monster: {result['name']} (ID: {result['monster_id']})\n"
                   f"HP: {result['current_hp']}/{result['max_hp']}\n"
                   f"Magic Points: {result['current_magic_points']}/{result['max_magic_points']}\n"
                   f"Properties: {result['properties']}\n"
                   f"Created: {result['created_at']}\n"
                   f"Updated: {result['updated_at']}",
        }
    ]
    
    return contents, result


def execute_update_monster(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the update monster functionality.
    
    Args:
        arguments: Dictionary containing monster updates
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    monster_id = arguments.get("monsterId")
    if not monster_id:
        raise ValueError("Missing required argument: monsterId")
    
    manager = get_monster_manager()
    monster = manager.update_monster(
        monster_id=monster_id,
        name=arguments.get("name"),
        current_hp=arguments.get("currentHp"),
        max_hp=arguments.get("maxHp"),
        current_magic_points=arguments.get("currentMagicPoints"),
        max_magic_points=arguments.get("maxMagicPoints"),
        properties=arguments.get("properties")
    )
    
    result = monster.to_dict()
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": f"Monster '{result['name']}' (ID: {result['monster_id']}) updated\n"
                   f"HP: {result['current_hp']}/{result['max_hp']}\n"
                   f"Magic Points: {result['current_magic_points']}/{result['max_magic_points']}\n"
                   f"Properties: {result['properties']}",
        }
    ]
    
    return contents, result


def execute_list_monsters(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the list monsters functionality.
    
    Args:
        arguments: Dictionary (empty for list all)
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    manager = get_monster_manager()
    monsters = manager.list_monsters()
    
    monster_list = [monster.to_dict() for monster in monsters]
    result = {
        "monsters": monster_list,
        "count": len(monster_list)
    }
    
    if not monster_list:
        text = "No monsters found."
    else:
        lines = [f"Found {len(monster_list)} monster(s):\n"]
        for monster_dict in monster_list:
            lines.append(
                f"- {monster_dict['name']} (ID: {monster_dict['monster_id']}): "
                f"HP {monster_dict['current_hp']}/{monster_dict['max_hp']}, "
                f"MP {monster_dict['current_magic_points']}/{monster_dict['max_magic_points']}"
            )
        text = "\n".join(lines)
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": text,
        }
    ]
    
    return contents, result


def execute_delete_monster(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the delete monster functionality.
    
    Args:
        arguments: Dictionary containing monsterId
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    monster_id = arguments.get("monsterId")
    if not monster_id:
        raise ValueError("Missing required argument: monsterId")
    
    manager = get_monster_manager()
    manager.delete_monster(monster_id)
    
    result = {
        "monsterId": monster_id,
        "deleted": True
    }
    
    contents: list[dict] = [
        {
            "type": "text",
            "text": f"Monster with ID '{monster_id}' has been deleted.",
        }
    ]
    
    return contents, result
