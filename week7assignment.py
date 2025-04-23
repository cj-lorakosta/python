Question 1

# Base class
class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity
        self.__serial_number = None  # Private attribute for serial number

    def set_serial_number(self, serial_number):
        self.__serial_number = serial_number

    def get_serial_number(self):
        return self.__serial_number

    def display_info(self):
        print(f"{self.brand} {self.model} with {self.battery_capacity}mAh battery")

    def make_call(self, number):
        print(f"Calling {number}...")

# Subclass with inheritance
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_capacity, camera_resolution):
        super().__init__(brand, model, battery_capacity)
        self.camera_resolution = camera_resolution

    def take_picture(self):
        print(f"Taking a {self.camera_resolution}MP photo!")

    def display_info(self):  # Polymorphism: overrides parent method
        print(f"{self.brand} {self.model} - Camera: {self.camera_resolution}MP, Battery: {self.battery_capacity}mAh")

# Create instances
phone1 = Smartphone("Samsung", "Galaxy S21", 4000)
phone1.set_serial_number("SN1234567890")
phone1.display_info()
phone1.make_call("555-1234")
print(phone1.get_serial_number())

print("-----------")

phone2 = SmartphoneWithCamera("Apple", "iPhone 13", 3300, 12)
phone2.set_serial_number("SN0987654321")
phone2.display_info()
phone2.make_call("555-5678")
phone2.take_picture()
print(phone2.get_serial_number())

Question 2

# Base class for transport
class Transport:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Vehicle class
class Car(Transport):
    def move(self):
        print("Driving 🚗")

class Plane(Transport):
    def move(self):
        print("Flying ✈️")

# Animal class
class Dog(Transport):
    def move(self):
        print("Running 🐕")

class Fish(Transport):
    def move(self):
        print("Swimming 🐟")

# Create instances and call move()
car = Car()
car.move()  # Output: Driving 🚗

plane = Plane()
plane.move()  # Output: Flying ✈️

dog = Dog()
dog.move()  # Output: Running 🐕

fish = Fish()
fish.move()  # Output: Swimming 🐟


