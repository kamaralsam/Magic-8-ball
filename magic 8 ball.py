import random
random_number = random.randint(1,12)
name = "Jay"
question = "Should I change careers?"
answer = random_number



print(random_number)

if random_number == 1:
  answer = "Yes- definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
   answer = "Without a doubt"
elif random_number == 4:
  answer= "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "I don't care"
elif random_number == 11:
  answer = "Ask your momma"
elif random_number == 12:
  answer = "Pay first"
else:
  answer = "Error"

if name =="":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

if question == "":
  print("Ask a question")
else:
  print("Magic 8-Balls answer:" + answer)


