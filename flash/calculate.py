print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")


choice = int(input("enter option"))
x= int(input("first number"))
y= int(input("second number"))

if choice==1:
	z=x+y
	print("Addition is:", z)
elif choice==2:
	z=x-y
	print("subtraction is:", z)
elif choice==3:
	z=x*y
	print("multiplication is:", z)
elif choice==4:
	z=x/y
	print("division is:", z)
else:
	print("wrong input")