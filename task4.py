# 1
# print("============1============")
def is_armstrong_number(number):
    order = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return number == sum

# Example usage
input_number = int(input("Enter your number : "))  # Replace 153 with the actual number you want to check
print(is_armstrong_number(input_number))  # Output: True


# 2
# print("============2============")
# Initialize the largest number as the smallest possible value
largest = float('-inf')

# Loop to take 10 numbers as input
for _ in range(10):
    number = float(input("Enter a number: "))
    if number > largest:
        largest = number

# Print the largest number
print(f"The largest number is: {largest}")

# 3
# print("============3============")
import math
# Initialize the sum
s = 0

# Calculate the sum of factorials
for i in range(-2, 21):
    if i < 0:
        s -= math.factorial(abs(i))
    else:
        s += math.factorial(i)

# Print the result
print(s)