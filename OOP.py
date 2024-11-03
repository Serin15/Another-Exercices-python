# a. Define a new class named Dog.

# b. Dog objects will have 2 mandatory attributes: name and age.

# c. Create two objects of type Dog, access their attributes, and display them.

# d. Change the name attribute for one of the objects and display it again.

# e. Create a method called description that returns the message '{name} is {age} years old'.

# f. Using one of the instantiated objects from the exercise, call the description method,
# save the result in a variable, and display the variable.

# g. The Dog class is also characterized by the attribute breed.
# Add this attribute as a class attribute (not an object attribute).

# h. Add a new method to the Dog class called speak, which takes a parameter called sound.
# The method should return the message "<name> says <sound>."

# i. Call the speak method on one of the objects and display the result.

class Dog:
    breed = "Unknown breed"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name}, says {sound}"

dog1 = Dog("Xavi", 3)
dog2 = Dog("Tavi", 4)

print(f"Dog 1 : Name - {dog1.name}, Age - {dog1.age}")
print(f"Dog 2: Name - {dog2.name}, Age - {dog2.age}")

dog1.name = "Max"
print(f"Dog1 new name: {dog1.name}")


description_result = dog2.description()
print(description_result)

speak_result = dog2.speak("ham")
print(speak_result)