def duplicateString(s):
    s.lower()
    freq=[None]*len(s)
    for i in range(0,len(s)):
        freq[i]=1
        for j in range(i+1,len(s)):
            if (s[i]==s[j]):
                freq[i]=freq[i]+1
                s=s[:j]+'0'+s[j+1:]
        for i in range(0,len(freq)):
            if(s[i]=s[j] and s[i]!=' '):
                print(s[i]+'-'+str(freq[i]))
s="Great responsibility"
print("\n\nDuplicate characters in a given string:")
duplicateString(s)