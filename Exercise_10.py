# Story Book

book_1 = {
    'name' : 'The life of Breezy',
    'beginning' : 'Its not easy',
    'middle' : 'Being Breezy',
    'end' : 'Hence why we we should get freaky',
    'hero' : 'L-Breezy'
}

book_2 = {
    'name' : 'Wisdom',
    'beginning': 'Open the door, close the door I am so confused',
    'middle' : 'Lost in friction of life',
    'end' : 'I havent read a dictionary in my life',
    'hero' : 'Michael Kyle Jnr'
}

book_3 = {
    'name' : 'Deeper Meaning',
    'beginning' : 'Why are we here?',
    'middle' : 'Have we been put on earth to fulfill a specific role by God',
    'end' : 'What is my purpose?',
    'hero' : 'My Soul'
}

book_shop = {
    'first_book': book_1,
    'second_book': book_2,
    'third_book': book_3
}

book_shop1 = book_shop['first_book']
book_shop2 = book_shop['second_book']
book_shop3 = book_shop['third_book']

read_book = input("Would you like to read this book?: ").lower().strip()

while read_book != 'no':
    book_choose = int(input("What book do you want yo read?(1,2,3): "))
    if book_choose == 1:
        print(f"This story is about: {book_shop1['hero']} \n \n "
              f"{book_shop1['beginning']} \n {book_shop1['middle']} \n {book_shop1['end']}")

    elif book_choose == 2:
        print(f"This story is about: {book_shop2['hero']} \n \n "
              f"{book_shop2['beginning']} \n {book_shop2['middle']} \n {book_shop2['end']}")

    elif book_choose == 3:#
        print(f"This story is about: {book_shop3['hero']} \n \n "
              f"{book_shop3['beginning']} \n {book_shop3['middle']} \n {book_shop3['end']}")


    input_2 = input("Do you want to read another story?").lower().strip()
    if input_2 != 'no':
        print("Noice")
    else:
        print("Fair, but try and read more")
        break

else:
    print('Fair, but try to read more')


