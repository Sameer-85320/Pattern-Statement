# Q3. WAP to print the Reverse Triangle Star
n=int(input("Enter a rows: "))
for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()