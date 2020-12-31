
STACK = []
top = -1
max_size = 5

def push(element):
	global top
	global max_size
	if top == max_size-1:
		print("Stack Overflow")
	else:
		top+=1
		STACK.append(element)
		print(element," added")

def pop():
	global top
	global max_size
	if top == -1:
		print("Stack Underflow")
	else:
		item = STACK.pop()
		top-=1
		print(item," removed")

def display():
	global top
	global max_size
	if top == -1:
		print("Empty Stack !!!")
	else:
		for i in STACK:
			print(i,end=" ")

while True:
	print("1: Push")
	print("2: Pop")
	print("3: Display")
	print("4: Exit")

	choice = int(input("Enter Choice: "))


	if choice==1:
		element = int(input("Enter element: "))
		push(element)
	elif choice==2:
		pop()
	elif choice==3:
		display()
	elif choice==4:
		#break
		exit(0)
	else:
		print("Wrong Input, Try Again !!!")



