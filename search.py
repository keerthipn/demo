x=[]
n=int(input("enter the number of elements you want t0 read:"))
for i in range(0,n):
    item=int(input('enter elements:'))
    x.append(item)
key=int(input("enter the element to be searched:"))
pos=-1
for i in range(0,n):
    if(key==x[i]):
        pos=i
        break
if(pos==-1):
    print(f"{key} element not found:")
else:
    print(f"{key} element is found at {pos} position")
