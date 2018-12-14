a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print("Common divisor=")
for i in range(1,b+1):
    if (b%i==0 and a%i==0):
        print(i)