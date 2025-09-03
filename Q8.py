# Q8. WAP to print the reverse aligned right angle 
rows=int(input("Enter a rows: "))
for i in range(rows, 0, -1):
    for j in range(rows - i):
            print("_", end=" ")
    for k in range(i):     
            print("*", end=" ")
    print()