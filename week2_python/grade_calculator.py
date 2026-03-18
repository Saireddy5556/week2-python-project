# Student Grade Calculator

name = input("Enter student name: ")

while True:
    marks = int(input("Enter marks (0-100): "))
    
    if 0 <= marks <= 100:
        break
    else:
        print("Invalid marks! Try again.")

if marks >= 90:
    grade = "A"
    message = "Excellent!"
elif marks >= 80:
    grade = "B"
    message = "Very Good!"
elif marks >= 70:
    grade = "C"
    message = "Good!"
elif marks >= 60:
    grade = "D"
    message = "Keep Improving!"
else:
    grade = "F"
    message = "Try Again!"

print("\nResult for", name)
print("Marks:", marks)
print("Grade:", grade)
print("Message:", message)