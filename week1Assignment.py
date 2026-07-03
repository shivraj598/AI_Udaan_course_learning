# 1. it display the welcome message at Top
print("Welcome to DPLMS Student Registration System")
print("---------------------------------------------")

# 2. its is a list of courses.
courses = ["Python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]

# 3. for loop for course print
print("Available Courses:")
for course in courses:
    print("- " + course)
print("---------------------------------------------")

# 4. this block of code is used to take input from the user for student registration details.
name = input("Enter Student Name: ")
email = input("Enter Email: ")
age = input("Enter Age: ")
selected_course = input("Enter Selected Course: ")

# 5. this store the student details in a dictionary
student_details = {
    "Name": name,
    "Email": email,
    "Age": age,
    "Selected Course": selected_course
}
print("---------------------------------------------")

# 6 & 7. check if course is available or not and print the registration status
if selected_course in courses:
    print("Registration Successful!")
else:
    print("Course Not Available.")

print("---------------------------------------------")

# 8. final print of successful and not successful of registration of student.
print("STUDENT REGISTRATION DETAILS")
print("---------------------------------------------")
print("Name: " + student_details["Name"])
print("Email: " + student_details["Email"])
print("Age: " + student_details["Age"])
print("Selected Course: " + student_details["Selected Course"])
print("---------------------------------------------")
