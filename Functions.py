# EX1: Define a function that prints, one by one, the first 10 numbers (1 to 10).
def first_number():
    for i in range(1, 11):
        print(i)
first_number()


# EX2: Write a function that iterates over a given list of numbers and
# displays the message 'Even number' for even numbers and
# 'Odd number' for odd numbers.
# If the list contains an element that is not an integer,
# display a message to the user and skip that element.
# (Use the built-in function isinstance() to check
# if the current element is an int or not)

def check_odd_even(numbers):
    for i in numbers:
        if isinstance(i, int):
            if i % 2 == 0:
                print(f"{i}: Even number")
            else:
                print(f"{i}:Odd number")
        else:
            print(f"{i}: Not an integer, skipping..")
list_number = [1, 2, 3, "Hello", 23.3, 22.1]
check_odd_even(list_number)


# EX3: Write a function that calculates the square of a number.
# Display the result.
def square_number(i):
    square = i ** 2
    print(f"The square of {i} is {square}")
square_number(2)

# EX4: Write a function that calculates the division of two numbers.
# Display the result.

def divide_numbers(i, i2):
    if i2 == 0:
        print("Error: Division with zero is not allowed.")
    else:
        result = i / i2
        print(f"The result of dividing of {i} by {i2} is {result}")
divide_numbers(10, 2)

# EX5: Write a function that calculates the multiplication of two numbers.
# Display the result.

def multiply_numbers(i, i2):
    result = i * i2
    print(f"The result of multiplying", i, "and", i2, "is:", result )
multiply_numbers(2,3)


# EX6: Rewrite the function from exercise 3
# so that it returns the result.
def square_number(i):
    square = i ** 2
    return square

result = square_number(2)
print(f"The square of 2 is {result}")

# EX7: Rewrite the function from exercise 4
# so that it returns the result.



def divide_numbers(i, i2):
    if i2 == 0:
        return "Error: Division with zero is not allowed."
    else:
        result = i / i2
        return result
result = divide_numbers(10, 2)
if isinstance(result, str):
    print(result)
else:
    print(f"the result of dividing 10 by 2 is {result}")


# EX8: Write a function that takes an integer as a parameter
# and returns True if the number is even
# and False if the number is odd.

def is_even(number):
    return number % 2 == 0
print(is_even(2))
print(is_even(3))