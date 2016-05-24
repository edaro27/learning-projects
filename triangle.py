a=2
b=2
c=2
item=[a,b,c]
for i in item:
    if i<=0:
        print False

if (a+b)<=c or (a+c)<=b or (b+c)<=a:
    print False
print True