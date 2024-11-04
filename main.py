my_dict = {'Arnold':1960,'Yuri':1970,'Dug':1980}
print('Dict: ',my_dict)
print('Existing value: ',my_dict.get('Arnold'))
print('Not existing value: ',my_dict.get('Chuck'))
my_dict.update({'Paul':1965,'Karina':1975})
del my_dict['Dug']
print('Modified dictionary: ',my_dict)
print()
my_set  = {3,'apple', 3, True}
print('Set: ',my_set)
my_set.add(False)
my_set.add((0,1))
print('Modified set: ',my_set)
