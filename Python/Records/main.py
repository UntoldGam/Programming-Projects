from json import loads

MemberNumber = int(open("members.txt", "r").readline().split("=")[1])  # e.g. 0
membersFile = open("members.txt", "r")
# works for a small file however as the file gets larger a more permenant solution should be found - this is if itt was implemented into a larger system rather than a small piece of test code
firstLine, wholeFile = membersFile.readline(), membersFile.read()


def locate(condition, name, member_number):
    with open("members.txt", "r") as f:
        text = f.readlines()
          # print(text)
        strings = []
        for string in text:
            # print(string)
            if string.startswith("{"):
                string = string.replace("\'", "\"")
                strings.append(string)
                #print(strings)
                
                for string in strings:
                    string = loads(string)
                    # print(type(string), string, string["Name"])
                    print(name, string['Name'])
                    print(member_number, string['memberNumber'])
                    if name == string['Name'] and member_number == string["memberNumber"]:
                        return string
                    else:
                       if string["Surname"] == condition or string["memberNumber"] == condition:
                        header = ""
                        if string["Surname"] == condition:
                            header = "Surname"
                        else:
                            header = "Member Number"
                            print(
                                f"\nA match has been found for {header} {condition}:\n======================================\nName: {string['Name']}\nSurname: {string['Surname']}\nMember Number: {string['memberNumber']}\nAddress: {string['Address']}\nCity: {string['City']}\nPostcode: {string['Postcode']}\nDate of Birth: {string['DateOfBirth']}\n======================================")

while True:
    choice = input("Are you a new or existing member? (N for New, E for Existing) ")

    if choice.upper() == "N":
        name = input("What is your first name? ")
        surname = input("What is your last name? ")
        address = input("What is your address? ")
        city = input("What is your city? ")
        postcode = input("What is your postcode? ")
        DateOfBirth = input("What is your date of birth? ")
        MemberNumber = MemberNumber + 1
        newMember = {"memberNumber": MemberNumber, "Name": name, "Surname": surname,
                     "Address": address, "City": city, "Postcode": postcode, "DateOfBirth": DateOfBirth}
        # print(newMember)
        
        newFirst = f"Total_Members={MemberNumber}"
        with open("members.txt", "w") as membersFile:
            membersFile.write(newFirst + "\n")
            membersFile.write(wholeFile + f"\n{str(newMember)}")
            membersFile.close()
    elif choice.upper() == "E":
        account_name = input("What is the name on your account? ").capitalize()
        member_number = input("What is your member number? ")
        account_information = locate("login", account_name, member_number)
        if not account_information == None:
            print(f"Welcome back {account_information['memberNumber']} | {account_information['Name']}")
        else:
            print("account information not found")
