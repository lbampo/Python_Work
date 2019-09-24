# If statements
# (Control Flow) - Controls where the code is going to go depending on the result of
# -                 the evaluations that return true/false.


# if <condition>
    # block
# elif <condition>
    # block
# else:
    # block

# weather = 's'
#
# if weather == 'rainy':
#     print('Take an umbrella')
# elif weather == 'snowy':
#     print('Wrap up warm')
# else:
#     print('Wear shorts')

age = 22
driver_license = True

if (age > 18) and (driver_license == True):
    print("You can drink and drive")
elif (age >= 18) and (driver_license == False):
    print("You better get learning")
if (age > 0) and (age <= 16):
    print(" You can't legally drink, but your friends will help")
elif (age > 18) :
    print("You can vote")
elif (driver_license == True):
    print("You can drive")
else:
    print("Youre too young go back to school")




