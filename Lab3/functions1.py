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
import math

def sphere_volume(radius):
    if radius < 0:
        return "Radius cannot be negative"
    else:
        volume = (4/3) * math.pi * radius ** 3
        return volume

# Пример
radius = 5
volume = sphere_volume(radius)
print("Volume of the sphere with radius {} units: {:.2f}".format(radius, volume)nt

10.
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Пример
input_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(input_list)
print("Original list:", input_list)
print("List with unique elements:", result)

11.
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

# Пример
input_word = "Levels"
result = is_palindrome(input_word)
if result:
    print(f"{input_word} is a palindrome")
else:
    print(f"{input_word} is not a palindrome")

12.
def histogram(numbers):
    for num in numbers:
        print('*' * num)

# Пример
histogram([4, 9, 7])

13.
import random

def guess_the_number():
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())

        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

# Call the function to play the game
guess_the_number()

14....
