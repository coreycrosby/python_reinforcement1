documentary = "Fyre Festival"
drama = "12 years a slave"
comedy = "The Hangover"
dramedy = "Easy A"

print("On a scale from 1-5 rate the following")
print("Documentaries")
doc_option = int(input())
print("Dramas")
drama_option = int(input())
print("Comedies")
com_option = int(input())

if doc_option >= 4 and doc_option > drama_option and doc_option > com_option:
    print("You should watch {}!".format(documentary))

elif doc_option <=3 and drama_option >=4 and com_option >=4:
    print("You should watch {}!".format(dramedy))

elif drama_option >=4 and drama_option > doc_option and drama_option > com_option:
    print("You should watch {}!".format(drama))

elif com_option >=4 and com_option > doc_option and com_option > drama_option :
    print("You should watch {}!".format(comedy))

elif doc_option <=3 and drama_option <=3 and com_option <=3:
    print("You should read the book Gone Girl!")
