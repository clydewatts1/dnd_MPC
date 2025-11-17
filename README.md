# D&D MCP Servers

A collection of Model Context Protocol (MCP) servers for playing Dungeons and Dragons.

## Project Structure

This project follows a standard structure for organizing multiple MCP servers:

```
dnd_MPC/
├── src/
│   └── servers/
│       ├── DnD_dice/             # Dice rolling server
│       │   ├── __init__.py
│       │   ├── server.py
│       │   ├── tools.py
│       │   ├── dice_roller.py
│       │   └── README.md
│       ├── DnD_character/        # Character management server
│       │   ├── __init__.py
│       │   ├── server.py
│       │   ├── tools.py
│       │   ├── character_manager.py
│       │   └── README.md
│       ├── DnD_monster/          # Monster management server
│       │   ├── __init__.py
│       │   ├── server.py
│       │   ├── tools.py
│       │   ├── monster_manager.py
│       │   └── README.md
│       └── hello_world/          # Hello World example server
│           ├── __init__.py
│           └── server.py
├── tests/                        # Test files
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

## Available Servers

### 1. DnD Dice Server

Simulates dice rolls for D&D games with support for standard dice notation.

**Features:**
- Roll any combination of D4, D6, D8, D10, D12, D20
- Support for complex notation (e.g., `2d6+3`, `1d20`, `2d3 + 1d6`)
- Detailed roll breakdowns

**Running:**
```bash
python -m src.servers.DnD_dice.server
```

See [DnD_dice/README.md](src/servers/DnD_dice/README.md) for details.

### 2. DnD Character Server

Manages D&D character data including life points, magic points, and properties.

**Features:**
- Create, update, retrieve, list, and delete characters
- Track current/max HP and magic points
- Flexible character properties (strength, dexterity, etc.)

**Running:**
```bash
python -m src.servers.DnD_character.server
```

See [DnD_character/README.md](src/servers/DnD_character/README.md) for details.

### 3. DnD Monster Server

Manages D&D monster data for combat encounters and NPCs.

**Features:**
- Create, update, retrieve, list, and delete monsters
- Track current/max HP and magic points
- Monster-specific properties (challenge rating, armor class, etc.)

**Running:**
```bash
python -m src.servers.DnD_monster.server
```

See [DnD_monster/README.md](src/servers/DnD_monster/README.md) for details.

### 4. Hello World Server

A simple example MCP server demonstrating basic functionality.

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

## Testing with MCP Inspector

You can test any server using the MCP Inspector tool:

```bash
# Test dice server
npx @modelcontextprotocol/inspector python -m src.servers.DnD_dice.server

# Test character server
npx @modelcontextprotocol/inspector python -m src.servers.DnD_character.server

# Test monster server
npx @modelcontextprotocol/inspector python -m src.servers.DnD_monster.server

# Test hello world server
npx @modelcontextprotocol/inspector python src/servers/hello_world/server.py
```

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
- Demonstrating different server patterns (dice rolling, entity management, etc.)

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_dice_roller.py
```

### Project Structure Pattern

Each server follows this pattern:
- `server.py` - MCP server setup and tool routing
- `tools.py` - Tool definitions and execution functions
- `*_manager.py` or `*_roller.py` - Core business logic
- `README.md` - Server-specific documentation

## License

See LICENSE file for details.
