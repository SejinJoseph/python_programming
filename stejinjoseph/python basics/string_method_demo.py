original="HELLO WORLD"
lowered=original.lower()
print("the lower case:",lowered)

uppered=original.upper()
print("uppercase:",uppered)

messy="      python      "
cleaned=messy.strip()
print("after strip",cleaned)


text="java is powerful"
update=text.replace("java","python" )
print("after update:",update)

sentence="python is easy to learn"
words=sentence.split()
print("split result",words)


text="learning python is fun"
position=text.find("python")
print("found at index",position)

heading="welcome to python programming"
formatting=heading.title()
print("Title case",formatting)


msg="hello world"
cleaned=msg.capitalize()
print("capitalize result",cleaned)

greeting="hello everyone"
print(greeting.startswith("hello"))
print(greeting.endswith("world"))
print(greeting.find("world"))