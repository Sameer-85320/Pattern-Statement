# Q13. WAP to print reverse simple number
n= int(input("Enter a rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()