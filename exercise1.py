documentary = "Fyre Festival"
drama = "12 years a slave"
comedy = "The Hangover"
dramedy = "Easy A"

print("Do you enjoy \n1. documentaries\n2. dramas \n3. comedies? \nChoose 1 for documentaries, 2 for dramas, 3 for comedies, 2 and 3 for dramas and comedies.")
user_options = input()

if user_options == "1":
    print("You should watch {}!".format(documentary))

elif user_options == "2":
    print("You should watch {}!".format(drama))

elif user_options == "3":
    print("You should watch {}!".format(comedy))

elif user_options == ("2 and 3"):
    print("You should watch {}!".format(dramedy))

else: print("You should read the book Gone Girl!")






