#checking if string is palindrome
str="toyota"
j=1
k=0
c=0
for k,i in enumerate(str):
    while j<=len(str):
        a=str[k:j]
        j=j+1
        b=a[::-1]
        if a==b and len(a)>c:
            c=len(a)
            d=a
    j=0
if len(d)>1:
    print d