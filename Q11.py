# Q11. WAP to print the diamond with star and middle space 
n=int(input("Enter a rows: "))
for i in range(n):
    print("*" * (n - i), end="")
    print(" " * (2 * i), end="")
    print("*" * (n - i))
for i in range(n):
    print("*" * (i + 1), end="")
    print(" " * (2 * (n - i - 1)), end="")
    print("*" * (i + 1))