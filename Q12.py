# Q12.WAP to print the simple number
n= int(input("Enter a rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()