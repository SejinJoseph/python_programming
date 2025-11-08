# this is a program to calculate simple intrest

print("this is to find the intrest amount and total amount")

principal_amount = float(input("Enter the principal value:"))
rate_of_intrest = float(input("Enter the rate of intrest per year:"))
time = float(input("Enter the year :"))

simple_intrest = (principal_amount * rate_of_intrest * time) / 100
total_amount = principal_amount + rate_of_intrest

print("simple_intrest=", int(simple_intrest))
print("total_amount=", int(total_amount))
