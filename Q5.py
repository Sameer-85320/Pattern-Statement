# Q5. WAP to print the Star(1,5) and 2,3,4 print Space
n=int(input("Enter the row: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == n:
            print("*", end=" ")
        else:
            print("_", end=" ")
    print()