def greet():
    print("welcome to python functions")


greet()
greet()
greet()

def greet_user(name):
    print("welcome " , name)
greet_user("shanic")
greet_user("tamil")
greet_user("sanjiv")


def square(num):
    return num ** 2
result=square(100)
print(result)


def get_max(a,b):
    if a>b:
        return a
    else:
        return b

max_value=get_max(a=40,b=30)
print("maximum:",max_value)


def greet_user(name):
    print("welcome " , name)
name = ["alice","stejin","shanic","tamil","sanjiv"]
for name in name:
    greet_user(name)
