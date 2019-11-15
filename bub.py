l=[2,42,3,67,5,6,88]
for i in range(0,len(l)-1):
	 for j in range(i+1,len(l)-1):
		if(l[i]>l[i+1]):
			l[i],l[i+1]=l[i+1],l[i]	
print("sorted:",l)	
