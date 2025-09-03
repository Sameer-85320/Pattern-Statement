# Q6. WAP to print Star(1,5) with Space
n=int(input("Enter a number of underscores in first row: "))
for i in range(n,0,-1):
    print(" *"*1 + "_"*i + "* "*1)