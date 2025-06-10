# TimeFSM - Handles time state transitions and time-based events

init python:
    class TimeFSM:
        def __init__(self):
            self.states = {
                "morning": {
                    "next": "afternoon",
                    "duration": 20,
                    "description": "The sun rises, bringing a new day.",
                    "effects": {
                        "fish_health": -5,  # Fish gets hungry overnight
                        "water_quality": 0
                    }
                },
                "afternoon": {
                    "next": "evening",
                    "duration": 20,
                    "description": "The sun is high in the sky.",
                    "effects": {
                        "fish_health": 0,
                        "water_quality": -10  # Water gets dirty during day
                    }
                },
                "evening": {
                    "next": "night",
                    "duration": 20,
                    "description": "The sun begins to set.",
                    "effects": {
                        "fish_health": -3,  # Fish gets tired
                        "water_quality": -5
                    }
                },
                "night": {
                    "next": "morning",
                    "duration": 20,
                    "description": "The moon rises, bringing darkness.",
                    "effects": {
                        "fish_health": -2,
                        "water_quality": -5  # Water quality decreases at night
                    }
                }
            }
            self.current_state = "morning"
            self.time_remaining = self.states["morning"]["duration"]
            self.day_number = 1

        def advance_time(self):
            current = self.states[self.current_state]
            self.current_state = current["next"]
            self.time_remaining = self.states[self.current_state]["duration"]
            
            if self.current_state == "morning":
                self.day_number += 1
                return True  # Signal that a new day has started
            return False

        def get_current_state_info(self):
            return self.states[self.current_state]

        def get_time_remaining(self):
            return self.time_remaining

        def decrement_time(self):
            self.time_remaining -= 1
            return self.time_remaining <= 0

        def apply_time_effects(self, fish, pond):
            effects = self.states[self.current_state]["effects"]
            fish.health = max(0, fish.health + effects["fish_health"])
            pond.water_quality = max(0, pond.water_quality + effects["water_quality"]) 