from .animal import Animal


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

    def move(self):
        return f"{self.name} runs on four legs."