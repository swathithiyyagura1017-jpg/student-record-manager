# ---------------------------------------------------------
# Student Record Manager
# Module 2 Assignment
# ---------------------------------------------------------

# Import the 're' module for Regular Expression
# It is used to validate the email address.
import re


# Name of the text file where student details will be stored
FILE_NAME = "students.txt"


# ---------------------------------------------------------
# Function to validate email
# ---------------------------------------------------------
def validate_email(email):

    # Regular Expression pattern for checking email format
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    # Return True if email matches the pattern
    # Otherwise, return False
    return re.match(pattern, email) is not None


# ---------------------------------------------------------
# Function to add a student
# ---------------------------------------------------------
def add_student():

    try:
        # Get Student ID from the user through terminal
        student_id = int(input("Enter Student ID: "))

        # Get Student Name
        name = input("Enter Student Name: ").strip()

        # Get Email
        email = input("Enter Email: ").strip()

        # Check whether name is empty
        if name == "":
            raise ValueError("Student name cannot be empty.")

        # Validate the email using Regular Expression
        if not validate_email(email):
            raise ValueError("Invalid email format.")

        # Open the text file in append mode
        # 'a' means new data will be added without deleting old data
        with open(FILE_NAME, "a") as file:

            # Write student details into the text file
            file.write(f"{student_id},{name},{email}\n")

        # Display success message
        print("\nStudent details saved successfully!")

    # Handle invalid input such as entering text instead of a number
    except ValueError as e:
        print("\nError:", e)

    # Handle any other unexpected errors
    except Exception as e:
        print("\nSomething went wrong:", e)


# ---------------------------------------------------------
# Function to retrieve student details
# ---------------------------------------------------------
def read_students():

    try:
        # Open the text file in read mode
        # 'r' means we only want to read the data
        with open(FILE_NAME, "r") as file:

            # Read all lines from the file
            records = file.readlines()

        # Check whether the file contains any records
        if not records:
            print("\nNo student records found.")
            return

        # Display heading
        print("\n========== STUDENT RECORDS ==========")

        # Read each student record
        for record in records:

            # Remove extra spaces and newline
            record = record.strip()

            # Split the data using comma
            student_id, name, email = record.split(",")

            # Display student details
            print("Student ID :", student_id)
            print("Name       :", name)
            print("Email      :", email)
            print("-------------------------------------")

    # Handle the situation when the text file does not exist
    except FileNotFoundError:
        print("\nNo student file found.")

    # Handle any other errors
    except Exception as e:
        print("\nError while reading file:", e)


# ---------------------------------------------------------
# Main function
# ---------------------------------------------------------
def main():

    # Keep displaying the menu until the user chooses Exit
    while True:

        print("\n====================================")
        print("       STUDENT RECORD MANAGER")
        print("====================================")
        print("1. Add Student")
        print("2. Read Student Records")
        print("3. Exit")
        print("====================================")

        try:
            # Get menu choice from the user
            choice = int(input("Enter your choice: "))

            # If user chooses 1, add student
            if choice == 1:
                add_student()

            # If user chooses 2, retrieve students
            elif choice == 2:
                read_students()

            # If user chooses 3, exit the program
            elif choice == 3:
                print("\nThank you! Program ended.")
                break

            # If user enters any other number
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")

        # Handle non-numeric menu input
        except ValueError:
            print("\nInvalid input! Please enter a number.")


# ---------------------------------------------------------
# Start the program
# ---------------------------------------------------------
main()