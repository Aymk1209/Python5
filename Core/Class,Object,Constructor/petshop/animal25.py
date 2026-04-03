class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return f"{self.name} makes a generic animal sound"

    def get_info(self):
        return f"{self.name} is a {self.species}"