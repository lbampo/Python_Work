# Homework (23/09/2019)
#
# Use variables, print abn different data types
# ask and store: Name, last_nmame, age, age_of_mother, 3 skills

fname = input("Please input your first name: ")
lname = input("Please input your last name: ")
age = int(input("Please input your age: "))
mother_age = int(input("Please input your mothers age: "))
skill_1 = input("What is your first amazing skill?")
skill_2 = input("What is your second amazing skill?")
skill_3 = input("What is your third amazing skill?")

age_difference = int(mother_age - age)

# Print out information a formatted matter
# Work out age between response and mother

print(f'Hello {fname.capitalize()} {lname.capitalize()}!\n It looks like your age is {age}, and your mothers age is {mother_age}.\n So according to my calculations.. the difference in your age is: {age_difference}')


# Store skill sets in list
skillset = [skill_1, skill_2, skill_3]
#print(skillset)

# Print each skill in a formatted way
print(f'\n \n WOOOOOOW, so you are telling me your skill is {skill_1}? \n And not only that.. but also {skill_2} and {skill_3} as well? \n God definitely took his time with you \n \n You Single?')