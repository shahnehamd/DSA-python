class Ticket:
    def __init__(self, id, name, no, pass_name, pass_age, coach_no, berth_n, wt_no, status):
        self.id = id
        self.name = name
        self.no = no
        self.pass_name = pass_name
        self.pass_age = pass_age
        self.coach_no = coach_no
        self.berth_n = berth_n
        self.wt_no = wt_no
        self.status = status
id = 1
no_of_coaches = 2 #int(input('Enter the number of coaches in the train'))
no_of_berths = 1 #int(input('Enter the number of berths in the train'))
waiting_list=[None]*3 #int(input('Enter the number of waiting tickets'))
coaches = []
for i in range(0, no_of_coaches):
    berths = []
    for j in range(0, no_of_berths):
        berths.append(None)
    coaches.append(berths)
    
def allocate(id):
    pass_name = input('\nEnter your name: ')
    pass_age = input('Enter your age: ')
    t = Ticket(id, 'train1', 12345, pass_name, pass_age, 0, 0, 0, 'undefined')
    for i in range(0, no_of_coaches):
        for j in range(0, no_of_berths):
            if coaches[i][j]==None and t.status=='undefined':
                t = coaches[i][j] = t
                t.coach_no = i
                t.berth_n = j
                t.status = 'confirmed'
            if coaches[no_of_coaches-1][no_of_berths-1]!=None and t.status=='undefined':
                for k in range(0,len(waiting_list)):
                    if waiting_list[k] == None:
                        t=waiting_list[k]=t
                        t.wt_no = k
                        t.status = 'waiting'
                        break
    print('\nThe status of your booking is: ',t.status)
    if t.status == 'confirmed':
        print('\nYour booking id is: ',t.id)
        print('\nYour coach number is : ',t.coach_no+1,' and berth number is: ',(t.berth_n)+1,'\n')
    elif t.status == 'waiting':
        print('\nYour booking id is: ',t.id)
        print('\nYour waiting number is: ',(t.wt_no+1),'\n')
    print(coaches)
    print(waiting_list)
def deallocate():
    my_id = int(input('Enter your booking id: '))
    status = 'waiting'
    for ii in range(0, no_of_coaches):
        for jj in range(0, no_of_berths):
            if coaches[ii][jj] != None:
                if my_id == coaches[ii][jj].id:
                    status = 'confirmed'
                    i = ii
                    j = jj
    if status == 'confirmed':
        print('\nYour ticket details are as follows:','\nName: ',coaches[i][j].pass_name,'\nAge: ',coaches[i][j].pass_age,'\nStatus: ',coaches[i][j].status)
        confirming = int(input('Are your sure you want to cancel your booking? then, type 1.'))
        if confirming==1:
            coaches[i][j] = waiting_list[0]
            if waiting_list[0]!=None:
                coaches[i][j].status = 'confirmed'
            for i in range(0,len(waiting_list)-1):
                waiting_list[i]=waiting_list[i+1]
            waiting_list[len(waiting_list)-1] = None
        else:
            print('Booking not cancelled :)')
    elif status == 'waiting':
        for ii in range(0,len(waiting_list)-1):
            if my_id == waiting_list[ii].id:
                i = ii
        print('\nYour ticket details are as follows:','\nName: ',waiting_list[i].pass_name,'\nAge: ',waiting_list[i].pass_age,'\nStatus: ',waiting_list[i].status)
        confirming = int(input('Are your sure you want to cancel your booking? then, type 1.'))
        if confirming==1:
            for j in range(i,len(waiting_list)-1):
                waiting_list[j]=waiting_list[j+1]
            waiting_list[len(waiting_list)-1] = None
    else:
        print('invalid status')
    print(coaches)
    print(waiting_list)
def display_bookings():
    for i in range(0, no_of_coaches):
        for j in range(0, no_of_berths):
            if coaches[i][j] != None:
                print(coaches[i][j].id)
def display_waiting():
    for j in range(0,len(waiting_list)):
        if waiting_list[j] != None:
            print(waiting_list[j].id)
c=999
while c!=0:
    if c == 1:
        if waiting_list[len(waiting_list)-1] == None:
            allocate(id)
            id+=1
        else:
            print('No more bookings are possible. Try again later')
    elif c == 2:
        if waiting_list[len(waiting_list)-1] == None and coaches[0][0] == None:
            print('There are no existing bookings.')
        else:
            deallocate()
    elif c == 3:
        display_bookings()
    elif c == 4:
        display_waiting()
    c = int(input('Enter the value of c: \n'))
