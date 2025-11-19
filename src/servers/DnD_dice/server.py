"""
Dungeons & Dragons Dice MCP Server
This server will used to simulate dice rolls for Dungeons & Dragons games.
It will throw different types of dice and return the results to the client.
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
    Prompt,
    GetPromptRequest,
    ReadResourceRequest,
    INVALID_PARAMS,  # noqa: F401
    INTERNAL_ERROR,  # noqa: F401
)
from pydantic import AnyUrl

from src.servers.DnD_dice import tools

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

    return tools.execute_throw_dice(arguments)


@server.read_resource()
async def handle_read_resource(uri: AnyUrl) -> str:
    """
    Read a resource.
    """
    return f"Hello from DnD_dice resource: {uri}"

@server.get_prompt()
async def handle_get_prompt(name: str, arguments: dict | None = None) -> GetPromptRequest:
    """
    Get a prompt.
    """
    return Prompt(
        name="hello",
        description="A hello world prompt",
        arguments=[]
    )

# Icon and Context handlers are not directly supported by the Server class decorators in this version.
# @server.icon()
# async def handle_get_icon(name: str) -> str:
#     return f"Hello from DnD_dice icon: {name}"

# @server.context()
# async def handle_get_context() -> dict:
#     return {"message": "Hello from DnD_dice context"}




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
