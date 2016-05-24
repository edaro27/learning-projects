#orders names in form: Bart, Maggie & Jenna
names=([{'name':'Bart'}, {'name': 'Maggie'}])
if names==[]:
    print ''
if len(names)==1:
    o=names[0]['name']
    print o
i=list()
for name in names:
    i.append(name['name'])
    
str1= ', '.join(i[:-1])
str2= str1+' & '+i[-1]
print str2

'''
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
'''