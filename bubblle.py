l=[2,543,54,36,758,867]
"""
    bubble sort 
    
    algorithm
    
"""


for j in range(len(l)-1):
  for i in range(len(l)-1):
    if l[i]>l[i+1]:
      l[i],l[i+1]=l[i+1],l[i]
print("Sorted list:",l)
