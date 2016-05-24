

a=['a','b','c','a','a']
b=[]
prev=None
for i in a:
    if i != prev:
        b.append(i)
        prev=i
print b

'''
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
    
    '''