
array=[1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
lis=0
for item in array:
    lis2=array.count(item)
   
    if lis2>lis:
        im=item
        lis=lis2
print array.count(im)  