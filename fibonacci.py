n=int(input("enter the number:"))
fib1=0
fib2=1
if(n==fib1 or n==fib2):
    print(f"{n} is fibonacci series number")
else:
    while(True):
        fib3=fib1+fib2
        if(fib3==n):
            print(f"{n} is a fibonacci series number")
            break
        elif(fib3>n):
            print(f"{n} is not fibonacci number")
            break
        else:
            fib1=fib2
            fib2=fib3