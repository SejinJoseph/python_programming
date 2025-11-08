# Implicit Type Casting
x = 10 # int
y = 2.5 # float

sum = x + y # 10.0 + 2.5 = 12.5
print("Type of sum:", type(sum))

# Explicit Type Casting
value = "100" #string
num = int(value)
print("Type of num:", type(num))

f = float(value)
print("Type of f:", type(f))

price = 19.99
price_str = str(price)
print("Price: ", price_str)
print("Type of price_str:", type(price_str))