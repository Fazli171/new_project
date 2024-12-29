from abc import ABC, abstractmethod

# Abstract base class for devices
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Concrete class for TV
class TV(Device):
    def turn_on(self):
        print("The TV is turned on!")

    def turn_off(self):
        print("The TV is turned off!")

# Concrete class for Radio
class Radio(Device):
    def turn_on(self):
        print("The radio is turned on!")

    def turn_off(self):
        print("The radio is turned off!")

# Creating objects
tv = TV()
tv.turn_on()  # "The TV is turned on!"
tv.turn_off()  # "The TV is turned off!"

radio = Radio()
radio.turn_on()  # "The radio is turned on!"
radio.turn_off()  # "The radio is turned off!"

# Abstract base class for transport
class TransportType(ABC):
    def __init__(self, transport_type):
        self.transport_type = transport_type

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class for cars
class Car(TransportType):
    def __init__(self, transport_type):
        super().__init__(transport_type)

    def start(self):
        print(f"The {self.transport_type} car has started moving.")

    def stop(self):
        print(f"The {self.transport_type} car has stopped.")

# Concrete class for airplanes
class Airplane(TransportType):
    def __init__(self, transport_type):
        super().__init__(transport_type)

    def start(self):
        print(f"The {self.transport_type} airplane has taken off.")

    def stop(self):
        print(f"The {self.transport_type} airplane has landed.")

car = Car('Nexia')
car.start()
car.stop()

plane = Airplane('Boeing')
plane.start()
plane.stop()

# Abstract base class for mathematical operations
class Operation(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def subtract(self, a, b):
        pass

# Concrete class for operations
class Calculator(Operation):
    def __init__(self):
        super().__init__()

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.subtract(12, 4))
print(calc.add(34, 90))

# Abstract base class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class for rectangles
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Concrete class for circles
class Circle(Shape):
    def __init__(self, radius, pi=3.14):
        super().__init__()
        self.radius = radius
        self.pi = pi

    def perimeter(self):
        return 2 * self.pi * self.radius

    def area(self):
        return (self.radius ** 2) * self.pi

rect = Rectangle(12, 10)
print(rect.area())
print(rect.perimeter())

circle = Circle(3)
print(circle.area())
print(circle.perimeter())

# Abstract base class for transport
class Transport(ABC):
    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

# Concrete class for cars
class Car(Transport):
    def __init__(self, fuel_type, max_speed=120):
        super().__init__()
        self.max_speed_value = max_speed
        self.fuel_type_value = fuel_type

    def max_speed(self):
        return f"Max speed: {self.max_speed_value}"

    def fuel_type(self):
        return f"Fuel type: {self.fuel_type_value}"

# Concrete class for bicycles
class Bicycle(Transport):
    def __init__(self, fuel_type, max_speed=25):
        super().__init__()
        self.max_speed_value = max_speed
        self.fuel_type_value = fuel_type

    def max_speed(self):
        return f"Max speed: {self.max_speed_value}"

    def fuel_type(self):
        return f"Fuel type: {self.fuel_type_value}"

car = Car('Gasoline', 200)
print(car.max_speed())
print(car.fuel_type())

bicycle = Bicycle('Human power', 27)
print(bicycle.max_speed())
# print(bicycle.fuel_type())

# Abstract base class for transport
class Transport(ABC):
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete class for cars
class Car(Transport):
    def __init__(self, name, year, seats, fuel_type, max_speed=180):
        super().__init__(name, year)
        self.max_speed_value = max_speed
        self.fuel_type_value = fuel_type
        self.seats = seats

    def max_speed(self):
        return f"The car's max speed is {self.max_speed_value}."

    def fuel_type(self):
        return f"The car's fuel type is {self.fuel_type_value}."

    def description(self):
        return f"The car's name is {self.name}, manufactured in {self.year}, with a max speed of {self.max_speed_value}, and runs on {self.fuel_type_value}."

# Concrete class for bicycles
class Bicycle(Transport):
    def __init__(self, name, year, seats, movement_type, max_speed=25):
        super().__init__(name, year)
        self.max_speed_value = max_speed
        self.seats = seats
        self.movement_type = movement_type

    def fuel_type(self):
        return f"Bicycles do not use fuel; they are powered by human effort."

    def max_speed(self):
        return f"The bicycle's max speed is {self.max_speed_value}."

    def description(self):
        return f"The bicycle's name is {self.name}, manufactured in {self.year}, with a max speed of {self.max_speed_value}, and powered by {self.movement_type}."

# Concrete class for airplanes
class Airplane(Transport):
    def __init__(self, name, year, seats, fuel_type, max_speed):
        super().__init__(name, year)
        self.max_speed_value = max_speed
        self.fuel_type_value = fuel_type
        self.seats = seats

    def max_speed(self):
        return f"The airplane's max speed is {self.max_speed_value}."

    def fuel_type(self):
        return f"The airplane's fuel type is {self.fuel_type_value}."

    def description(self):
        return f"The airplane's name is {self.name}, manufactured in {self.year}, with a max speed of {self.max_speed_value}, and runs on {self.fuel_type_value}."

car = Car('Nexia', 2014, 5, 'Gasoline', 200)
print(car.max_speed())
print(car.description())
print(car.fuel_type())

bicycle = Bicycle('Binvi', 2020, 1, 'Human power')
print(bicycle.description())
print(bicycle.max_speed())
print(bicycle.fuel_type())

airplane = Airplane('Airways', 2022, 300, 'Diesel', 500)
print(airplane.max_speed())
print(airplane.description())
print(airplane.fuel_type())
