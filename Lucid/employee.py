class Employee:
    def __init__(self):
        print("Welcome ro employee manager app")
        print("---------------------------------\n")

    # This Method accept emaployee data  and return them for feture use
    def info(self):
        name = input("Please enter your First name: ")
        last = input("Please enter your last name: ")
        dep = input("Which department are you working: ")
        title = input("Please enter your title: ")
        email = str(name) + '.' + str(last) + '@mycompany.com'
        return name, last, dep,title, email


def main():
    employee = Employee()
    name, last, dep,title, email = employee.info()
    print(f"Fullname: '{name} {last }' Department: '{dep}' Title:  '{title}'  and email is '{email}'")


if __name__ == '__main__': main()
