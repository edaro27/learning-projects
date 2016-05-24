#print a.count(i)
n=2
a=[1,2,3,4,5,4,2,2,4,5,5,1,1,3,1,1,1,1,1]

b=[]

for i in a:
    st=b.count(i)
    if st<n:
        b.append(i)

print b

