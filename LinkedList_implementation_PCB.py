class Process:
    def __init__(self, name, id, pri):
        self.name = name
        self.id = id
        self.pri = pri
        self.next = None

class PCB:
    def __init__(self):
        self.start = None

    def display(self):
        if self.start == None:
            print("empty PCB QUEUE")
        else:
            p = self.start
            print("name  id  priority")
            while(p != None):
                print(p.name, '\t', p.id, '\t', p.pri)
                p = p.next
        
    def insertstart(self, name, id, pri):
        print("\n\ninsertstart")
        myproc = Process(name, id, pri)
        myproc.next = self.start
        self.start = myproc
        print("\nNode inserted")

    def insertend(self, name, id, pri):
        print("\n\ninsertend")
        myproc = Process(name, id, pri)
        p = self.start
        while(p.next != None):
            p = p.next
        p.next = myproc
        print("\nNode inserted")

    def insertbw(self, name, id, pri, prevnode_id):
        print("\n\ninsertbw")
        myproc = Process(name, id, pri)
        p = self.start
        while(p.id != prevnode_id and p != None):
            p = p.next
        if (p==None):
            print("kacchu naahi hai linked list me aisan")
        else:
            print("mileya mileya mujhe")
            myproc.next = p.next
            p.next = myproc
        print("\nNode inserted")

    def deletestart(self):
        print("\n\ndeletestart")
        myproc = self.start
        self.start = myproc.next
        del(myproc)
        print("\nNode deleted")

    def deleteend(self):
        print("\n\ndeleteend")
        p = self.start
        while (p.next.next != None):
            p = p.next
        p.next = None
        del(p)
        print("\nNode deleted")

    def deletebw(self, myproc_id):
        print("\n\ndeletebw")
        p = self.start
        while(p.next.id != myproc_id and p.next != None):
            p = p.next
        if (p.next==None):
            print("kacchu naahi hai linked list me aisan")
        else:
            print("mileya mileya mujhe.....ab ye jayega")
            p.next = p.next.next
            del(p)
        print("\nNode deleted")

    def searchproc(self, myproc_id):
        p = self.start
        while (p.id != myproc_id):
            p = p.next
            print(p.id)
        if (p == None):
            print("kacchu naahi hai linked list me aisan")
        else:
            print(p.name, '\t', p.id, '\t', p.pri)

c=-1
pcb = PCB()
while c!=8:
    if c==0:
        pcb.display()
    elif c==1:
        name = input('\nEnter the name of the process: ')
        pid = int(input('Enter the id of the process: '))
        priority = float(input('Enter the priority of the process: '))
        pcb.insertstart(name, pid, priority)
    elif c==2:
        name = input('\nEnter the name of the process: ')
        pid = int(input('Enter the id of the process: '))
        priority = float(input('Enter the priority of the process: '))
        pcb.insertend(name, pid, priority)
    elif c==3:
        name = input('\nEnter the name of the process: ')
        pid = int(input('Enter the id of the process: '))
        priority = float(input('Enter the priority of the process: '))
        proc_id = int(input('\nEnter the id of the process you want to insert after'))
        pcb.insertbw(name, pid, priority, proc_id)
    elif c==4:
        pcb.deletestart()
    elif c==5:
        pcb.deleteend()
    elif c==6:
        proc_id = int(input('\nEnter the id of the process you want to delete'))
        pcb.deletebw(proc_id)
    elif c==7:
        proc_id = int(input('\nEnter the id of the process you want to search'))
        pcb.searchproc(proc_id)
    c = int(input('\nEnter your choice: \n0.Display \n1.Insert at beginning \n2.Insert at end \n3.Insert in between \n4.Delete from beginning \n5.Delete from end \n6.Delete from between \n7.Search a process \n8.Exit \n'))
