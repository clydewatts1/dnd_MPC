"""
Dungeons & Dragons Dice MCP Server
This server will used to simulate dice rolls for Dungeons & Dragons games.
It will throw different types of dice and return the results to the client.
"""

import asyncio

# --- Start of path modification ---
import sys
import os
import datetime


# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
# --- End of path modification ---
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    INVALID_PARAMS, # noqa: F401
    INTERNAL_ERROR, # noqa: F401
)
from pydantic import AnyUrl

from src.servers.DnD_dice import tools
from src.servers.DnD_dice.dice_roller import roll_dice_notation

# Create server instance
server = Server("Dungeons & Dragons DICE MCP Server")


@server.list_tools()
async def handle_list_tools() -> list[tools.Tool]:
    """
    List available tools.
    """
    return tools.get_all_tools()


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> tuple[list[dict], dict]:
    """
    Handle tool execution requests.
    Executes the Throw Dice tool.
    """
    if tools.get_tool(name) is None:
        raise ValueError(f"Unknown tool: {name}")

    # Get the dice notation from arguments
    notation = arguments.get("notation")
    if not notation:
        raise ValueError("Missing required argument: notation")
    
    # Roll the dice using the actual dice rolling logic
    try:
        total, details = roll_dice_notation(notation)
    except ValueError as e:
        raise ValueError(f"Invalid dice notation: {e}")
    
    result = {
        "rollId": arguments.get("rollId"),
        "notation": notation,
        "result": str(total),
        "rolledAt": datetime.datetime.now(datetime.UTC).isoformat(),
    }

    # Return a text content message for humans AND a structured output dict
    # for the MCP framework to validate against outputSchema.
    contents: list[dict] = [
        {
            "type": "text",
            "text": f"Rolled {result['notation']} → {result['result']} (rollId={result['rollId']})\nDetails: {details}",
        }
    ]

    return contents, result



async def main():
    """Main entry point for the server."""
    # Run the server using stdin/stdout streams
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="dnd-dice",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
