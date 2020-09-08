String = input("Enter a string:")
RString = String[::-1]

print("\nThe reversed string is: ", RString, "\n")

if RString == String:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
