contact = {}
def add_contacts():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    a = f"{first_name} {last_name}"
    if a in contact.keys():
        print(f"Contact already exists for {first_name} {last_name}")
    else:
        phone = input("Enter Phone Number: ")
        if len(phone) <10 or len(phone) > 12:
            print("invalid number")
        else:
            contact[a] = phone
            print("Contact added")
    return


def get_contacts():
    n = input("enter the full name: ")
    if n in contact.keys():
        return contact[n]
    else:
        return "Contact not found"

def saved_contacts():
    p = input("enter the phone number: ")
    for k, v in contact.items():
        if v == p:
            print(k)
        return
    else:
        return "Contact is not saved"

def display_contacts():
    for k, v in contact.items():
        print(f"{k}: {v}")
    return

def delete_contact():
    phone = input("Enter the full name :")
    if phone in contact.keys():
        del contact[phone]
        print("Contact deleted")
        return
    else:
        return "Contact not found"

def update_contact():
    phone = input("Enter the full name:")
    if phone in contact.keys():
        a = input("Enter the phone number: ")
        contact.update({phone: a})
        print("Contact updated")
        return
    else:
        return "Contact not found"
def update_name():
    d = input("enter the wrong name: ")
    if d in contact.keys():
        j = input("Enter the new name: ")
        x = contact.get(d)
        contact.pop(d)
        contact.update({j:x})
        print("Contact updated")
        return
    else:
        return "Contact not found"
ad = {}
def additional_details():
    x = []
    j = input("Enter the contact name: ")
    if j in contact.keys():
        dob = input("enter dob :")
        add = input("enter address: ")
        email = input("enter email: ")
        note = input("enter a note: ")
        x.append(j)
        x.append(dob)
        x.append(add)
        x.append(email)
        x.append(note)
        ad[j] = x
        print("details added")
        return
    else:
        return "contact not found"
def get_additional_details():
    g = input("enter contact name: ")
    if g in contact.keys() and g in ad.keys():
        print(f"{g}: name - {ad.get(g)[0]}")
        print(f"     dob - {ad.get(g)[1]}")
        print(f"     adress - {ad.get(g)[2]}")
        print(f"     email id - {ad.get(g)[3]}")
        print(f"     note - {ad.get(g)[4]}")
        return
    else:
        return "contact not found"

AAA = True
while AAA:
    print("------------------------------------------------")
    print("YOUR CONTACTS")
    print("1) add a new contact")
    print("2) display all contacts")
    print("3) delete a contact")
    print("4) update a contact")
    print("5) get contact details")
    print("6) get contact for a name")
    print("7) add additional details for a contact")
    print("8) additional details for a contact")
    print("9) exit")
    print("------------------------------------------------")

    t = int(input("Enter your choice: "))
    if t == 1:
        add_contacts()
        r = input("add additional details? (y/n): ")
        if r == "y":
            additional_details()

    elif t == 2:
        display_contacts()
    elif t == 3:
        ds = delete_contact()
        print(ds)
        if ds == "Contact not found":
            r = input("add new contact? (y/n): ")
            if r == "y":
                add_contacts()
            elif r == "n":
                continue
    elif t == 4:
        z = input("do you want to update contact number or contact name: ")
        if z == "contact name":
            update_name()
        elif z == "contact number":
            update_contact()
    elif t == 5:
        gh = get_contacts()
        print(gh)
        if gh == "Contact not found":
            r = input("add new contact? (y/n): ")
            if r == "y":
                add_contacts()
        else:
            r = input("see additional details? (y/n): ")
            if r == "y":
                get_additional_details()
    elif t == 6:
        saved_contacts()
        r = input("see additional details? (y/n): ")
        if r == "y":
            get_additional_details()
    elif t == 7:
        jj = additional_details()
        print(jj)
        if jj == "Contact not found":
            r = input("add new contact? (y/n): ")
            if r == "y":
                add_contacts()
            elif r == "n":
                continue
    elif t == 8:
        pp = get_additional_details()
        print(pp)
        if pp == "Contact not found":
            r = input("add new contact? (y/n): ")
            if r == "y":
                add_contacts()
            elif r == "n":
                continue
    elif t == 9:
        AAA = False
    else:
        print("invalid choice ! Try again")