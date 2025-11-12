# Testing the Hello World MCP Server

This guide explains how to test the Hello World MCP server.

## Prerequisites

Before testing, you need to install the MCP SDK:

```bash
pip install mcp
```

Or install all project dependencies:

```bash
pip install -r requirements.txt
```

## Method 1: Using MCP Inspector (Recommended)

The MCP Inspector provides a visual interface to interact with your server:

```bash
npx @modelcontextprotocol/inspector python src/servers/hello_world/server.py
```

This will open a web interface where you can:
1. See the available tools
2. Call the `say_hello` tool
3. View the responses

## Method 2: Direct Execution

You can also run the server directly:

```bash
python src/servers/hello_world/server.py
```

The server will wait for JSON-RPC messages on stdin and respond on stdout. This is the standard MCP communication pattern.

## Method 3: Programmatic Testing

Create a test client that communicates with the server using the MCP protocol:

```python
import asyncio
import json
from mcp.client import Client

async def test_hello_world():
    # This is a simplified example
    # In practice, you would use the MCP client library
    # to properly connect to the server
    pass

if __name__ == "__main__":
    asyncio.run(test_hello_world())
```

## Expected Behavior

When you call the `say_hello` tool:

- **Without arguments**: Returns "Hello, World! Welcome to the D&D MCP Server!"
- **With `{"name": "Gandalf"}`**: Returns "Hello, Gandalf! Welcome to the D&D MCP Server!"
- **With `{"name": "Frodo"}`**: Returns "Hello, Frodo! Welcome to the D&D MCP Server!"

## Troubleshooting

### ImportError: No module named 'mcp'

Install the MCP package:
```bash
pip install mcp
```

### Server doesn't respond

Make sure you're using Python 3.10 or higher:
```bash
python --version
```

### Connection issues

The server uses stdio (stdin/stdout) for communication. Make sure your client is properly configured to use this transport method.

## Next Steps

Once you've verified the hello world server works, you can:
1. Explore the server code in `src/servers/hello_world/server.py`
2. Create your own MCP server using the hello world server as a template
3. Add more tools, resources, or prompts to the server
