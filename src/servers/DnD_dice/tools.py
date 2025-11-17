"""Tool definitions for the Dungeons & Dragons DICE MCP Server."""

import datetime
from mcp.types import Tool
from src.servers.DnD_dice.dice_roller import roll_dice_notation

THROW_DICE_TOOL = Tool(
    name="Throw Dice",
    description="Simulates throwing a dice and returns the result",
    inputSchema={
        "type": "object",
        "properties": {
            "mcp_type": {"type": "string", "description": "The type of MCP event."},
             "mcp_return_format": {"type": "string", "description": "The desired return format. ether json or toon ,default is toon."},
            "action": {"type": "string", "description": "The action to perform."},
            "actor": {"type": "string", "description": "The identifier of the actor performing the roll."},
            "rollId": {
                "type": "string",
                "description": "A unique identifier for the roll.",
            },
            "notation": {
                "type": "string",
                "description": "The dice notation (e.g., '2d3 + 1d6').",
            },
            "reason": {"type": "string", "description": "The reason for the roll."},
        },
        "required": ["mcp_type", "action", "rollId", "notation", "actor" ],
    },
    outputSchema={
        "type": "object",
        "properties": {
            "rollId": {"type": "string", "description": "The unique identifier for the roll."},
            "notation": {"type": "string", "description": "The dice notation used."},
            "result": {"type": "string", "description": "The result of the dice roll."},
            "rolledAt": {"type": "string", "description": "The timestamp when the roll was made."},
        },
        "required": ["rollId", "notation", "result", "rolledAt"],
    },
)


TOOLS = {
    THROW_DICE_TOOL.name: THROW_DICE_TOOL,
}


def get_tool(name: str) -> Tool | None:
    """Get a tool by name."""
    return TOOLS.get(name)


def get_all_tools() -> list[Tool]:
    """Get a list of all available tools."""
    return list(TOOLS.values())


def execute_throw_dice(arguments: dict) -> tuple[list[dict], dict]:
    """
    Execute the dice throw functionality.
    
    Args:
        arguments: Dictionary containing rollId, notation, and other parameters
        
    Returns:
        Tuple of (contents list, result dict) for MCP response
    """
    # Get the dice notation from arguments
    notation = arguments.get("notation")
    if not notation:
        raise ValueError("Missing required argument: notation")
    
    # Roll the dice using the actual dice rolling logic
    try:
        total, details = roll_dice_notation(notation)
    except ValueError as e:
        raise ValueError(f"Invalid dice notation: {e}")
    mcp_return_format = arguments.get("mcp_return_format","toon")
    if mcp_return_format == "json":
        contents = [
            {
                "type": "text",
                "text": f"Rolled {notation} → {total} (rollId={arguments.get('rollId')})\nDetails: {details}",
            }
        ]
        result = {
            "rollId": arguments.get("rollId"),
            "notation": notation,
            "result": str(total),
            "rolledAt": datetime.datetime.now(datetime.UTC).isoformat(),
        }
    elif mcp_return_format == "toon":
        contents = [
            {
                "type": "text",
                "text": f"Rolled {notation} → {total} (rollId={arguments.get('rollId')})\nDetails: {details}",
            }
        ]
        result = {
            "rollId": arguments.get("rollId"),
            "notation": notation,
            "result": str(total),
            "rolledAt": datetime.datetime.now(datetime.UTC).isoformat(),
        }
        # default text format
    else:
        contents = [
            {
                "type": "text",
                "text": f"Rolled {notation} → {total} (rollId={arguments.get('rollId')})\nDetails: {details}",
            }
        ]
        result = {
            "rollId": arguments.get("rollId"),
            "notation": notation,
            "result": str(total),
            "rolledAt": datetime.datetime.now(datetime.UTC).isoformat(),
        }   


    # Return a text content message for humans AND a structured output dict
    # for the MCP framework to validate against outputSchema.
    
    return contents, result

