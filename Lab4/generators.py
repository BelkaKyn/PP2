1.
def squares_generator(N):
    for i in range(1, N+1):
        yield i ** 2


N = 5
squares = squares_generator(N)

for square in squares:
    print(square)

2.
def even_numbers_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number (n): "))

even_numbers = even_numbers_generator(n)

print("Even numbers between 0 and", n, ":", end=" ")
for num in even_numbers:
    if num == 0:
        print(num, end="")
    else:
        print(",", num, end="")

3.
def divisible_by_3_and_4_generator(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number (n): "))

divisible_numbers = divisible_by_3_and_4_generator(n)

print("Numbers divisible by both 3 and 4 between 0 and", n, ":", end=" ")
for num in divisible_numbers:
    print(num, end=" ")

4.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the start number (a): "))
b = int(input("Enter the end number (b): "))

print("Squared values from", a, "to", b, ":")
for square in squares(a, b):
    print(square)

5.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number (n): "))

print("Counting down from", n, "to 0:")
for num in countdown(n):
    print(num)

