"""
Dungeons & Dragons Character MCP Server
This server manages D&D character data including life points, magic points, and properties.
"""

import asyncio

# --- Start of path modification ---
import sys
import os

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
    INVALID_PARAMS,  # noqa: F401
    INTERNAL_ERROR,  # noqa: F401
)

from src.servers.DnD_character import tools

# Create server instance
server = Server("Dungeons & Dragons Character MCP Server")


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
    Routes to the appropriate character management tool.
    """
    if tools.get_tool(name) is None:
        raise ValueError(f"Unknown tool: {name}")
    
    # Route to the appropriate tool executor
    if name == "Set Character":
        return tools.execute_set_character(arguments)
    elif name == "Get Character":
        return tools.execute_get_character(arguments)
    elif name == "Update Character":
        return tools.execute_update_character(arguments)
    elif name == "List Characters":
        return tools.execute_list_characters(arguments)
    elif name == "Delete Character":
        return tools.execute_delete_character(arguments)
    else:
        raise ValueError(f"Tool '{name}' not implemented")


async def main():
    """Main entry point for the server."""
    # Run the server using stdin/stdout streams
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="dnd-character",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
