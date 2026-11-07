
# OOP Wrapper - Employee Management System
# Author: Prince Shah
# Guided by: Girish Gondaliya

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        pass

class Employee(Person):

    def __init__(self, name, age, employee_id="", salary=0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = float(salary)

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = float(salary)

    # Method Overloading Concept
    def calculate_bonus(self, *args):
        if len(args) == 0:
            return self.__salary * 0.05
        elif len(args) == 1:
            return self.__salary * args[0] / 100

    def display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $", self.__salary)

class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("Manager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Department:", self.department)

class Developer(Employee):

    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        print("Developer Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Programming Language:", self.programming_language)

def main():

    persons = []
    employees = []
    managers = []

    while True:

        print("\n--- Python OOP Project: Employee Management System ---")
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))

            p = Person(name, age)
            persons.append(p)

            print("\nPerson created with name:", name,
                  "and age:", age)

        elif choice == "2":

            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))

            e = Employee(name, age, employee_id, salary)
            employees.append(e)

            print("\nEmployee created with name:", name,
                  "age:", age,
                  "ID:", employee_id,
                  "and salary: $", salary)

        elif choice == "3":

            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")

            m = Manager(name, age, employee_id, salary, department)
            managers.append(m)

            print("\nManager created with name:", name,
                  "age:", age,
                  "ID:", employee_id,
                  "salary: $", salary,
                  "and department:", department)

        elif choice == "4":

            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":

                if persons:
                    for p in persons:
                        print("\nPerson Details:")
                        p.display()
                else:
                    print("No Person details available.")

            elif sub_choice == "2":

                if employees:
                    for e in employees:
                        e.display()
                else:
                    print("No Employee details available.")

            elif sub_choice == "3":

                if managers:
                    for m in managers:
                        m.display()
                else:
                    print("No Manager details available.")

            else:
                print("Invalid choice.")

        elif choice == "5":

            print("\nExiting the system.")
            print("Goodbye!")
            break

        else:

            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()