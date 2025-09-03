# Q15. WAP to print the star pattern diamond shape without space
n=int(input("Enter a rows: "))
for i in range(1,n+1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)