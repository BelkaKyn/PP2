1.
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Пример
grams_needed = 520
ounces_needed = grams_to_ounces(grams_needed)
print(f"{grams_needed} grams is equal to {ounces_needed:.2f} ounces")

2.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)

print(f"The actuall temperature in Celsius is: {celsius:.2f} degrees Celsius")

3.
def solve(numheads, numlegs):
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        totallegs = 2 * numchickens + 4 * numrabbits
        if totallegs == numlegs:
            return numchickens, numrabbits
    return "No solution"

numheads = 35
numlegs = 94

result = solve(numheads, numlegs)

if result != "No solution":
    numchickens, numrabbits = result
    print("Number of chickens:", numchickens)
    print("Number of rabbits:", numrabbits)
else:
    print("No solution found")

4.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

#Пример
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

5.
from itertools import permutations
def print_permutations(s):
    
    perms = permutations(s)

   
    for perm in perms:
        print(''.join(perm))


input_string = input("Enter a string: ")

print("Permutations of the string:")
print_permutations(input_string)

6.
def reverse_sentence(sentence):
    words = sentence.split()

    reversed_sentence = ' '.join(reversed(words))

    return reversed_sentence

input_sentence = input("Enter a sentence: ")

reversed_result = reverse_sentence(input_sentence)

print("Reversed sentence:", reversed_result)

7.
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#Примеры
print(has_33([1, 3, 3]))   
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))    

8.
def spy_game(nums):
    zero_pos = None
    seven_pos = None
    
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_pos = i
        elif nums[i] == 7:
            seven_pos = i
        
        if zero_pos is not None and seven_pos is not None and zero_pos < seven_pos:
            return True
    
    return False

#Примеры
print(spy_game([1,2,4,0,0,7,5])) # True
print(spy_game([1,0,2,4,0,5,7])) # True
print(spy_game([1,7,2,0,4,5,0])) # False

9.

