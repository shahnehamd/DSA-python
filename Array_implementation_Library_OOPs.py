class Book:
    def __init__(self, name, author, price, copies):
        self.name = name
        self.author = author
        self.price = price
        self.copies = copies

class Library:
    def display(self,Book):
        print(Book.name,'\t', Book.author,'\t', Book.price,'\t', Book.copies)

c=0
arr = []
l = Library()
while c!=6:
    if c==1:
        name = input('\nEnter the name of the book: ')
        author = input('Enter the name of the author: ')
        price = float(input('Enter the price of the book: '))
        copies = int(input('Enter the number of copies of the book: '))
        b = Book(name, author, price, copies)
        arr.append(b)
    elif c==2:
        print('Name    ','Author   ','Price    ','Copies   ')
        for i in arr:
            l.display(i)
    elif c==3:
        book = input('\nEnter the name of the book to be searched: ')
        flag = 0
        for i in arr:
            if book == i.name:
                print('Name    ', 'Author   ', 'Price    ', 'Copies   ')
                l.display(i)
                flag = 1
        if flag==0:
            print('No such book found')
    elif c==4:
        book = input('\nEnter the name of the author to be searched: ')
        flag = 0
        for i in arr:
            if book == i.author:
                print('Name    ', 'Author   ', 'Price    ', 'Copies   ')
                l.display(i)
                flag = 1
        if flag == 0:
            print('No such book found')
    elif c==5:
        print('Name    ', 'Author   ', 'Price    ', 'Copies   ')
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[i].name > arr[(j+1)].name:
                    arr[j], arr[(j+1)] = arr[(j+1)], arr[j]
        for i in arr:
            l.display(i)
    c = int(input('\nEnter your choice: \n1.Enter new book \n2.Display the entire list of books \n3.Display book with book name \n4.Display book with author name \n5.Display the entire list in sorted form \n6.Exit \n'))
