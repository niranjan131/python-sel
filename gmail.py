import sys
import re

if len(sys.argv)<=1:
	raise Exception("args not provided")
	
n=sys.argv[1]
if re.match('(\W|^)[\w.+\-]*@gmail\.com',n):
	print("gmail is validated")
	
else:
	print("gmail is not validated")

