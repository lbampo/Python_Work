# Dictionaries

# Dictionaries are defined using {}
# They are organised with keys that point to values
#
## Contact FILIPE PAIVA will hold lots of info for this entry eg. phone number, work, email, address

dictionary_crazy_x = {
        'Carolina': 'She was actually nice',
        'Arthur': 'Drank way to much for my liking',
        'Lillian': 'Was definiteky a babe'
}

print(dictionary_crazy_x)

print(dictionary_crazy_x ['Arthur'])

#Adding new key pair value
dictionary_crazy_x['Kyle'] = 'Really likes monsters'

#Get out all the values

print(dictionary_crazy_x.values())

# Remove Item from dictionaru

dictionary_crazy_x.pop('Carolina')


# Better example of a Dictionary

crazy1 = {
        'name' : 'Frampton',
        'phone' : '07842715514',
        'address' : 'Dat place, where she lives',
        ' Known places to avoid' : [Milan, Paris, Hannover]
}