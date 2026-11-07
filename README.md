<div align="center">

# 👨‍💼 OOP Wrapper
### Employee Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Python%20Project-purple)
![OOP](https://img.shields.io/badge/Concepts-Python%20OOP-success)

**A simple menu-driven Employee Management System using Python Object-Oriented Programming.**

</div>

---

## 📌 Project Details

| Item | Details |
|---|---|
| Project Name | OOP Wrapper – Employee Management System |
| Programming Language | Python |
| Author | **Prince Shah** |
| Guided by | **Girish Gondaliya** |
| Project Type | Python OOP Project |

## 🎯 Objective

The objective of this project is to create a simple Employee Management System using Python OOP concepts such as classes, objects, constructors, encapsulation, inheritance, method overriding, and `super()`. The program allows the user to create Person, Employee, and Manager objects and display their details through a menu-driven interface.

## ✨ Main Menu

The program contains exactly **five main menu options**, as shown below:

```text
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice:
```

### Show Details Submenu

When the user selects option 4, this submenu appears:

```text
Choose details to show:
1. Person
2. Employee
3. Manager
Enter your choice:
```

## 🧠 OOP Concepts Used

| OOP Concept | Implementation |
|---|---|
| Class and Object | `Person`, `Employee`, `Manager`, `Developer` |
| Constructor | `__init__()` initializes object attributes |
| Destructor | `__del__()` is defined in the `Person` class |
| Encapsulation | Employee ID and salary are private attributes |
| Getter and Setter | Methods access and update private attributes |
| Inheritance | `Employee` inherits `Person`; `Manager` and `Developer` inherit `Employee` |
| Method Overriding | `display()` is redefined in derived classes |
| Method Overloading concept | `calculate_bonus()` uses `*args` for flexible arguments |
| `super()` | Calls the parent class constructor |

> **Note:** Python does not provide traditional method overloading by defining multiple methods with the same name. This project demonstrates flexible arguments with `*args`.

## 🗂️ Project Structure

```text
OOP_Wrapper_Project/
│
├── main.py
└── README.md
```

## ▶️ How to Run the Project

1. Install Python 3.
2. Open the project folder in VS Code or Python IDLE.
3. Open `main.py`.
4. Run the program.

Or run this command in the terminal:

```bash
python main.py
```

## 🖥️ Sample Output

### 1. Create a Person

```text
Enter your choice: 1

Enter Name: John Doe
Enter Age: 30

Person created with name: John Doe and age: 30
```

### 2. Create an Employee

```text
Enter your choice: 2

Enter Name: Jane Smith
Enter Age: 28
Enter Employee ID: E123
Enter Salary: 50000

Employee created with name: Jane Smith age: 28 ID: E123 and salary: $ 50000.0
```

### 3. Create a Manager

```text
Enter your choice: 3

Enter Name: Alice Johnson
Enter Age: 40
Enter Employee ID: M456
Enter Salary: 80000
Enter Department: Sales

Manager created with name: Alice Johnson age: 40 ID: M456 salary: $ 80000.0 and department: Sales
```

### 4. Show Employee Details

```text
Enter your choice: 4

Choose details to show:
1. Person
2. Employee
3. Manager
Enter your choice: 2

Employee Details:
Name: Jane Smith
Age: 28
Employee ID: E123
Salary: $ 50000.0
```

### 5. Show Manager Details

```text
Enter your choice: 4

Choose details to show:
1. Person
2. Employee
3. Manager
Enter your choice: 3

Manager Details:
Name: Alice Johnson
Age: 40
Employee ID: M456
Salary: $ 80000.0
Department: Sales
```

### 6. Exit

```text
Enter your choice: 5

Exiting the system.
Goodbye!
```

## 📚 Class Structure

- **Person:** Stores the person's name and age.
- **Employee:** Inherits from `Person` and stores private employee ID and salary.
- **Manager:** Inherits from `Employee` and adds a department.
- **Developer:** Inherits from `Employee` and adds a programming language. It is defined in the code to demonstrate inheritance and method overriding, but is not included as a creation option in the five-option main menu.

## 📝 Assumptions and Limitations

- The main menu has exactly five options to match the practical instructions.
- The Show Details submenu displays Person, Employee, or Manager records.
- The Developer class is included in the source code, but the menu does not create Developer objects.
- Records are stored in Python lists while the program is running.
- Records are not permanently saved; they are cleared when the program exits.
- The program expects valid numeric input for age and salary.

## ✅ Conclusion

This project demonstrates important Python OOP concepts through a basic Employee Management System. It provides a menu-driven way to create and display Person, Employee, and Manager records while illustrating constructors, encapsulation, inheritance, method overriding, and the use of `super()`.

---

<div align="center">

**Developed by: Prince Shah**  
**Guided by: Girish Gondaliya**

*Python OOP Practical Project*

</div>
