# Stupid School Teacher

response = input("As your teacher I will always be smarter than you, what do you think: ")

count = 0

while response != 'Im a doctor':
    while (count <= 1 - 1):
        count += 1
        if '?' in response[-1:]:
            print("HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!")

        elif '!' in response[-1:]:
            print(" YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!")

        else:
            print("Go back to school!")


    response2 = input("have you actually got anything smart to say?").lower().strip()
    if '?' in response2[-1:]:
        print("HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!")

    elif '!' in response2[-1:]:
        print(" YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!")

    elif response2 == 'im a doctor':
        print("WELLL DONE! YOU can now talk to me")
        break
    else:
        print("Nice catch up, bye then")
        break
else:
    print("WELLL DONE! YOU can now talk to me")