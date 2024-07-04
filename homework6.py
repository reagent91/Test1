my_dict={'Alexey':1995,'Natalia':1997, 'Nail': 1991}
print(my_dict)
print(my_dict['Alexey'])
print(my_dict.get('Luka'))
my_dict.update({'Evgenii':1980,
                'Roman':1985})
print(my_dict)
tatar=my_dict.pop('Nail')
print(tatar)
print(my_dict)

my_set={34,42,34,42,54,34,True,False,'fruits', 77.54}
print(my_set)
my_set.add(86)
my_set.add('vegetables')
print(my_set)
my_set.remove(54)
print(my_set)