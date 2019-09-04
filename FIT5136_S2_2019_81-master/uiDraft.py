

adminAccounts = {'a1':['email','123@abc','password','123']}
ownerAccounts = {'o1':['email','234@abc','password','123']}
customerAccounts = {'c1':['email','567@abc','password','123','2.Caulfield hall',
                          'Number of guests: 10\nEvent date: 9/1/19\nDecoration cost: $50\nCatering cost: $300\
                          \nPhotography cost:$30\nTotal cost: $380\nAlready received deposit: $190\
                          \nPlease pay the rest of cost before 8/31/2019]']}


def register():
    pass


def welcomeInterface():
    print('\n\n'+('*'*50).center(100))
    print('Welcome to Prime Events system'.center(100))
    print(('*' * 50).center(100))
    print('\nPlease enter your account:')
    userAccount = input()
    print('Welcome !! ' + userAccount)
    print('\nPlease enter your password:')
    userPassword = input()

    # find the administrator/owner/customer account in adminAccounts/ownerAccounts/customerAccounts,
    # if the account exists, see whether the password is correct by finding the password after the value 'password'
    if userAccount in adminAccounts :
        for i in range(len(adminAccounts[userAccount])-1):
            if adminAccounts[userAccount][i] == 'password':
                if adminAccounts[userAccount][i+1] == userPassword:
                    loginAsAdministrator(userAccount)
                else:
                    print('Wrong account or password')


    elif userAccount in ownerAccounts :
        for i in range(len(ownerAccounts[userAccount])-1):
            if ownerAccounts[userAccount][i] == 'password':
                if ownerAccounts[userAccount][i+1] == userPassword:
                    loginAsOwner(userAccount)
                else:
                    print('Wrong account or password')


    elif userAccount in customerAccounts :
        for i in range(len(customerAccounts[userAccount])-1):
            if customerAccounts[userAccount][i] == 'password':
                if customerAccounts[userAccount][i+1] == userPassword:
                    loginAsCustomer (userAccount)
                else:
                    print('Wrong account or password')

    else:
        print('Wrong account or password')





def loginAsAdministrator(userAccount):
    pass

def loginAsOwner(userAccount):
    pass

def loginAsCustomer(userAccount):
    print('\n\n\n')
    print('*' * 80)
    print('You can choose your option, please enter the number')
    print('1.Search a hall')
    print('2.Book a hall')
    print('3.View booking history')
    print('4.Request for quotation')
    print('5.Manage payments')
    print('6.View receipt')
    print('7.Rating')
    print('8.Logout')
    print('*' * 80)

    choice = input()
    if choice == '6' :
        viewReceipt(userAccount)
    elif choice == '8' :
        print('Thanks for using Prime Events system!')
        return

def viewReceipt(userAccount):
    print('\n\n\n')
    print('*' * 80)
    print('There are your receipt records:')
    print('1.Clayton hall')
    print('2.Caulfield hall')
    print('3.Flinders street hall')
    print('4.Go back')
    print('You can enter the number of the hall that you wan to view, or enter 4, go back')
    print('Please enter your option:')
    print('*' * 80)

    choice = input()

    # find the corresponding receipt in customerAccounts, after the exact name of the receipt record
    if choice == '2' :
        print('Here is your Caulfield hall receipt:')
        for i in range(len(customerAccounts[userAccount])-1):
            if customerAccounts[userAccount][i] == '2.Caulfield hall':
                print(customerAccounts[userAccount][i+1])

        print('If you want to go back, please enter 1.')
        choice = input()
        if choice == '1':
            viewReceipt(userAccount)

    elif choice == '4' :
        loginAsCustomer(userAccount)



def main():
    welcomeInterface()

if __name__ == "__main__":
    main()