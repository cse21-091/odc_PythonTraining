print("Welcome to the Automated Driving Licence Booking System.")
print("Please enter your full names:")
full_names = input("")

print(full_names+","+" how old are you?")
age = int(input(""))

if age >= 18:
    print("Do you want to book for the theory test?")
    print("1. Press 1 for yes \n2. Press 2 for no")
    option = int(input("\nEnter your option:"))
    
    if option == 1:
        location = int(input("\nPlease select location: \n1. Gaborone  \n2. Francistown\n"))
        if location == 1:
            select=int(input("Please select from available slots: \n1. Morning session \n2. Afternoon session \n"))
            if select==1:
                print("The available slot is in Gaborone at 9am.")
                id=int(input("Please enter your ID number to book the slot:\n"))
                print(full_names+","+" your session has been booked! Thank you.")
            elif select == 2:
                print("The available slot is in Gaborone at 2pm.")
                id=int(input("Please enter your ID number to book the slot:\n"))
                print(full_names+","+" your session has been booked! Thank you.")
            else:
                print("Invalid selection")
        elif location == 2:
             select=int(input("Please select from available slots are: \n1. Morning session \n2. Afternoon session \n"))
             if select == 1:
                print("The available slot is in Francistown at 9am.")
                id=int(input("Please enter your ID number to book the slot:\n"))
                print(full_names+","+" your session has been booked! Thank you.")
             elif select == 2:
                print("The available slot is in Francistown at 2pm.")
                id=int(input("Please enter your ID number to book the slot:\n"))
                print(full_names+","+" your session has been booked! Thank you.")
             else:
                print("Invalid selection")
        else:
            print("Invalid selection")
    elif option == 2:
        print("Ok! Have a great day.")
    else:
        print("Invalid selection")
else:
    print("You are not eligible to register")
        
    
    


            
