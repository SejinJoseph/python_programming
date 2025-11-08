name=input("Enter your name:")
print("hello " + name+"!")

age=int(input("Enter your age:"))
age1=age+1
print("you will be",
      age1,
      "next year..")

price =float(input("Enter your price:"))
discount=price * 0.1
print("discount is",discount)

answer =input("are you a student? yes or not :")
is_student= answer=="yes"
if is_student:
    print("welcome student")
else:
    print("hello guest")
