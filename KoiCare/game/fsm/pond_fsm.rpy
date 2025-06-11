# PondFSM - Handles pond state transitions and water quality effects

init python:
    class PondFSM:
        def __init__(self):
            self.states = {
                "clean": {
                    "threshold": 70,
                    "description": "Air dalam kondisi sangat bersih!",
                    "effects": {
                        "quality_decay": -1,
                        "fish_health_effect": 1
                    }
                },
                "normal": {
                    "threshold": 40,
                    "description": "Air dalam kondisi baik.",
                    "effects": {
                        "quality_decay": -2,
                        "fish_health_effect": 0
                    }
                },
                "dirty": {
                    "threshold": 0,
                    "description": "Air kotor! Pompa perlu dinyalakan.",
                    "effects": {
                        "quality_decay": -5,
                        "fish_health_effect": -2
                    }
                }
            }
            self.current_state = "clean"
            self.water_quality = 100
            self.pump_on = True

        def update_state(self):
            if self.water_quality >= self.states["clean"]["threshold"]:
                self.current_state = "clean"
            elif self.water_quality >= self.states["normal"]["threshold"]:
                self.current_state = "normal"
            else:
                self.current_state = "dirty"

        def apply_effects(self):
            if not self.pump_on:
                effects = self.states[self.current_state]["effects"]
                self.water_quality = max(0, self.water_quality + effects["quality_decay"])
            else:
                self.water_quality = min(100, self.water_quality + 5)  # Pump improves water quality
            self.update_state()

        def toggle_pump(self):
            self.pump_on = not self.pump_on
            return self.pump_on

        def get_state(self):
            return self.current_state

        def get_state_description(self):
            return self.states[self.current_state]["description"]

        def get_fish_health_effect(self):
            return self.states[self.current_state]["effects"]["fish_health_effect"] 