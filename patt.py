n=int(input("Enter the numbr of rows:"))
for i in range(0,n):
	for j in range(0,i+1):
		print("*"+" "*(n-2*i)+"*",end=" ")
	print()

for i in range(0,n):
	for j in range(0,n-i):
		print("*",end=" ")
	print()




