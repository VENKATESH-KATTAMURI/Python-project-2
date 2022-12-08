print('CONTACT ADDRESS BOOK APP')
print()
# Mydict=dict()
Mydict=dict()
while True:

    print('''*********** MENU *********

    1) Add New Contact
    2) Display all contacts
    3) Search for Contact''')
    print('****************************')
    choice=int(input('Enter Your Choice: '))
    

    if choice==1:
        while True:
            print('PLEASE ENTER CONTACT DETAILS')
            print()
            name=input('Enter Name: ').upper()
            num=int(input('Enter Phone Number: '))
            Mydict.update({name:num})
            c=input('Do you want to add more number??(Y/N): ')
            if c=='y' or c=='Y':
                continue
            else:
                break
    if choice==2:
        print('CONTACTS IN YOUR CONTACT LIST ARE')
        print()
        for i in Mydict:
            print(i,' : ',Mydict[i])
        print()
    if choice==3:
        print('SEARCH FOR A PARTICULAR CONTACT')
        search=input('Enter Name: ').upper()
        print()
        print(search,' : ',Mydict[search])
        print()

