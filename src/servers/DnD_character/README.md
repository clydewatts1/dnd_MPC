# D&D Character MCP Server

A Model Context Protocol (MCP) server for managing Dungeons & Dragons character data.

## Overview

This server provides character management functionality for D&D games, allowing you to create, update, retrieve, and manage character information including:

- **Life Points**: Current and maximum hit points (HP)
- **Magic Points**: Current and maximum magic points pool
- **Properties**: Flexible character attributes (strength, dexterity, intelligence, etc.)
- **Character Metadata**: Creation and update timestamps

## Features

### Tools

The server provides 5 MCP tools:

1. **Set Character** - Create a new character or completely replace an existing one
2. **Get Character** - Retrieve a character by their unique ID
3. **Update Character** - Update specific fields of an existing character
4. **List Characters** - List all characters in the system
5. **Delete Character** - Delete a character by their unique ID

### Character Data Model

Each character includes:

```json
{
  "characterId": "unique-id",
  "name": "Character Name",
  "currentHp": 25,
  "maxHp": 30,
  "currentMagicPoints": 10,
  "maxMagicPoints": 15,
  "properties": {
    "strength": 16,
    "dexterity": 14,
    "constitution": 15,
    "intelligence": 12,
    "wisdom": 10,
    "charisma": 8
  },
  "createdAt": "2025-11-16T12:00:00Z",
  "updatedAt": "2025-11-16T12:30:00Z"
}
```

## Usage

### Running the Server

```bash
# From the project root
python -m src.servers.DnD_character.server
```

### Example Operations

#### Creating a Character

Use the **Set Character** tool:

```json
{
  "characterId": "char-001",
  "name": "Gandalf",
  "currentHp": 30,
  "maxHp": 30,
  "currentMagicPoints": 50,
  "maxMagicPoints": 50,
  "properties": {
    "intelligence": 20,
    "wisdom": 18,
    "charisma": 16
  }
}
```

#### Updating Character HP

Use the **Update Character** tool:

```json
{
  "characterId": "char-001",
  "currentHp": 20
}
```

This will update only the current HP, leaving all other fields unchanged.

#### Retrieving a Character

Use the **Get Character** tool:

```json
{
  "characterId": "char-001"
}
```

#### Listing All Characters

Use the **List Characters** tool with an empty object:

```json
{}
```

## Implementation Details

### Architecture

The server follows the same pattern as the DnD_dice server:

- **server.py**: MCP server setup and tool routing
- **tools.py**: Tool definitions and execution functions
- **character_manager.py**: Core character management logic
- **__init__.py**: Package initialization

### Storage

Characters are stored **in-memory** only. Data will be lost when the server stops. For persistent storage, you would need to add file or database persistence to `character_manager.py`.

### Validation

The character manager validates:

- HP values (max >= 1, current >= 0, current <= max)
- Magic points (max >= 0, current >= 0, current <= max)
- Character existence for get/update/delete operations

## Integration with MCP

This server implements the Model Context Protocol (MCP) and can be used with any MCP-compatible client. Each tool returns both:

1. Human-readable text content
2. Structured data matching the output schema

## Future Enhancements

Potential improvements:

- Persistent storage (JSON file, SQLite, etc.)
- Character search and filtering
- Damage/healing calculations
- Magic point consumption tracking
- Character level and experience tracking
- Equipment and inventory management
