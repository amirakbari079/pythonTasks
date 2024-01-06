

# 3
# print("============3============")
# Define the number of rows
rows = 9

for i in range(1, rows):
    # Inner loop for the numbers in each row
    for j in range(1, rows - i + 1):
        print(i, end=' ')
    # Move to the next line after each row is printed
    print()
# ---------------

4
print("============4============")
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

input_number = int(input("Enter your number: ")) 
multiplication_table(input_number)

5
print("============5============")
rows = 10
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        square = i * j
        print(square, end=' ')
    print()
# ---------------

# 6
# print("============6============")
def is_prime(number):
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if (number % i) == 0:
                return False
        return True
    else:
        return False

# Example usage
number1 = int(input("Enter your number 1: "))   # Replace 11 with the first number you want to check
number2 = int(input("Enter your number 2: "))   # Replace 15 with the second number you want to check
print(f"{number1} is prime: {is_prime(number1)}")  
print(f"{number2} is prime: {is_prime(number2)}") 
# ---------------

