# Q4. WAP to print the Odd number(1,3,5) and Even Star(2,4)
n= int(input("Enter a rows: "))
for i in range(1,6):
    num = 1
    for j in range(i):
        if (j % 2 == 0):
            print(num, end=" ")
            num+=2
        else:
            print("*",end=" ")
    print()