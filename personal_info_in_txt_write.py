personal_info = {}

#use the loop
while True:
    try:
        while True:
            #ask the user to input the name
            name = input("please enter your nickname: ")

            if name.isalpha():
                break
            else:
                print("Something is wrong...")
                continue

        while True:
            #ask the user to input their personal information
            firstname = input("please enter your first name: ")

            if firstname.isalpha():
                break
            else:
                print("Something is wrong...")
                continue

        while True:
            #ask the user to input their personal information
            lastname = input("please enter your last name: ")

            if lastname.isalpha():
                break
            else:
                print("Something is wrong...")
                continue

        while True:
            #ask the user to input their personal information
            middlename = input("please enter your middle name: ")

            if middlename.isalpha():
                break
            else:
                print("Something is wrong...")
                continue

        while True:
            #ask the user to input their personal information
            age = input("please enter your age: ")

            if age.isdigit():
                break
            else:
                print("Something is wrong...")
                continue

        while True:
            #ask the user to input their personal information
            birth_month = input("please enter your birth month in numbers: ")
            birth_day = input("please enter your birth day: ")
            birth_year = input("please input your birth year: ")

            if birth_month.isdigit() and birth_day.isdigit() and birth_year.isdigit() and len(birth_year) == 4:
                break
            else:
                print("Something is wrong...")
                continue

        while True:
            #ask the user to input their personal information
            address = input("please enter your address: ")
            break

        while True:
            #ask the user to input their personal information
            phone_number = input("please enter your phone number: ")

            if phone_number.isdigit() and len(phone_number) == 11:
                break
            else:
                print("Something is wrong...")
                continue

        while True:
            #ask the user to input their personal information
            email_address = input("please enter your email: ")
            break

        #format
        fullname = f"{lastname}, {firstname}, {middlename}"
        birth = f"{birth_month}/{birth_day}/{birth_year}"

        #insert the personal information into the name's dictionary
        personal_info[name] = {
            "name" : fullname ,
            "age" : age ,
            "birthday" : birth ,
            "address" : address ,
            "phone number" : phone_number ,
            "email address" : email_address
        }
        
        print(f"\nName: {personal_info[name]['name']}\n")
        print(f"Age: {personal_info[name]['age']}\n")
        print(f"Birthday: {personal_info[name]['birthday']}\n")
        print(f"Address: {personal_info[name]['address']}\n")
        print(f"Phone Number: {personal_info[name]['phone number']}\n")
        print(f"Email Address: {personal_info[name]['email address']}\n")

        
        #enter the dictionary for writing in the text file
        with open(".\personal_info.txt", "a") as file_handle:
            file_handle.write(f"{name}'s Personal Information:\n")
            file_handle.write(f"Name: {personal_info[name]['name']}\n")
            file_handle.write(f"Age: {personal_info[name]['age']}\n")
            file_handle.write(f"Birthday: {personal_info[name]['birthday']}\n")
            file_handle.write(f"Address: {personal_info[name]['address']}\n")
            file_handle.write(f"Phone Number: {personal_info[name]['phone number']}\n")
            file_handle.write(f"Email Address: {personal_info[name]['email address']}\n")
            file_handle.write("\n")  # Separate records by a blank line
        
        #ask the user to continue or not
        continue_or_not = input("Would you like to continue? (y or n): ")

        if continue_or_not == "n":
            print("All input has been added!")
            break
        elif continue_or_not != "y":
            print("please input y or n.")
            continue

    except:
        print("Unexpected error, please try again.")