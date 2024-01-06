# 1
print("============1============")
def is_palindrome(input):
    # Convert the input to a string and compare it with its reverse
    return str(input) == str(input)[::-1]

# Test the function with a number and a string
number = 12321
string = "radar"
print(is_palindrome(number))  # Output: True
print(is_palindrome(string))
# ---------------

# 2
# print("============2============")
def calculate_net_salary(salary):
    # Calculate insurance deduction (7%)
    insurance_deduction = 0.07 * salary
    # Calculate tax deduction (10%)
    tax_deduction = 0.10 * salary
    # Calculate net salary
    net_salary = salary - insurance_deduction - tax_deduction
    return net_salary

# Example usage
salary = int(input("Enter your sallary: "))
net_salary = calculate_net_salary(salary)
print(f"The net salary after insurance and tax deductions is: {net_salary}")
# ---------------


# 3
print("============3============")
def sum_of_digits(number):
    # Calculate the sum of the digits
    sum = 0
    while number:
        sum += number % 10
        number = number // 10
    return sum

# Example usage
number=int(input("Enter your number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")
# ---------------

4
print("============4============")
def convert_distance(kilometers):
    # Convert to meters
    meters = kilometers * 1000
    # Convert to centimeters
    centimeters = kilometers * 100000
    # Convert to miles
    miles = kilometers * 0.621371

    return meters, centimeters, miles

# Example usage
distance_in_kilometers = int(input("Enter your distance in kilometers: "))  # Replace 10 with the actual distance in kilometers
meters, centimeters, miles = convert_distance(distance_in_kilometers)
print(f"{distance_in_kilometers} kilometers is equal to {meters} meters, {centimeters} centimeters, and {miles} miles")
# ---------------

# 5
print("============4============")
import xml.etree.cElementTree as ET

# Function to convert inputs to XML
def create_xml(data1, data2, data3, data4,data5):
    root = ET.Element("User")
    item1 = ET.SubElement(root, "field")
    item1.text = data1
    item2 = ET.SubElement(root, "grade")
    item2.text = data2
    item3 = ET.SubElement(root, "name")
    item3.text = data3
    item4 = ET.SubElement(root, "age")
    item4.text = data4
    item5 = ET.SubElement(root, "bmi")
    item5.text = data5
    tree = ET.ElementTree(root)
    tree.write("output.xml")

# Example usage
field =  input("Enter your field: ")
grade =  input("Enter your grade: ")
name =  input("Enter your name: ")
age = input("Enter your age: ")
bmi = input("Enter bmi: ")
create_xml(field, grade, name, age,bmi)
