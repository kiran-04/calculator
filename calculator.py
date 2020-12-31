import math
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. power")
print("6. square root")


choice = int(input("enter option"))
if choice in [1,2,3,4,5]:

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
		try:
			z=x/y
			print("division is:", z)
		except ZeroDivisionError:
			print("division by error")
	elif choice==5:
		z= math.pow(x,y)
		print("power is:", z)
elif choice==6:
	x = int(input("Number: "))
	z=math.sqrt(x)
	print("square root:", z)
		
else:
	print("wrong input")