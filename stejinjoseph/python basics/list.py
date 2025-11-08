my_list=["apple","bannana","mango"]
for name in my_list:
    if name!="bannana":
        print(name)


num=[10,20,30,40]
print(num)

mixed=["hello",99,3.14,True]
print (mixed)

empty_list=[]
print(len(empty_list))


fruit=["apple","banana","mango", "cheery"]
fruit_item=fruit[0]
print("first item:",fruit_item)
fruit_item=fruit[1]
print("second item:",fruit_item)
fruit_item=fruit[2]
print("third item:",fruit_item)
fruit_item=fruit[3]
print("fourth item:",fruit_item)


last_item_alt=fruit[-1]
print("last item alt:",last_item_alt)


fruits=["apple","bannana","mango", "cherry"]

fruits[1]="blueberry"
print(fruits)

fruits[-1]="KIWI"
print(fruits)

fruit[0]="GRAPE"
print(fruits)


fruit=[]
fruit.append("apple")
fruit.append("banana")
fruit.append("mango")
print(fruit)


fruit.insert(1,"orange")
print(fruit)

fruit.extend(["mango","kiwi"])
print(fruit)


item=["apple","bannana","mango","kiwi"]
revers=[]
for i in range(len(item)-1,-1,-1):
    revers.append(item[i])

print(revers)


