# Program to find whether the string is Palindrome or not.

def is_palindrome(s):
    s.lower()
    reversed_s = s[::-1]
    return s == reversed_s
s = input("Enter any String:")
if is_palindrome(s):
    print(f"{s} is Palindrome.")
else:
    print(f"{s} is not Palindrome.")