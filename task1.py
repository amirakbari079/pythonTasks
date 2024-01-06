# 1
a=10
b=3
a=a+b
b=a-b
a=a-b
print(a,b)
# ---------------

# 2
def reverse_number(number):
    return int(str(number)[::-1])
x = 34
reversed_number = reverse_number(x)
print(f"The reversed number of {x} is {reversed_number}")
# ---------------

# 3
seconds_in_a_year = 3.156 * 10**7
age = 48
age_in_seconds = age * seconds_in_a_year
print(f"A 48 year old man is approximately {age_in_seconds} seconds old.")
# ---------------