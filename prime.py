n=int(input("enter the number:"))
flag=False
for i in range(2,n//2+1):
    if(n%i==0):
        flag=True
        break
if(flag==False):
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime")