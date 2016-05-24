str1="123"
str2="abc"
list=[]
j=0
while j<len(str1) or j<len(str2):
    if j<len(str1):
        list.append(str1[j])
    if j<len(str2):
        list.append(str2[j])
    j=j+1
print ''.join(list)