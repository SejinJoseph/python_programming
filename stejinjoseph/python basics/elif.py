score =int(input("Enter your score:"))

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")

role =str(input("who are you?"))

if role == "admin":
    print("Welcome, Admin!")
elif role == "editor":
    print("Welcome, Editor!")
elif role == "viewer":
    print("Welcome, Viewer!")
else:
    print("Unknown role")
