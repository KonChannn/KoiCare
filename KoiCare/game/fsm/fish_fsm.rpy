# FishFSM - Handles fish state transitions and health effects

init python:
    class FishFSM:
        def __init__(self):
            self.states = {
                "healthy": {
                    "threshold": 70,
                    "description": "Ikan dalam kondisi sangat sehat!",
                    "effects": {
                        "health_decay": -1,
                        "happiness": 1
                    }
                },
                "normal": {
                    "threshold": 40,
                    "description": "Ikan dalam kondisi baik.",
                    "effects": {
                        "health_decay": -2,
                        "happiness": 0
                    }
                },
                "sick": {
                    "threshold": 0,
                    "description": "Ikan terlihat tidak sehat!",
                    "effects": {
                        "health_decay": -5,
                        "happiness": -2
                    }
                }
            }
            self.current_state = "healthy"
            self.health = 100
            self.happiness = 50

        def update_state(self):
            if self.health >= self.states["healthy"]["threshold"]:
                self.current_state = "healthy"
            elif self.health >= self.states["normal"]["threshold"]:
                self.current_state = "normal"
            else:
                self.current_state = "sick"

        def apply_effects(self):
            effects = self.states[self.current_state]["effects"]
            self.health = max(0, self.health + effects["health_decay"])
            self.happiness = max(0, min(100, self.happiness + effects["happiness"]))
            self.update_state()

        def feed(self):
            self.health = min(100, self.health + 20)
            self.happiness = min(100, self.happiness + 10)
            self.update_state()

        def get_state_description(self):
            return self.states[self.current_state]["description"]

        def get_state(self):
            return self.current_state

        def is_alive(self):
            return self.health > 0 