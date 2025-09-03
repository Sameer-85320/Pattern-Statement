# Q10. WAP to print the reverse Hollow Pyramid Pattern
n=int(input("Enter a rows: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    for j in range(2*n-2*i):
        print(" ", end="")
    for j in range(i):
        print("*",end="")
    print()