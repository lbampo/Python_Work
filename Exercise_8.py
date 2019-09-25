# POP and TOC

# multiple of 3 are POP
# multiple of 5 are TOC
# multiple of 3 and 5 are POPTOC

input_que = (input("Would you like to play this game?: "))

count = 0

while input_que != 'no':

    input_num = int(input("Input your special number: "))
    while count < (input_num ):
        count += 1
        if ((count % 3 == 0) and (count % 5 == 0)):
            print("POPTOC")
        elif (count % 3 == 0):
            print('POP')
        elif(count % 5 == 0):
            print("TOC")
        else:
            print(count)
    print('\n')
    input_que2 = input("Do you want to continue playing?:").lower().strip()

    if input_que2 != 'no':
        print('cool')
        count = 0

    else:
         print("You have exited the game")
         break

else:
    print("You have exited game")

