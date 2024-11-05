# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Rakshit,11/04/2024,Created Script and made changes to include Dictionaries
#   Rakshit,11/04/2024, Added structured error handling
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    print("Initial content of Enrollments.csv File is as follows:")
    for row in file.readlines():
        # Transform the data from the file
        student_data = row.split(',')
        if len(student_data) == 3:  # Only process rows with 3 columns
            student_data = {"FirstName": student_data[0], "LastName": \
student_data[1], "CourseName": student_data[2].strip()}
            # Load it into our collection (list of dictionaries rows)
            print(student_data)
            students.append(student_data)
        else:
            print(f"Skipping invalid row: {row.strip()}")
    file.close()
except FileNotFoundError:
    print(f"Error: The file {FILE_NAME} was not found.")
except IOError as e:
    print(f"Error: An IO error occurred while reading the file. {e}")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # Register a student
        try:
            #Error handling for first name
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
            #Error handling for last name
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
            # Check if course name is valid
            course_name = input("Please enter the name of the course: ")
            if not course_name:
                raise ValueError("Course name cannot be empty.")
            # Collected data added to a 2-D List of dictionary rows
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} \
{student_last_name} for {course_name}.")
            csv_data += f"{student_first_name},{student_last_name},\
{course_name}\n"
        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'{student["FirstName"]},{student["LastName"]},\
{student["CourseName"]}')
        print("\nThe collected data in a 2-D List of Dictionary Rows Format \
is as below:")
        print(students)
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":  # Save data to a file
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                try:
                    file.write(f'{student["FirstName"]},{student["LastName"]}, \
{student["CourseName"]}\n')
                except KeyError as e:
                    print(f"Error: Missing key {e} in student data while \
saving.")
            file.close()
            print("The following data was saved to file!")
            for student in students:
                try:
                    print(f'{student["FirstName"]},{student["LastName"]}, \
{student["CourseName"]}')
                except KeyError as e:
                    print(f"Error: Missing key {e} in student data \
while displaying.")
        except IOError as e:
            print(f"Error: An error occurred while saving to the file. {e}")
        except Exception as e:
            print(f"An unexpected error occurred while saving to \
the file: {e}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
