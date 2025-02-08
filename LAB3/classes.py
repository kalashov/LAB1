# Task 1
class MyClass:
    def getString(self):
        self.s = input("Enter a string: ")
    
    def printString(self):
        print(self.s.upper())

# Task 2
class Shape:
    def __init__(self):
        self.area_value = 0
    
    def area(self):
        print(f"Area: {self.area_value}")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.area_value = length * length

# Task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area_value = length * width

# Task 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Task 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

# Task 6
is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
filter_primes = lambda numbers: list(filter(is_prime, numbers))