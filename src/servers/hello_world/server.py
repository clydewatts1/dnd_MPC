"""
Hello World MCP Server

A simple MCP server that demonstrates basic functionality.
This server provides a single tool that returns a hello world message.
"""

import asyncio
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    INVALID_PARAMS,
    INTERNAL_ERROR,
)
from pydantic import AnyUrl


# Create server instance
server = Server("hello-world")


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """
    List available tools.
    Returns a tool that says hello to the world or a specified name.
    """
    return [
        Tool(
            name="say_hello",
            description="Says hello to the world or a specified name",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name to greet (optional, defaults to 'World')",
                    }
                },
            },
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[TextContent]:
    """
    Handle tool execution requests.
    Executes the say_hello tool.
    """
    if name != "say_hello":
        raise ValueError(f"Unknown tool: {name}")

    # Get the name parameter, default to "World" if not provided
    target_name = arguments.get("name", "World")

    return [
        TextContent(
            type="text",
            text=f"Hello, {target_name}! Welcome to the D&D MCP Server!",
        )
    ]


async def main():
    """Main entry point for the server."""
    # Run the server using stdin/stdout streams
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="hello-world",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
