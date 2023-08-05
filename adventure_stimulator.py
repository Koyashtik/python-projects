name = input("What is your name? ")
print("Hello, ",name ,"welcome to this adventure stimulator. In this stimulator I will create a fascinating story for you, and only for you. You can call me 'Mark', your story telling friend. I will ask you a bunch of questions before we proceed.")
print("Shall I?")
permission = input("Yes or No? ")
if permission == "Yes":

 like = input("What do you like ")
 hate = input("What do you don't like ")
 friend= input("Who is your best friend ")
 father= input("What is your father's name ")
 mother= input("What is your mother's name ")
 bad_friend= input("Who is the friend you don't like? ")
 print()
 print("Lets generate the story now")
 print()
 print(name," really likes",like,". However, it is",hate," that she hates most.",name," is daughter of",father," and",mother,". She really likes her friend",friend," but has not so good opinion about ",bad_friend)
else:
 print()
 print("So sad that you don't want to hear the story")
print()
print("I am signing off now, goodbye")

