# Student Record Manager

A simple and beginner-friendly **Python-based Student Record Manager** that allows users to add student information, validate email addresses, store records in a text file, and retrieve saved student records through a terminal-based menu.

## 📌 Project Overview

The **Student Record Manager** is a console application developed using Python. It demonstrates fundamental programming concepts such as:

* Functions
* Conditional statements
* Loops
* File handling
* Exception handling
* Regular expressions
* User input validation

Student records are stored in a local `students.txt` file, allowing previously entered information to be retrieved whenever the program is executed.

## ✨ Features

### 1. Add Student

Allows the user to enter:

* Student ID
* Student Name
* Email Address

The entered information is validated before being saved.

### 2. Email Validation

The project uses Python's built-in `re` module and a Regular Expression to validate the email format.

Example:

```text
preethi@gmail.com
```

Invalid email formats are rejected with an appropriate error message.

### 3. File Storage

Student information is stored in:

```text
students.txt
```

The program uses **append mode (`"a"`)**, so adding a new student does not remove previously stored records.

### 4. Read Student Records

The application can retrieve all previously stored student records from the text file and display them in a structured format in the terminal.

### 5. Exception Handling

The program handles different types of invalid input and errors, including:

* Invalid Student ID
* Invalid menu choice
* Empty student name
* Invalid email format
* Missing student file
* Unexpected runtime errors

## 🛠️ Technologies Used

| Technology         | Purpose                                    |
| ------------------ | ------------------------------------------ |
| Python             | Core programming language                  |
| `re` Module        | Email validation using Regular Expressions |
| Text File (`.txt`) | Storing student records                    |
| VS Code            | Development environment                    |
| Git & GitHub       | Version control and project hosting        |

## 📂 Project Structure

```text
Student-Record-Manager/
│
├── student_record_manager.py
├── students.txt
└── README.md
```

> `students.txt` is created automatically when the first student record is added.

## ⚙️ How It Works

The application displays a menu with three options:

```text
====================================
       STUDENT RECORD MANAGER
====================================
1. Add Student
2. Read Student Records
3. Exit
====================================
```

### Add Student Flow

```text
User enters Student ID
        ↓
User enters Student Name
        ↓
User enters Email
        ↓
Validate Name
        ↓
Validate Email using Regex
        ↓
Save record to students.txt
```

### Read Records Flow

```text
Select "Read Student Records"
        ↓
Open students.txt
        ↓
Read stored records
        ↓
Split each record
        ↓
Display Student ID, Name & Email
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your system.

Check the installation using:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 3: Open the Project

Open the project folder in **Visual Studio Code**.

### Step 4: Run the Program

Open the VS Code terminal and execute:

```bash
python student_record_manager.py
```

## 💻 Sample Usage

### Adding a Student

```text
Enter your choice: 1

Enter Student ID: 101
Enter Student Name: Preethi
Enter Email: preethi@gmail.com

Student details saved successfully!
```

### Reading Student Records

```text
Enter your choice: 2

========== STUDENT RECORDS ==========
Student ID : 101
Name       : Preethi
Email      : preethi@gmail.com
-------------------------------------
```

### Invalid Email

```text
Enter Email: preethi@gmail

Error: Invalid email format.
```

### Invalid Menu Input

```text
Enter your choice: 5

Invalid choice. Please enter 1, 2, or 3.
```

## 📚 Python Concepts Demonstrated

This project provides practical implementation of several Python concepts:

* **Variables** – storing student information
* **Functions** – organizing program functionality
* **`if-elif-else`** – decision making
* **`while` loop** – continuous menu execution
* **`try-except`** – exception handling
* **File handling** – reading and writing student records
* **Regular Expressions** – email validation
* **String methods** – `strip()` and `split()`
* **Formatted strings** – storing records using f-strings
* **Modules** – importing and using the `re` module

## 🎯 Learning Objectives

Through this project, the following practical skills are demonstrated:

* Building a menu-driven Python application
* Accepting and validating user input
* Working with text files
* Handling common programming errors
* Using Regular Expressions for data validation
* Organizing code into reusable functions
* Developing a simple command-line application

## 🔮 Future Enhancements

The project can be extended in the future by adding:

* Search student by ID or name
* Update existing student records
* Delete student records
* Prevent duplicate Student IDs
* Store additional student information
* Use CSV or a database such as MySQL
* Add a graphical user interface
* Add sorting and filtering functionality

## 👩‍💻 Author

**Preethi Ahalya**

Computer Science & Engineering Student

Interested in Python, Artificial Intelligence, Generative AI, SQL, and Software Development.

## 📄 License

This project is created for **learning and educational purposes**.
