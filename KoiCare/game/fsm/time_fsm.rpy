# TimeFSM - Handles time state transitions and time-based events

init python:
    class TimeFSM:
        def __init__(self):
            self.states = {
                "pagi": {
                    "next": "siang",
                    "duration": 5,
                    "description": "Matahari terbit, membawa hari yang baru.",
                    "effects": {
                        "fish_health": -5,  # Fish gets hungry overnight
                        "water_quality": 0
                    }
                },
                "siang": {
                    "next": "sore",
                    "duration": 5,
                    "description": "Matahari sudah tinggi di langit.",
                    "effects": {
                        "fish_health": 0,
                        "water_quality": -10  # Water gets dirty during day
                    }
                },
                "sore": {
                    "next": "malam",
                    "duration": 3,
                    "description": "Matahari mulai terbenam.",
                    "effects": {
                        "fish_health": -3,  # Fish gets tired
                        "water_quality": -5
                    }
                },
                "malam": {
                    "next": "pagi",
                    "duration": 2,
                    "description": "Bulan terbit, membawa kegelapan.",
                    "effects": {
                        "fish_health": -2,
                        "water_quality": -5  # Water quality decreases at night
                    }
                }
            }
            self.current_state = "pagi"
            self.time_remaining = self.states["pagi"]["duration"]
            self.day_number = 1

        def advance_time(self):
            current = self.states[self.current_state]
            self.current_state = current["next"]
            self.time_remaining = self.states[self.current_state]["duration"]
            
            if self.current_state == "pagi":
                self.day_number += 1
                return True  # Signal that a new day has started
            return False

        def get_current_state_info(self):
            return self.states[self.current_state]

        def get_time_remaining(self):
            return self.time_remaining

        def decrement_time(self):
            if self.time_remaining > 0:
                self.time_remaining -= 1
                return self.time_remaining <= 0

        def apply_time_effects(self, fish, pond):
            effects = self.states[self.current_state]["effects"]
            fish.health = max(0, fish.health + effects["fish_health"])
            pond.water_quality = max(0, pond.water_quality + effects["water_quality"]) 