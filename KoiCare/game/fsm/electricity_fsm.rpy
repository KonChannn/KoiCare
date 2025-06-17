init python:
    class ElectricityFSM:
        def __init__(self, max_electricity=100, drain_per_turn=5):
            self.max = max_electricity
            self.drain = drain_per_turn
            self.amount = max_electricity

        def apply_effects(self):
            self.amount = max(0, self.amount - self.drain)

        def recharge(self, amount):
            self.amount = min(self.max, self.amount + amount)

        def decreaseCharge(self, drain):
            self.amount = max(0, self.amount - drain)
        