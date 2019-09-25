import time

# While loops
# Keeps looping and iterating until a condition is met

# while <condition>
     # block


# while <condition>
    #block
    #if <condition>
      #break

# while True :
#     print('qwerty')
#     time.sleep(1)


# counter = 0
#
# while True:
#     print("qwerty2")
#     if counter >= 10:
#         break
#     counter += 1


# while True:
#     print("How you doing? (Joey Voice): ")
#     U_input = input().lower()
#
#     if U_input == "nope":
#         break
#     elif U_input == 'cute':
#         print("Shes feeling you, carry on")
#     else:
#         print("Don't worry mumma still loves you")


# user_input = input("Do you want to talk about it? (yes/no) : ").lower().strip()
# while user_input == 'yes':
#     print("Nice, lets talk then")
#     break
# else:
#     print("That's fine, come and talk to me when you're ready")
#

cars = ['volvo', 'skoda', 'ferrari', 'Lambo']

counter = 0
max_len = len(cars)

while counter < max_len:
    print(counter +1, '-', cars[counter])
    counter += 1
