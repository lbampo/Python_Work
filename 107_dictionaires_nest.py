# Nested lists and dictionaries
#
# nested_list = ['bread', 'sugar', [1, 2, 3, 4, 'spice', {'name': 'Buttercup', 'age': '46'}]]
#
#
# variable_spice = nested_list[2][4]
#
# variable_dict_name = nested_list[2][5]['name']
#
# print(variable_spice)
# print(variable_dict_name)
#
#

student_1 = {
        'name': 'Arya Stark',
        'stream': 'Many Faces',
        'grade': 10,
        'complete modules': ['sword', 'augmented senses', 'no face', 'warrior']
}

students = {
    'studen1': student_1,
    'studen2': {
        'name': 'Johnny English',
        'stream': 'Spy Training',
        'grade': 3.5,
        'complete modules': ['relaxation']
}

}

print(students['studen1']['name'])
print(students['studen2']['name'])