# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power         # Encapsulated attribute
        self.origin = origin

    def display_info(self):
        print(f"Name: {self.name}, Power: {self._power}, Origin: {self.origin}")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

# Subclass
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} takes off at {self.flight_speed} km/h, using {self._power}!")

# Creating objects
hero1 = Superhero("ShadowFist", "Invisibility", "Earth")
hero2 = FlyingSuperhero("SkyBlade", "Wind Blast", "Mars", 800)

hero1.display_info()
hero1.use_power()

hero2.display_info()
hero2.use_power()
