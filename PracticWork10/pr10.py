# Task 1

# a = float(input("Enter first number (a): "))
# b = float(input("Enter second number (b): "))

# sum_res = a + b
# diff_res = a - b
# prod_res = a * b

# if b != 0:
#     quot_res = a / b
#     print(f"Quotient (a / b): {quot_res}")
# else:
#     print("Quotient (a / b): Undefined (division by zero)")

# print(f"Sum (a + b): {sum_res}")
# print(f"Difference (a - b): {diff_res}")
# print(f"Product (a * b): {prod_res}")

# Task 2

# a = int(input("Enter first number (a): "))
# b = int(input("Enter second number (b): "))

# if a > b:
#     print(f"{a} is greater than {b}")
# elif a < b:
#     print(f"{b} is greater than {a}")
# elif a == b:
#     print(f"{a} is equal to {b}")
# else:
#     print("Invalid input")

# Task 3

# a = input("Enter a text: ")
# len = len(a)

# if len < 5:
#     print("Short text")
# elif 5 <= len <= 15:
#     print("Medium text")
# else:
#     print("Long text")

# Task 4

min_diapazon = 5
max_diapazon = 20

num = int(input("Enter a number: "))

if min_diapazon <= num and num <= max_diapazon:
    print(f"The number {num} is within the range of {min_diapazon} to {max_diapazon}.")
else:
    print(f"The number {num} is outside the range of {min_diapazon} to {max_diapazon}.")

if num < min_diapazon or num > max_diapazon:
    print(f"The number {num} is outside the specified range.")