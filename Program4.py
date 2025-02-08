#program to Swap two variable

num1= int(input("Enter the first value:"))
num2= int(input("Enter the second value:"))
print("num1 before swapping:", num1)
print("num2 before swapping:", num2)
temp = num1
num1 = num2
num2 = temp
print("num1 after swapping:", num1)
print("num2 after swapping:",num2)