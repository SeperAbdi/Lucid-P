from employee import Employee

def main():

    #do something as a new project to re-use the external class

    employee =  Employee()
    info = employee.info()
    print("---------------------------\n")
    print(f"First Name is: {info[0]}")
    print(f"Last name is: {info[1]} ")
    print(f"Department is: {info[2]}")
    print(f"Title is {info[3]}")
    print(f"Email is {info[-1]}")
    print("This program has been ended ")

if __name__ == "__main__": main()