global nox
nox=0
global idd
global head
class Node:
    def __init__(self, x,id=0,fert=0):
        self.data = x
        self.id=int(id) 
        self.fert=int(fert)
        self.children=[]

def addChild(x,nu):
    global nox
    global idd
    global head
    if nox!=1:
        newnode=Node(x)
        head=newnode
        temu=nu
        newnode.id=1

        while temu!=0:
            inp=input(f"enter names of {x}'s child {temu}:")
            childnode=Node(inp)
            newnode.children.append(childnode)
            newnode.fert=nu
            temu-=1
        nox=1
        print(f"Node:{newnode.data} id:{newnode.id} fertility:{newnode.fert} children:",[child.data for child in newnode.children])
        return newnode

def disp(n):
    print("hello")
    temp=n
    if n.id==0: 
        return
    print("hello 2")
    print(f"Node:{temp.data} id:{temp.id} fertility:{temp.fert} children:",[child.data for child in temp.children])
    temp_fert=temp.fert
    for child in n.children:
        disp(child)

#def addchildren(x,nu):

if __name__ == "__main__":
    name=input("Enter the name of the tree.")
    number=int(input(f"Enter the number of children of the root node {name}"))
    root=addChild(name,number)
    print("\t Commands")
    print("1-display\n2-add\n3-remove\n4-update")
    while True:
        opt=int(input("Enter the option:"))
        if opt==1:            
            disp(root)
        elif opt==2:
            print("Current id's")
            for child in head.children:
                print(child.id)
            loc_id=int(input("enter the id you wanna enter:"))




