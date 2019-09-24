# cars = ['Skoda Felicia FUN', 'Fiat Panda 4x4', 'Mustang Ford', 'Corvette']
#
# # syntax
#
# # For <placeholder> in <iteratable>:
#     #block of code
#     #indented
#
# # for car in cars:
# #     print(car)
#
#
# embedded_list = [['Felipe', 'Francis'], ['Moustapha', 'David', 'Gillian']]
#
# for data in embedded_list:
#     print(data)
#     for name in data:
#         print(name)


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
        'complete modules': ['relaxation']}
}
#


print( students['studen1']['name'],('\n'),  students['studen1']['stream'])

# # ---------------------------------------------------
# n = 0
# for key in student_1:
#     n += 1
#     print((n), '-', key, ':', student_1[key] )
#
# print('\n')
#
# # ----------------------------------------------------
# n1 = 0
# for key in students['studen2']:
#     n1 += 1
#     print ((n1), '-', key, ':', students['studen2'][key])



