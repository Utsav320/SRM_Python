# Program to find out the positive and negative number in the list.

n = int(input("Enter the number of elements in the list: "))
numbers = []
positive_numbers = []
negative_numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
print(f"All list are:{numbers}")
print(f"Positive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")