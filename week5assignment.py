# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
        self.__secret_identity = None  # Encapsulated attribute

    def set_secret_identity(self, identity):
        self.__secret_identity = identity

    def get_secret_identity(self):
        return f"Secret identity of {self.name} is {self.__secret_identity}"

    def display_info(self):
        print(f"{self.name} protects {self.city} with the power of {self.power}!")

# Subclass with inheritance and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def display_info(self):  # Polymorphism: overrides parent method
        print(f"{self.name} soars above {self.city} at {self.flight_speed} km/h using {self.power}!")

# Create instances
hero1 = Superhero("ShadowStrike", "Invisibility", "Night City")
hero1.set_secret_identity("Liam Cole")
hero1.display_info()
print(hero1.get_secret_identity())

print("-----------")

hero2 = FlyingHero("SkyFlare", "Fire Flight", "Skyhaven", 800)
hero2.set_secret_identity("Ava Blaze")
hero2.display_info()
print(hero2.get_secret_identity())
