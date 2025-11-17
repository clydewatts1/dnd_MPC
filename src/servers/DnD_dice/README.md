# D&D Dice Roller MCP Server

A Model Context Protocol (MCP) server for simulating dice rolls in Dungeons & Dragons games.

## Overview

This server provides dice rolling functionality with support for standard D&D dice notation, including complex expressions with multiple dice types and modifiers.

## Supported Dice

- **D4** - 4-sided die (tetrahedron)
- **D6** - 6-sided die (cube)
- **D8** - 8-sided die (octahedron)
- **D10** - 10-sided die (pentagonal trapezohedron)
- **D12** - 12-sided die (dodecahedron)
- **D20** - 20-sided die (icosahedron)

## Features

### Dice Notation Support

The server supports standard D&D dice notation:

- Simple rolls: `1d20`, `2d6`, `3d8`
- Modifiers: `1d20+5`, `2d6-2`, `3d8+3`
- Multiple dice types: `2d6 + 1d4`, `1d20 + 2d6 + 3`
- Complex expressions: `2d3 + 1d6 + 3`

### MCP Tools

#### Throw Dice

Simulates throwing dice and returns the result.

**Input Schema:**
```json
{
  "mcp_type": "dice_event",
  "mcp_return_format": "json",
  "action": "roll_dice",
  "rollId": "unique-identifier",
  "notation": "2d6+3",
  "reason": "Attack roll"
}
```

**Parameters:**
- `mcp_type` (required): Type of MCP event
- `mcp_return_format` (optional): Return format - "json" or "toon" (default: "toon")
- `action` (required): Action to perform (e.g., "roll_dice")
- `rollId` (required): Unique identifier for the roll
- `notation` (required): Dice notation (e.g., "2d6+3", "1d20", "2d3 + 1d6")
- `reason` (optional): Reason for the roll

**Output Schema:**
```json
{
  "rollId": "unique-identifier",
  "notation": "2d6+3",
  "result": "11",
  "rolledAt": "2025-11-17T10:30:00Z"
}
```

**Example:**
```json
{
  "mcp_type": "dice_event",
  "action": "roll_dice",
  "rollId": "attack_001",
  "notation": "2d6+3",
  "reason": "Longsword attack"
}
```

**Response:**
```json
{
  "rollId": "attack_001",
  "notation": "2d6+3",
  "result": "11",
  "rolledAt": "2025-11-17T10:30:00Z"
}
```

With detailed breakdown:
```
Rolled 2d6+3 → 11 (rollId=attack_001)
Details: 2d6: [4, 4] = 8, modifier: +3, subtotal: 11
```

## Usage

### Running the Server

```bash
# From project root
python -m src.servers.DnD_dice.server
```

### Testing with MCP Inspector

You can test the server using the MCP Inspector tool:

```bash
npx @modelcontextprotocol/inspector python -m src.servers.DnD_dice.server
```

### Example Rolls

1. **Simple d20 roll:**
   ```json
   {
     "mcp_type": "dice_event",
     "action": "roll_dice",
     "rollId": "initiative_001",
     "notation": "1d20",
     "reason": "Initiative roll"
   }
   ```

2. **Damage roll with modifier:**
   ```json
   {
     "mcp_type": "dice_event",
     "action": "roll_dice",
     "rollId": "damage_001",
     "notation": "2d6+3",
     "reason": "Greatsword damage"
   }
   ```

3. **Complex multi-dice roll:**
   ```json
   {
     "mcp_type": "dice_event",
     "action": "roll_dice",
     "rollId": "custom_001",
     "notation": "2d3 + 1d6 + 2",
     "reason": "Custom damage calculation"
   }
   ```

## Implementation Details

### Architecture

- **server.py**: MCP server setup and tool routing
- **tools.py**: Tool definitions and execution functions
- **dice_roller.py**: Core dice rolling logic and notation parsing

### Dice Rolling Logic

The `dice_roller.py` module provides:
- `parse_dice_notation()`: Parses dice notation strings
- `roll_dice()`: Simulates rolling dice
- `roll_dice_notation()`: Complete roll with detailed breakdown

### Notation Parsing

Supports:
- Multiple dice groups: `2d6 + 1d4`
- Modifiers: `1d20+5`, `2d6-2`
- Whitespace flexibility: `2d6+3` or `2 d 6 + 3`

## D&D Dice Reference

### d4 (4-sided die)
**Shape:** Tetrahedron (pyramid)

**Common Uses:**
- Damage for very small weapons (dagger, dart, sling)
- Minor magical effects or healing
- Determining random directions

### d6 (6-sided die)
**Shape:** Cube (standard die)

**Common Uses:**
- Common weapon damage (shortsword, light crossbow)
- Spell damage (Fireball uses multiple d6s)
- Ability score generation (4d6 drop lowest)
- Hit dice for Wizards

### d8 (8-sided die)
**Shape:** Octahedron

**Common Uses:**
- Medium weapon damage (longsword, rapier, shortbow)
- Hit dice for Rogues, Clerics, Monks

### d10 (10-sided die)
**Shape:** Pentagonal trapezohedron

**Common Uses:**
- Large weapon damage (battleaxe, heavy crossbow)
- Hit dice for Fighters, Paladins, Rangers
- Percentage rolls (d100): Two d10s for 1-100

### d12 (12-sided die)
**Shape:** Dodecahedron

**Common Uses:**
- Very large weapon damage (greataxe)
- Hit dice for Barbarians
- Potent monster attacks

### d20 (20-sided die)
**Shape:** Icosahedron

**The Most Important Die** - Used for almost all checks in D&D

**Common Uses:**
- Attack rolls (d20 + modifiers vs AC)
- Ability checks (d20 + modifiers vs DC)
- Saving throws (d20 + modifiers vs spell DC)
- Initiative (d20 + Dexterity modifier)

## Roll Notation Examples

- `3d6+2`: Roll three d6, sum results, add 2
- `1d20+5`: Roll one d20 and add 5
- `2d8`: Roll two d8 and sum results
- `1d4+1d6`: Roll one d4 and one d6, sum both

## Future Enhancements

Potential improvements:
- Advantage/disadvantage rolls (roll twice, take higher/lower)
- Critical hit handling (double dice on natural 20)
- Roll history tracking
- Statistical analysis of rolls
- Custom dice types (d3, d100)

  "mcp_type": "dice_event",
  "action": "roll_dice",
  "rollId": "player_damage_roll_123",
  "notation": "2d3 + 1d6",
  "reason": "Custom damage roll"
}
     
output:
    mcp_type : string
    rollId : <unique identifier for role> 
    individualRolls : [
        type: <dice type> 
        role: <value>
    ]
    total: 7
    rolledAt: <date>

{
  "mcp_type": "dice_result",
  "rollId": "player_damage_roll_123",
  "individualRolls": [
    { "type": "d3", "roll": 2 },
    { "type": "d3", "roll": 1 },
    { "type": "d6", "roll": 4 }
  ],
  "total": 7,
  "rolledAt": "2023-10-27T10:30:00Z"
}

### Seed Dice

name: Seed Dice
description:  This will configure the seed of the randomisation function used to throw the dice.
inputs:
    Seed
output:
    Seed

### Testing the Server

You can test the server using the MCP Inspector tool, which provides a user-friendly interface to interact with MCP servers.

#### Running with MCP Inspector

To test the server, run the following command in your terminal:

```bash
npx @modelcontextprotocol/inspector python src/servers/DnD_dice/server.py
```

This will start the server and open the MCP Inspector in your web browser.

#### Example Usage

1.  In the MCP Inspector, you will see the `Throw Dice` tool listed.
2.  Select the `Throw Dice` tool.
3.  In the `arguments` panel, enter a JSON object with the dice notation you want to roll. For example:

```json
{
  "mcp_type": "dice_event",
  "action": "roll_dice",
  "rollId": "test_roll_001",
  "notation": "2d6 + 1d4",
  "reason": "Testing the dice server"
}
```

4.  Click "Call" to execute the tool. The server will respond with the dice roll results in the `response` panel.


### Notes:

#### d4 (4-sided die)

Shape: Usually a tetrahedron (pyramid). Sometimes designed as a "bar" or "caltrop" shape to avoid rolling under furniture.

Common Uses:

Damage for very small weapons (e.g., dagger, dart, sling stone).

Minor magical effects or healing.

Determining random directions or small quantities.

#### d6 (6-sided die)

Shape: The familiar cube, like standard board game dice.

Common Uses:

Damage for many common weapons (e.g., shortsword, light crossbow).

Damage for many spells (e.g., Fireball often uses multiple d6s).

Rolling for character ability scores (e.g., 4d6 drop the lowest).

Many random tables (e.g., rolling a specific encounter).

Hit Dice for some classes (e.g., Wizard).

#### d8 (8-sided die)

Shape: An octahedron (two square pyramids joined at their bases).

Common Uses:

Damage for medium-sized weapons (e.g., longsword, rapier, shortbow).

Damage for some spells.

Hit Dice for many classes (e.g., Rogue, Cleric, Monk).

#### d10 (10-sided die)

Shape: A pentagonal trapezohedron.

Common Uses:

Damage for larger weapons (e.g., battleaxe, heavy crossbow).

Damage for some powerful spells.

Hit Dice for some robust classes (e.g., Fighter, Paladin, Ranger).

Percentage Rolls (d% or d100): You roll two d10s to get a number between 1 and 100. One d10 represents the tens digit (usually marked 00, 10, 20... 90), and the other represents the units digit (0, 1, 2... 9). A roll of 00 and 0 usually means 100, while 0 and 0 means 0 (or 10 if you prefer to count from 1-10 instead of 0-9).

#### d12 (12-sided die)

Shape: A dodecahedron.

Common Uses:

Damage for very large, powerful weapons (e.g., greataxe).

Damage for some potent monster attacks or spells.

Hit Dice for the most resilient classes (e.g., Barbarian).

#### d20 (20-sided die)

Shape: An icosahedron.

The Most Important Die: This is the primary die for almost all checks in D&D.

Common Uses:

Attack Rolls: d20 + modifiers vs. Armor Class (AC).

Ability Checks: d20 + modifiers vs. a Difficulty Class (DC). (e.g., Strength (Athletics) check, Dexterity (Stealth) check, Wisdom (Perception) check).

Saving Throws: d20 + modifiers vs. a spell's or effect's DC.

Initiative: d20 + Dexterity modifier to determine turn order in combat.

Any time the Dungeon Master asks you to "roll a d20."

Other "Dice" Concepts:
d% or d100: As mentioned, this is typically two d10s (one for tens, one for units) to generate a number from 1 to 100.

Arbitrary "dX": While the standard set has specific sided dice, you might occasionally see references to "d3" (often rolled as a d6 divided by 2, rounding up, or a d6 where 1-2=1, 3-4=2, 5-6=3) or even rarer dice in homebrew or specialized modules.

Roll Notation: Dice rolls are generally expressed as [Number of Dice]d[Sides] + [Modifier].

3d6+2: Roll three 6-sided dice, sum their results, and add 2.

1d20+5: Roll one 20-sided die, and add 5.

2d8: Roll two 8-sided dice and sum their results.d4 (4-sided die)

Shape: Usually a tetrahedron (pyramid). Sometimes designed as a "bar" or "caltrop" shape to avoid rolling under furniture.

Common Uses:

Damage for very small weapons (e.g., dagger, dart, sling stone).

Minor magical effects or healing.

Determining random directions or small quantities.

d6 (6-sided die)

Shape: The familiar cube, like standard board game dice.

Common Uses:

Damage for many common weapons (e.g., shortsword, light crossbow).

Damage for many spells (e.g., Fireball often uses multiple d6s).

Rolling for character ability scores (e.g., 4d6 drop the lowest).

Many random tables (e.g., rolling a specific encounter).

Hit Dice for some classes (e.g., Wizard).

d8 (8-sided die)

Shape: An octahedron (two square pyramids joined at their bases).

Common Uses:

Damage for medium-sized weapons (e.g., longsword, rapier, shortbow).

Damage for some spells.

Hit Dice for many classes (e.g., Rogue, Cleric, Monk).

d10 (10-sided die)

Shape: A pentagonal trapezohedron.

Common Uses:

Damage for larger weapons (e.g., battleaxe, heavy crossbow).

Damage for some powerful spells.

Hit Dice for some robust classes (e.g., Fighter, Paladin, Ranger).

Percentage Rolls (d% or d100): You roll two d10s to get a number between 1 and 100. One d10 represents the tens digit (usually marked 00, 10, 20... 90), and the other represents the units digit (0, 1, 2... 9). A roll of 00 and 0 usually means 100, while 0 and 0 means 0 (or 10 if you prefer to count from 1-10 instead of 0-9).

d12 (12-sided die)

Shape: A dodecahedron.

Common Uses:

Damage for very large, powerful weapons (e.g., greataxe).

Damage for some potent monster attacks or spells.

Hit Dice for the most resilient classes (e.g., Barbarian).

d20 (20-sided die)

Shape: An icosahedron.

The Most Important Die: This is the primary die for almost all checks in D&D.

Common Uses:

Attack Rolls: d20 + modifiers vs. Armor Class (AC).

Ability Checks: d20 + modifiers vs. a Difficulty Class (DC). (e.g., Strength (Athletics) check, Dexterity (Stealth) check, Wisdom (Perception) check).

Saving Throws: d20 + modifiers vs. a spell's or effect's DC.

Initiative: d20 + Dexterity modifier to determine turn order in combat.

Any time the Dungeon Master asks you to "roll a d20."

Other "Dice" Concepts:
d% or d100: As mentioned, this is typically two d10s (one for tens, one for units) to generate a number from 1 to 100.

Arbitrary "dX": While the standard set has specific sided dice, you might occasionally see references to "d3" (often rolled as a d6 divided by 2, rounding up, or a d6 where 1-2=1, 3-4=2, 5-6=3) or even rarer dice in homebrew or specialized modules.

Roll Notation: Dice rolls are generally expressed as [Number of Dice]d[Sides] + [Modifier].

3d6+2: Roll three 6-sided dice, sum their results, and add 2.

1d20+5: Roll one 20-sided die, and add 5.

2d8: Roll two 8-sided dice and sum their results.
