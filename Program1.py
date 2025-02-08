# Program to raise Indentation Error and correct it.

def max(x,y):
    if(x>y):
        return x
    else:
   # return y   # Indentated Code
        return y    # Corrected Code
a= int(input("Enter a number:"))
b= int(input("Enter second number:"))
print("Finding maximun out of a:",a, "and b:",b)
c = max(a,b)
print(c, "is maximum")



