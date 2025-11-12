# Contributing to D&D MCP Servers

Thank you for your interest in contributing to the D&D MCP Servers project!

## Project Philosophy

This project is designed as a **learning resource** for understanding and building MCP (Model Context Protocol) servers. The primary goals are:

1. Learn how to code MCP servers using the official Python SDK
2. Create modular, well-structured server components
3. Build D&D-related tools and resources accessible via MCP

## Adding a New MCP Server

Follow these steps to add a new MCP server to the project:

### 1. Create the Server Directory

```bash
mkdir -p src/servers/your_server_name
```

### 2. Create Required Files

Create `__init__.py`:
```python
"""Your Server Name MCP Server package."""

from .server import server

__all__ = ["server"]
```

Create `server.py` using the hello_world server as a template:
```python
"""
Your Server Name MCP Server

Description of what your server does.
"""

import asyncio
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Create server instance
server = Server("your-server-name")

@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="your_tool",
            description="Description of your tool",
            inputSchema={
                "type": "object",
                "properties": {
                    # Define your tool's input parameters
                },
            },
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool execution."""
    if name == "your_tool":
        # Implement your tool logic
        return [TextContent(type="text", text="Your response")]
    
    raise ValueError(f"Unknown tool: {name}")

async def main():
    """Main entry point for the server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="your-server-name",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### 3. Test Your Server

Test your server using the MCP Inspector:
```bash
npx @modelcontextprotocol/inspector python src/servers/your_server_name/server.py
```

### 4. Document Your Server

Add a section to the main README.md describing:
- What your server does
- What tools/resources it provides
- How to use it
- Any specific D&D rules or mechanics it implements

### 5. Submit Your Changes

Create a pull request with:
- Your new server code
- Updated documentation
- Examples of how to use your server

## Code Style Guidelines

- Follow PEP 8 Python style guide
- Use type hints for function parameters and return values
- Include docstrings for all functions and classes
- Keep functions focused and single-purpose
- Add comments for complex logic

## MCP Server Best Practices

1. **Use descriptive names**: Tool and resource names should clearly indicate their purpose
2. **Provide good descriptions**: Help users understand what each tool does
3. **Define clear schemas**: Use JSON Schema to define tool input parameters
4. **Handle errors gracefully**: Return meaningful error messages
5. **Keep it simple**: Start with basic functionality and expand gradually

## Resources for Learning

- [MCP Python SDK Documentation](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Specification](https://modelcontextprotocol.io/)
- D&D SRD (System Reference Document) for rules implementation

## Questions?

If you have questions or need help, please:
1. Check the hello_world server example
2. Review the MCP SDK documentation
3. Open an issue for discussion

Happy coding! 🎲
