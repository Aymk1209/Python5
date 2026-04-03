class Walkable:
    def __init__(self, leg_count):
        self.leg_count = leg_count

    def walk(self):
        return f"Walking on {self.leg_count} legs"

    def get_info(self):
        return f"Has {self.leg_count} legs"