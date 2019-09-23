# lists keep objects in order of index
# They are defined by []
# Lists are organised with index

# List name       = [   0      ,   1   ,    2    ,     3    ]
crazy_ex_partners = ['Carolina', 'JSON', 'Arthur', 'Tereece']

print(crazy_ex_partners)

print(type(crazy_ex_partners))

# Remove someone from the list (destroy one)


# Add someone to the list (create one)
print(crazy_ex_partners)
crazy_ex_partners.append('Serius Black')

crazy_ex_partners.insert(2, 'Tereece')

# Get particular record out of list (read one)

## First in list
print(crazy_ex_partners[0])

## Last in list
print(crazy_ex_partners[-1])

# Edit an entry

##Changing a record in a specific index

(crazy_ex_partners[3]) = 'LANA!! (...) DANGER!!!'
print(crazy_ex_partners)


# What happens when you have 36000 exes


#Mixed data list
#lists may have data types #
hybrid_list = ['This is a string', 12, 66, 'hello', [1,2,3], [1,2,2]]




#Tuples - Immutable lists(They do not change)

my_tuple = (2, 'hello', 22, 'more value')

print(my_tuple)
print(my_tuple[1])

