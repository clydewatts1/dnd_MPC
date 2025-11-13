"""Tool definitions for the Dungeons & Dragons DICE MCP Server."""

from mcp.types import Tool

THROW_DICE_TOOL = Tool(
    name="Throw Dice",
    description="Simulates throwing a dice and returns the result",
    inputSchema={
        "type": "object",
        "properties": {
            "mcp_type": {"type": "string", "description": "The type of MCP event."},
            "action": {"type": "string", "description": "The action to perform."},
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
        "required": ["mcp_type", "action", "rollId", "notation"],
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