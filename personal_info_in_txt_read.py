#Input the name
firstname = input("please enter your first name: ").strip()
lastname = input("please enter your last name: ").strip()
middlename = input("please enter your middle name: ").strip()

#Format
name = f"{lastname}, {firstname}, {middlename}"

#Read the .txt file with the name
with open(".\personal_info.txt", "r") as file_handle:
    found = False  #Flag to check if the name is found
    for line in file_handle: #Loop
        if name in line: #Case insensitive checking
            found = True
            line1 = file_handle.readline().strip()
            line2 = file_handle.readline().strip()
            line3 = file_handle.readline().strip()
            line4 = file_handle.readline().strip()
            line5 = file_handle.readline().strip()
            line6 = file_handle.readline().strip()

            print(f"Name: {name}")
            print(f"{line1}")
            print(f"{line2}")
            print(f"{line3}")
            print(f"{line4}")
            print(f"{line5}")
            print(f"{line6}")
    
    if not found:
        print(f"Name '{name}' not found in the file.")