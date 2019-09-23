# Homework 2 23/09/2019
#
# Define an empty dictionary eg name_dict = {}


# Prompt user for input for a story
print("Tell me your story \n")

hero_name = input("What was the name of the hero?:")
s_beginning = input("What happened in the beginning?")
s_middle = input("woooooooow thats mad, then what?")
s_end = input("I seeee, so tell me.. what happenned in the end?")
s_moral = input("Alright most importantly, what did you learn?")

#     : Hero, beginning, middle , end + 3 other things you define to add to story
#     : add each response  to dictionary under approproate key

story_dict = {
    'hero': hero_name.capitalize(),
    'beginning': s_beginning,
    'middle': s_middle,
    'end': s_end,
    'moral': s_moral
}
#
# Print out dictionary info in formatted way
print('\n This story is about {hero}. \n \n {beginning} and then {middle}. \n In the end {end} \n \n The moral of this story is {moral} '.format_map(story_dict))

