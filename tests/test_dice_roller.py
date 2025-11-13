"""
Tests for the dice roller module.
"""

import pytest
from src.servers.DnD_dice.dice_roller import (
    parse_dice_notation,
    roll_dice,
    roll_dice_notation,
)


class TestParseDiceNotation:
    """Tests for parse_dice_notation function."""
    
    def test_simple_dice(self):
        """Test parsing simple dice notation."""
        result = parse_dice_notation("2d6")
        assert result == [(2, 6, 0)]
    
    def test_single_die(self):
        """Test parsing single die notation."""
        result = parse_dice_notation("1d20")
        assert result == [(1, 20, 0)]
    
    def test_dice_with_positive_modifier(self):
        """Test parsing dice with positive modifier."""
        result = parse_dice_notation("1d20+5")
        assert result == [(1, 20, 5)]
    
    def test_dice_with_negative_modifier(self):
        """Test parsing dice with negative modifier."""
        result = parse_dice_notation("2d6-1")
        assert result == [(2, 6, -1)]
    
    def test_multiple_dice_groups(self):
        """Test parsing multiple dice groups."""
        result = parse_dice_notation("2d3+1d6")
        assert result == [(2, 3, 0), (1, 6, 0)]
    
    def test_multiple_dice_groups_with_spaces(self):
        """Test parsing multiple dice groups with spaces."""
        result = parse_dice_notation("2d3 + 1d6")
        assert result == [(2, 3, 0), (1, 6, 0)]
    
    def test_complex_notation(self):
        """Test parsing complex notation with multiple groups and modifier."""
        result = parse_dice_notation("2d8+1d6+3")
        assert result == [(2, 8, 0), (1, 6, 3)]
    
    def test_empty_notation(self):
        """Test that empty notation raises ValueError."""
        with pytest.raises(ValueError, match="Empty dice notation"):
            parse_dice_notation("")
    
    def test_invalid_notation(self):
        """Test that invalid notation raises ValueError."""
        with pytest.raises(ValueError):
            parse_dice_notation("invalid")
    
    def test_zero_dice(self):
        """Test that zero dice raises ValueError."""
        with pytest.raises(ValueError, match="Number of dice must be at least 1"):
            parse_dice_notation("0d6")
    
    def test_zero_sides(self):
        """Test that zero sides raises ValueError."""
        with pytest.raises(ValueError, match="Number of sides must be at least 1"):
            parse_dice_notation("2d0")


class TestRollDice:
    """Tests for roll_dice function."""
    
    def test_roll_single_die(self):
        """Test rolling a single die."""
        for _ in range(10):  # Test multiple times for randomness
            result = roll_dice(1, 6)
            assert len(result) == 1
            assert 1 <= result[0] <= 6
    
    def test_roll_multiple_dice(self):
        """Test rolling multiple dice."""
        for _ in range(10):  # Test multiple times for randomness
            result = roll_dice(3, 8)
            assert len(result) == 3
            for roll in result:
                assert 1 <= roll <= 8
    
    def test_roll_d20(self):
        """Test rolling a d20."""
        for _ in range(10):  # Test multiple times for randomness
            result = roll_dice(1, 20)
            assert len(result) == 1
            assert 1 <= result[0] <= 20


class TestRollDiceNotation:
    """Tests for roll_dice_notation function."""
    
    def test_simple_roll(self):
        """Test simple dice roll."""
        total, details = roll_dice_notation("2d6")
        assert 2 <= total <= 12  # Minimum 2 (1+1), maximum 12 (6+6)
        assert "2d6:" in details
    
    def test_single_die_roll(self):
        """Test single die roll."""
        total, details = roll_dice_notation("1d20")
        assert 1 <= total <= 20
        assert "1d20:" in details
    
    def test_roll_with_positive_modifier(self):
        """Test dice roll with positive modifier."""
        total, details = roll_dice_notation("1d20+5")
        assert 6 <= total <= 25  # Minimum 1+5, maximum 20+5
        assert "1d20:" in details
        assert "modifier: +5" in details
    
    def test_roll_with_negative_modifier(self):
        """Test dice roll with negative modifier."""
        total, details = roll_dice_notation("2d6-1")
        assert 1 <= total <= 11  # Minimum 2-1, maximum 12-1
        assert "2d6:" in details
        assert "modifier: -1" in details
    
    def test_multiple_dice_groups(self):
        """Test rolling multiple dice groups."""
        total, details = roll_dice_notation("2d3 + 1d6")
        assert 3 <= total <= 12  # Minimum 2+1, maximum 6+6
        assert "2d3:" in details
        assert "1d6:" in details
    
    def test_invalid_notation_raises_error(self):
        """Test that invalid notation raises ValueError."""
        with pytest.raises(ValueError):
            roll_dice_notation("invalid")
    
    def test_deterministic_behavior(self):
        """Test that multiple rolls produce valid results."""
        for _ in range(20):
            total, details = roll_dice_notation("1d6")
            assert 1 <= total <= 6
            assert "1d6:" in details
