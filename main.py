# daily python project
print("Average Number Calculator")

# here we will ask user to input 3 numbers
num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))
num_three = int(input("Enter third number: "))

# adding all three inputs together
total_add = num_one + num_two + num_three

# dividing the total_add by the number of inputs
total_divide = int(total_add / 3)

print(total_divide)
