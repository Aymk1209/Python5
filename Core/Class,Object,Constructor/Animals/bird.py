from .animal import Animal


class Bird(Animal):
    def speak(self):
        return f"{self.name} chirps."

    def move(self):
        return f"{self.name} flies in the sky."