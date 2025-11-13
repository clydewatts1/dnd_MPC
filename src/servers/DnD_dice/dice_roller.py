"""
Dice rolling logic for D&D dice notation.
Supports standard dice notation like: 1d20, 2d6+3, 3d8-1, 2d3 + 1d6
"""

import re
import random
from typing import List, Tuple


def parse_dice_notation(notation: str) -> List[Tuple[int, int, int]]:
    """
    Parse dice notation and return a list of (num_dice, num_sides, modifier) tuples.
    
    Args:
        notation: Dice notation string (e.g., '2d6+3', '1d20', '2d3 + 1d6')
    
    Returns:
        List of tuples: (number_of_dice, number_of_sides, modifier)
        The modifier is only added to the last die group.
    
    Raises:
        ValueError: If the notation is invalid
    """
    # Remove all whitespace for easier parsing
    notation = notation.replace(" ", "")
    
    if not notation:
        raise ValueError("Empty dice notation")
    
    # Pattern to match dice notation: XdY with optional +/- modifier at the end
    # Supports multiple dice groups separated by + or -
    # Examples: 2d6, 1d20+5, 2d3+1d6, 3d8-2
    
    # Split by + or - while keeping the operators
    parts = re.split(r'(?=[+-])', notation)
    
    dice_groups = []
    accumulated_modifier = 0
    
    for part in parts:
        if not part:
            continue
            
        # Check if this part starts with + or -
        sign = 1
        if part[0] == '+':
            part = part[1:]
        elif part[0] == '-':
            sign = -1
            part = part[1:]
        
        # Match XdY pattern
        dice_match = re.match(r'^(\d+)d(\d+)$', part)
        if dice_match:
            num_dice = int(dice_match.group(1))
            num_sides = int(dice_match.group(2))
            
            if num_dice < 1:
                raise ValueError(f"Number of dice must be at least 1, got {num_dice}")
            if num_sides < 1:
                raise ValueError(f"Number of sides must be at least 1, got {num_sides}")
            
            dice_groups.append((num_dice, num_sides, 0))
        else:
            # Try to match a plain number (modifier)
            try:
                modifier = int(part)
                accumulated_modifier += sign * modifier
            except ValueError:
                raise ValueError(f"Invalid dice notation part: {part}")
    
    if not dice_groups:
        raise ValueError(f"No valid dice notation found in: {notation}")
    
    # Add accumulated modifier to the last dice group
    if accumulated_modifier != 0:
        last_group = dice_groups[-1]
        dice_groups[-1] = (last_group[0], last_group[1], accumulated_modifier)
    
    return dice_groups


def roll_dice(num_dice: int, num_sides: int) -> List[int]:
    """
    Roll a number of dice with specified sides.
    
    Args:
        num_dice: Number of dice to roll
        num_sides: Number of sides on each die
    
    Returns:
        List of individual die results
    """
    return [random.randint(1, num_sides) for _ in range(num_dice)]


def roll_dice_notation(notation: str) -> Tuple[int, str]:
    """
    Roll dice based on the notation and return the total result and details.
    
    Args:
        notation: Dice notation string (e.g., '2d6+3', '1d20', '2d3 + 1d6')
    
    Returns:
        Tuple of (total_result, detailed_breakdown)
        Example: (15, "2d6: [4, 5] = 9, 1d6: [6] = 6")
    
    Raises:
        ValueError: If the notation is invalid
    """
    dice_groups = parse_dice_notation(notation)
    
    total = 0
    details = []
    
    for num_dice, num_sides, modifier in dice_groups:
        rolls = roll_dice(num_dice, num_sides)
        subtotal = sum(rolls)
        
        if modifier != 0:
            detail = f"{num_dice}d{num_sides}: {rolls} = {subtotal}, modifier: {modifier:+d}, subtotal: {subtotal + modifier}"
            subtotal += modifier
        else:
            detail = f"{num_dice}d{num_sides}: {rolls} = {subtotal}"
        
        details.append(detail)
        total += subtotal
    
    detailed_breakdown = ", ".join(details)
    
    return total, detailed_breakdown
