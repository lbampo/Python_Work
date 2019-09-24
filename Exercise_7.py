film_rating = input("What is the film rating?\ ").lower().strip()

if film_rating == "universal":
    print("everyone can watch")
elif film_rating == 'pg':
    print("General viewing, but some scenes may be unsuitable for young children")
elif film_rating == '12':
    print(" 12, Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
elif film_rating == '12a':
    print("12A, o one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
elif film_rating == '15':
    print("15, No one younger than 15 may see a 15 film in a cinema.")
elif film_rating == '18':
    print("18, No one younger than 18 may see an 18 film in a cinema.")
else:
    print(" This print statement is invalid (universal, pg, 12, 12a, 15, 18)")




