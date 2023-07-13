x=[]
n=int(input("enter the number of elements you want to read:"))
for i in range(0,n):
    item=int(input("enter the elements :"))
    x.append(item)
print("list of elements are:")
print(x)
for i in range (0,n):
    pos=i
    for j in range(i+1,n):
        if(x[j]<x[pos]):
            pos=j
    temp=x[i]
    x[i]=x[pos]
    x[pos]=temp
print("sorted elements are:")
print(x)