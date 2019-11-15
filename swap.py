str1="Good"
str2="morning"
str1=str1+str2
str2=str1[0:(len(str1)-len(str2))]
str1=str1[len(str2):]

print("strings after swapping:"+ str1+" "+ str2)
