# EX1: INHERITANCE

# a. Define a class named Person.
# This class will have the following attributes (in the constructor):
# - name
# - age
# Implement the method describe(), which will display the message:
# 'Person {name} is {age} years old.'

# b. Define the Employee class, which inherits from the Person class.
# This class will take two additional parameters in the constructor:
# salary and position.
# Define the method display_salary(), which returns the salary attribute.

# c. Create an object of type Person.
# Access and display its properties.
# Call the describe method.

# d. Create an object of type Employee.
# Access and display its properties.
# Call the available methods on it.

# e. Extend the describe method from the Employee class,
# so that it also displays a sentence containing the salary and position attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Person {self.name} is {self.age} years old")

class Employee(Person):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age)
        self.salary = salary
        self.position = position

    def display_salary(self):
        return self.salary

    def describe(self):
        super().describe()
        print(f"Position: {self.position}, Salary: {self.salary}")


person1 = Person("Serin", 23)
print("Name:", person1.name)
print("Age:", person1.age)
person1.describe()

employee1 = Employee("serin", 23, 1500, "qa tester")
print("Name:", employee1.name)
print("Age:", employee1.age)
print("Position:", employee1.position)
print("Salary:", employee1.salary)

employee1.describe()
print("Employee Salary:", employee1.display_salary())

print("--------" * 4)

# EX2: POLYMORPHISM

# a. Define a class Bird that implements the method fly.
# In the fly method, display the message 'Most birds can fly.'

# b. Define a class Ostrich, which inherits from the Bird class.
# Define the fly method, and display the message 'Ostriches cannot fly.'
# (We do not extend the method from the base class, we override it -> OVERRIDING)

# c. Define the Duck class, which inherits from the Bird class.
# Define the fly method, and display the message 'Ducks can fly.'

# d. Instantiate all three classes and call the fly method on each object.
# POLYMORPHISM => same method name, different behavior.

class Bird:
    def fly(self):
        print("Most birds can fly.")
class Ostrich(Bird):
    def fly(self):
        print("Ostriches cannot fly.")
class Duck(Bird):
    def fly(self):
        print("Ducks can fly.")
bird = Bird()
ostrich = Ostrich()
duck = Duck()
bird.fly()
ostrich.fly()
duck.fly()

print("--------" * 4)
# EX3: ABSTRACTION

# a. Define an interface Car. It will have an abstract method called car_model.

# b. Define the classes Tesla and BMW, which implement the Car interface.
# The car_model method should display a message related to the car model.
# Instantiate the Tesla and BMW classes and invoke the car_model method on each.

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def car_model(self):
        pass

class Tesla(Car):
    def car_model(self):
        print("This is a Tesla Model S.")

class BMW(Car):
    def car_model(self):
        print("This is a BMW X5.")

tesla_car = Tesla()
bmw_car = BMW()

tesla_car.car_model()
bmw_car.car_model()

# EX4: ENCAPSULATION

# a. Define a class Product.
# It will have the following attributes in the constructor:
# - name
# - price
# - discount - private attribute

# b. Define the discount property:
# - getter
# - setter -> before setting a value for discount, ensure it is between 0-100.
# - deleter

print("--------" * 4)
class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.__discount = discount

    @property
    def discount(self):
        return self.__discount


    @discount.setter
    def discount(self,value):
        if 0 <= value <= 100:
            self.__discount = value
            print(f"Discount set to {value}%.")
        else:
            print("Error: Discount must be between 0 and 100.")

    @discount.deleter
    def discount(self):
        print("Discount deleted.")
        self.__discount = 0
product = Product("Laptop", 1500, 10)
print("Current discount:", product.discount)
product.discount = 20
print("New discount:", product.discount)
product.discount = 120
del product.discount
print("Discount after deletion:", product.discount)


# EX5: Define an abstract class AbstractVideo.
# It will have an abstract method show_details.
# Additionally, it will have a method play, which will display the message 'Video is playing.'


