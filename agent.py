# agent.py
import random


class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        # If standing directly on food, or just wander / move towards coordinates
        pos = percept['agent_pos']
        # Simple heuristic or fallback random sweep
        return random.choice(self.actions_pool)

class SimpleReflexAgent:
    """
    A simple reflex agent that makes decisions only
    based on the current percept.
    """

    def sense_and_act(self, percept: dict) -> str:

        # Rule 1: If food is here, collect it
        if percept["food_here"]:
            return "Stay"

        # Rule 2: If wall is ahead, turn left
        elif percept["wall_ahead"]:
            return "Left"

        # Rule 3: Otherwise move forward
        else:
            return "Right"

class ModelBasedAgent:
    """
    Model-Based Agent

    Maintains internal memory.
    Remembers visited cells and previous actions.
    """

    def __init__(self):

        # Internal memory state
        self.visited_cells = set()

        # Remember previous action
        self.last_action = None

        # Used for changing direction
        self.turn_actions = [
            "Up",
            "Left",
            "Down",
            "Right"
        ]

        self.turn_index = 0

    def sense_and_act(self, percept: dict) -> str:

        # Get current position from percept
        current_pos = percept["agent_pos"]

        # Check whether this cell was visited before
        already_visited = current_pos in self.visited_cells

        # Update memory
        self.visited_cells.add(current_pos)

        # Rule 1:
        # IF food_here THEN collect
        if percept["food_here"]:

            action = "Stay"

        # Rule 2:
        # IF wall ahead THEN change direction
        elif percept["wall_ahead"]:

            self.turn_index = (
                self.turn_index + 1
            ) % len(self.turn_actions)

            action = self.turn_actions[self.turn_index]

        # Rule 3:
        # IF already visited cell -> avoid loop
        elif already_visited:
            self.turn_index = (
                self.turn_index + 1
            ) % len(self.turn_actions)

            action = self.turn_actions[self.turn_index]

        # Rule 4:
        # Normal movement
        else:
            action = "Right"

        # Save last action
        self.last_action = action

        return action