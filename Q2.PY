# Q2. WAP to print the Triangle Star
n=int(input("Enter a rows: "))              
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()