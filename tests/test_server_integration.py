"""
Integration tests for the DnD Dice MCP Server.
"""

import pytest
import sys
import os

# Add project root to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.servers.DnD_dice.server import handle_call_tool


@pytest.mark.asyncio
async def test_handle_call_tool_simple_roll():
    """Test the handle_call_tool function with a simple dice roll."""
    arguments = {
        "mcp_type": "test",
        "action": "roll",
        "rollId": "test-123",
        "notation": "2d6",
    }
    
    contents, result = await handle_call_tool("Throw Dice", arguments)
    
    # Check the result structure
    assert "rollId" in result
    assert result["rollId"] == "test-123"
    assert "notation" in result
    assert result["notation"] == "2d6"
    assert "result" in result
    assert "rolledAt" in result
    
    # Check the result is valid for 2d6 (minimum 2, maximum 12)
    result_value = int(result["result"])
    assert 2 <= result_value <= 12
    
    # Check contents
    assert len(contents) == 1
    assert contents[0]["type"] == "text"
    assert "2d6" in contents[0]["text"]
    assert result["result"] in contents[0]["text"]


@pytest.mark.asyncio
async def test_handle_call_tool_with_modifier():
    """Test the handle_call_tool function with dice roll and modifier."""
    arguments = {
        "mcp_type": "test",
        "action": "roll",
        "rollId": "test-456",
        "notation": "1d20+5",
    }
    
    contents, result = await handle_call_tool("Throw Dice", arguments)
    
    # Check the result structure
    assert result["rollId"] == "test-456"
    assert result["notation"] == "1d20+5"
    
    # Check the result is valid for 1d20+5 (minimum 6, maximum 25)
    result_value = int(result["result"])
    assert 6 <= result_value <= 25
    
    # Check details are included in the message
    assert "Details:" in contents[0]["text"]


@pytest.mark.asyncio
async def test_handle_call_tool_multiple_dice_groups():
    """Test the handle_call_tool function with multiple dice groups."""
    arguments = {
        "mcp_type": "test",
        "action": "roll",
        "rollId": "test-789",
        "notation": "2d3 + 1d6",
    }
    
    contents, result = await handle_call_tool("Throw Dice", arguments)
    
    # Check the result structure
    assert result["rollId"] == "test-789"
    assert result["notation"] == "2d3 + 1d6"
    
    # Check the result is valid for 2d3 + 1d6 (minimum 3, maximum 12)
    result_value = int(result["result"])
    assert 3 <= result_value <= 12


@pytest.mark.asyncio
async def test_handle_call_tool_missing_notation():
    """Test that missing notation raises ValueError."""
    arguments = {
        "mcp_type": "test",
        "action": "roll",
        "rollId": "test-error",
    }
    
    with pytest.raises(ValueError, match="Missing required argument: notation"):
        await handle_call_tool("Throw Dice", arguments)


@pytest.mark.asyncio
async def test_handle_call_tool_invalid_notation():
    """Test that invalid notation raises ValueError."""
    arguments = {
        "mcp_type": "test",
        "action": "roll",
        "rollId": "test-invalid",
        "notation": "invalid",
    }
    
    with pytest.raises(ValueError, match="Invalid dice notation"):
        await handle_call_tool("Throw Dice", arguments)


@pytest.mark.asyncio
async def test_handle_call_tool_unknown_tool():
    """Test that unknown tool raises ValueError."""
    arguments = {
        "mcp_type": "test",
        "action": "roll",
        "rollId": "test-unknown",
        "notation": "1d20",
    }
    
    with pytest.raises(ValueError, match="Unknown tool"):
        await handle_call_tool("Unknown Tool", arguments)
