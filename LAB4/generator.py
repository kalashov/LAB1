#1
def squares_up_to(n):
    for i in range(n+1):
        yield i*i

print("Squares up to 5:")
for x in squares_up_to(5):
    print(x, end=" ")
print()

# 2
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n_input = int(input("Enter n: "))
print("Even numbers up to", n_input, ":")
print(*even_numbers(n_input), sep=",")

# 3
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("Numbers between 0 and 30 divisible by 3 and 4:")
for x in divisible_by_3_and_4(30):
    print(x, end=" ")
print()

# 4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

print("Squares from 3 to 7:")
for x in squares(3, 7):
    print(x, end=" ")
print()

# 5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

print("Countdown from 5:")
for x in countdown(5):
    print(x, end=" ")
print()