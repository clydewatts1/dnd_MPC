# D&D MCP Servers

A collection of Model Context Protocol (MCP) servers for playing Dungeons and Dragons.

## Project Structure

This project follows a standard structure for organizing multiple MCP servers:

```
dnd_MPC/
├── src/
│   └── servers/
│       └── hello_world/          # Hello World example server
│           ├── __init__.py
│           └── server.py
├── pyproject.toml                # Project configuration and dependencies
├── README.md                     # This file
└── .gitignore
```

## MCP Framework

This project uses the official [Model Context Protocol Python SDK](https://github.com/modelcontextprotocol/python-sdk) to build MCP servers.

### What is MCP?

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. It provides a standardized way to connect AI models with the context they need.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/clydewatts1/dnd_MPC.git
cd dnd_MPC
```

2. Install dependencies:
```bash
pip install -e .
```

For development with testing tools:
```bash
pip install -e ".[dev]"
```

## Hello World Server

The Hello World server is a simple example MCP server that demonstrates basic functionality.

### Features

- **Tool: `say_hello`** - Returns a greeting message
  - Optional `name` parameter (defaults to "World")
  - Returns a customized hello message

### Running the Hello World Server

```bash
python src/servers/hello_world/server.py
```

The server communicates via stdin/stdout using the MCP protocol.

### Testing with MCP Inspector

You can test the server using the MCP Inspector tool:

```bash
npx @modelcontextprotocol/inspector python src/servers/hello_world/server.py
```

### Example Usage

Once connected to an MCP client, you can:

1. List available tools to see `say_hello`
2. Call the tool with:
   - No arguments: Returns "Hello, World! Welcome to the D&D MCP Server!"
   - With name: `{"name": "Gandalf"}` returns "Hello, Gandalf! Welcome to the D&D MCP Server!"

## Adding New Servers

To add a new MCP server:

1. Create a new directory under `src/servers/`:
```bash
mkdir src/servers/your_server_name
```

2. Create `__init__.py` and `server.py` files in the new directory

3. Follow the structure of the hello_world server as a template

4. Implement your server's tools, resources, and prompts as needed

## Project Goals

This project is designed as a learning resource for building MCP servers. The focus is on:

- Understanding the MCP protocol
- Learning how to implement MCP servers in Python
- Creating modular, reusable server components for D&D gameplay

## License

See LICENSE file for details.
