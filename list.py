l=[]
for i in range(0,5):
    uucmsno=input("enter the uucms number:")
    info=input("enter the name and adress of the student:")
    per=float(input("enter the percentage:"))
    s=uucmsno+","+info+","+str(per)
    l.append(s)
print(l)
l1=[]
l2=[]
for s in l:
    x=s.split(",")
    per=float(x[-1])
    if(per>=60):
        y=x[0]+","+str(per)
        l.append(y)
    info=x[1].split(" ")
    z=info[1:3]
    l2.append(z)
print(l1)
print(l2)