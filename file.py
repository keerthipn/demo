file=None
def showMenu():
    print("student admission")
    print("1---> New admisssion:")
    print("2--->display all:")
    print("3-->Exit")
def newAdmission():
    global file
    uucmsno=input("enter your uucms number:")
    name=input("enter your name:")
    file=open("file.CSV","a")
    s=f"{uucmsno},{name}\n"
    file.write(s)
    file.close()
    print("students done successfully")
def displayAll():
    global file
    file=open("file.CSV","r")
    data=file.read()
    lines=data.split("\n")
    lines=lines[0:len(lines)-1]
    print("uucmsno\tname")
    for l in lines:
        s=l.split(",")
        print(f"{s[0]} \t {s[1]}")
        file.close()
        print("lines")
while(True):
    showMenu()
    choice=int(input("enter your choice:"))
    if(choice==1):
        newAdmission()
    elif(choice==2):
        displayAll()
    elif(choice==1):
        break
    else:
        print("invalid choice")