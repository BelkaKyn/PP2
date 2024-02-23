1
class String:
    def __init__(self):
        self.string = str
        
    def get_string(self):
        self.string = input('String: ')
        
    def print_string(self):
        print(self.string.upper())
        
f = String()
f.get_string()
f.print_string()


2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

square = Square(10)
print("Shape's area:", square.area())  

3
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
        
rectangle = Rectangle(5, 3)
print("Shape's area:", rectangle.area())  
4

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print("Координаты точки: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        distance = ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
        return distance

#Пример ниже
'''
point1 = Point(2, 3)
point2 = Point(-1, 5)


point1.show()  
point2.show()  


point1.move(1, -2)
point2.move(3, 1)


point1.show()  
point2.show()  


distance = point1.dist(point2)
print("Distance between them:", distance) 
'''

5.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted")
        else:
            print("Withdrawal amount exceeds available balance.")

    def display_balance(self):
        print(f"Balance: {self.balance}")


#Пример
'''
my_account = BankAccount("Baktiyar Kobegen")


my_account.deposit(100)
my_account.deposit(50)


my_account.withdraw(30)
my_account.withdraw(20)


my_account.withdraw(200)  


my_account.display_balance()  
'''

6.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [1, 2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)
