
employees=[{'last_name': 'Hepburn', 'first_name': 'Ollie', 'role': 'Boss'}, {'last_name': 'Smith', 'first_name': 'Morty', 'role': 'Truck Driver'}, {'last_name': 'Ross', 'first_name': 'Peter', 'role': 'Warehouse Manager'}, {'last_name': 'Neil', 'first_name': 'Cal', 'role': 'Sales Assistant'}, {'last_name': 'Saunders', 'first_name': 'Jesse', 'role': 'Admin'}, {'last_name': 'Jones', 'first_name': 'Anna', 'role': 'Sales Assistant'}, {'last_name': 'Hamm', 'first_name': 'Carmel', 'role': 'Admin'}, {'last_name': 'Sparks', 'first_name': 'Tori', 'role': 'Sales Manager'}, {'last_name': 'Jones', 'first_name': 'Peter', 'role': 'Warehouse Picker'}, {'last_name': 'Smith', 'first_name': 'Mort', 'role': 'Warehouse Picker'}, {'last_name': 'Bell', 'first_name': 'Anna', 'role': 'Admin'}, {'last_name': 'Bell', 'first_name': 'Jewel', 'role': 'Receptionist'}, {'last_name': 'Brown', 'first_name': 'Colin', 'role': 'Trainee'}]
test='Jesse Saunders'
coun=list()
i=0

#While loop extracts full name and adds to a list
while i<len(employees):
    a= employees[i].values()[0]
    b= employees[i].values()[1]
    i+=1
    str=' '.join([a,b])
    coun.append(str)

if test in coun:
    ind=coun.index(test)
    print employees[ind].values()[2]
else: print 'Does not work here!'

'''
def find_employees_role(name):
    
    for employee in employees:
        if employee['first_name'] + ' ' + employee['last_name'] == name:
            return employee['role']
        
    return "Does not work here!"
    '''