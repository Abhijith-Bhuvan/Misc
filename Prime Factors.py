x = 'a'

while(True):
    x = input("\n\tEnter a positive number:")
    if (x.isdigit()):
        break
    else:
        print("\nYou did not enter a positive number. Please try again...")

x = int(x)
f = False
L = [1]

for i in range(2, int(x / 2) + 1):
    if 0 == x % i:
        L.append(i)
        f = True

if not f:
    print("\n\n\t\tThe entered number was a prime.")
L.append(x)
print("\n\t\tList of divisors:  ", L)
