# A program to reverse an integer

# Input Integer Value
number = int(input("Enter your Integer Value: "))
print("\nInput Number is : ", number)
reverse = 0

# Reverse Code
while (number != 0):
    reverse = (reverse * 10) + (number % 10)
    number = number // 10

# Print Reverse Number
print("Reverse Number is: ", reverse)