birthdays = {"Alice":"April 1","Bob":"December 12", "Carol":"March 4"}
while True:
    print(birthdays)
    print("Enter name: Type blank to stop.")
    name = input()
    str(name)
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print('I do not have birthday information for ' + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print('Birthday info added')
        print (birthdays)