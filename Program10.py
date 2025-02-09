# Program for printing the cube of list elements using Lambda.

l = []
n = int(input("Enter the number of elements in the list:"))
for i in range(n):
    num = int(input(f"Enter elements {i+1}:"))
    l.append(num)

res = list(map(lambda x : x**3, l))
print("Normal list:",l)
print("Cubed list:", res)