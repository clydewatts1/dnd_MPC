# D&D Monster MCP Server

A Model Context Protocol (MCP) server for managing Dungeons & Dragons monster data.

## Overview

This server provides monster management functionality for D&D games, allowing you to create, update, retrieve, and manage monster information including:

- **Life Points**: Current and maximum hit points (HP)
- **Magic Points**: Current and maximum magic points pool
- **Properties**: Flexible monster attributes (strength, dexterity, armor class, challenge rating, etc.)
- **Monster Metadata**: Creation and update timestamps

## Features

### Tools

The server provides 5 MCP tools:

1. **Set Monster** - Create a new monster or completely replace an existing one
2. **Get Monster** - Retrieve a monster by their unique ID
3. **Update Monster** - Update specific fields of an existing monster
4. **List Monsters** - List all monsters in the system
5. **Delete Monster** - Delete a monster by their unique ID

### Monster Data Model

Each monster includes:

```json
{
  "monsterId": "unique-id",
  "name": "Dragon",
  "currentHp": 200,
  "maxHp": 250,
  "currentMagicPoints": 50,
  "maxMagicPoints": 80,
  "properties": {
    "strength": 22,
    "dexterity": 10,
    "constitution": 20,
    "intelligence": 14,
    "wisdom": 12,
    "charisma": 16,
    "armorClass": 18,
    "challengeRating": 10
  },
  "createdAt": "2025-11-17T12:00:00Z",
  "updatedAt": "2025-11-17T12:30:00Z"
}
```

## Usage

### Running the Server

```bash
# From the project root
python -m src.servers.DnD_monster.server
```

### Testing with MCP Inspector

```bash
npx @modelcontextprotocol/inspector python -m src.servers.DnD_monster.server
```

### Example Operations

#### Creating a Monster

Use the **Set Monster** tool:

```json
{
  "monsterId": "dragon-001",
  "name": "Ancient Red Dragon",
  "currentHp": 250,
  "maxHp": 250,
  "currentMagicPoints": 80,
  "maxMagicPoints": 80,
  "properties": {
    "strength": 22,
    "dexterity": 10,
    "constitution": 20,
    "intelligence": 14,
    "wisdom": 12,
    "charisma": 16,
    "armorClass": 18,
    "challengeRating": 10,
    "type": "Dragon",
    "size": "Gargantuan"
  }
}
```

#### Updating Monster HP (Taking Damage)

Use the **Update Monster** tool:

```json
{
  "monsterId": "dragon-001",
  "currentHp": 180
}
```

This will update only the current HP, leaving all other fields unchanged.

#### Retrieving a Monster

Use the **Get Monster** tool:

```json
{
  "monsterId": "dragon-001"
}
```

#### Listing All Monsters

Use the **List Monsters** tool with an empty object:

```json
{}
```

## Implementation Details

### Architecture

The server follows the same pattern as the DnD_character server:

- **server.py**: MCP server setup and tool routing
- **tools.py**: Tool definitions and execution functions
- **monster_manager.py**: Core monster management logic
- **__init__.py**: Package initialization

### Storage

Monsters are stored **in-memory** only. Data will be lost when the server stops. For persistent storage, you would need to add file or database persistence to `monster_manager.py`.

### Validation

The monster manager validates:

- HP values (max >= 1, current >= 0, current <= max)
- Magic points (max >= 0, current >= 0, current <= max)
- Monster existence for get/update/delete operations

## Integration with MCP

This server implements the Model Context Protocol (MCP) and can be used with any MCP-compatible client. Each tool returns both:

1. Human-readable text content
2. Structured data matching the output schema

## Comparison with DnD_character

This server is structurally identical to the DnD_character server but manages monsters instead of player characters. The main differences are:

- Entity type: Monsters vs Characters
- Typical use cases: Combat encounters, dungeon masters managing NPCs
- Properties: Often include monster-specific attributes (challenge rating, type, size)

## Future Enhancements

Potential improvements:

- Persistent storage (JSON file, SQLite, etc.)
- Monster search and filtering by type, CR, etc.
- Combat-related calculations (damage, healing)
- Monster template/preset loading
- Integration with monster compendiums
- Legendary actions and resistances tracking
- Lair actions and regional effects
- Monster group/encounter management

## Integration with Other Servers

This server can be used alongside:
- **DnD_dice**: For rolling monster attacks and saving throws
- **DnD_character**: For managing player characters in combat encounters
