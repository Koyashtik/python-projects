name= input("Hi, this is Be+, your affirmations generator. What shall I call you? ")
print("That's great",name,"let me ask you a few questions to proceed with. Shall I?")
permission = input()

if permission=="Yes":
  print("lets proceed")
  song= input("What is the song that you love " +name+" ? ")
  love= input("What is it that you love most doing "+ name+"? What is it that you would love to spend your day with? ")
  sport= input("What is it that you love to watch? ")
  singer= input("Who is your favorite singer? ")
  food= input("What is your best food? ")
  workout= input("Do you workout or do some exercise? ")
else:
  print=("That's so sad, i am signing off now")

mood= input("OK, let's start "+ name+" . How are you feeling today? Happy, sad, confused or motivated?")
if mood=="happy":
  print("That's so great to hear "+ name+" . Today, make sure to listen to some "+singer+" and do some "+ love+" . You are going to make this world very bright today "+ name)
elif mood== "sad":
  print("We all have bad days "+ name+" .Life is just a roller-coaster of some highs and lows. If there are some days of highs, then there will inevitably be some days of lows. Take a break today, listen to "+ song+" and some more of "+ singer+" .Maybe make some "+ food+" ,or you can just order it online anyways. Just spend your day watching some "+ sport)
  if workout== "Yes" or workout =="yes":
   print("Make sure to do some workout today too and also add meditation in that.")
  else:
    print("You must do some exercise today. Search in youtube for easy workout to do in home and follow it. Also search for mindfullness meditation and do it for sometime")
elif mood == "confused":
  print("No worries, we all have those days where we have no idea of what we are doing and what we will be doing "+name+" .Maybe listening to some "+singer+" might give you some clarity. If you have no clear idea of what to do, "+ love +"might be the best shot you can have.")
else:
  print("Oh, this is the day, we are gonna grind it. Eat some "+food+" and start "+love)
print()