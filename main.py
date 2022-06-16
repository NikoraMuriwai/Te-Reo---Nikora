#v1.9
#Te Reo Quiz 
#17/06/22
#made by Nikora Muriwai

#Welcome 
print ("Kia Ora, Ko Wai Tou Ingoa? / Hello, What Is Your Name")
name = input()
print ("Nau Mai Haere Mai / Welcome " + name)

#Chances
chances = 1
print("You Will Have", chances ,"Chance To Answer Correctly, Please Answer With The Following: A, B, C, D")

#Score
score = 0

#question 1
question_1 = print("1) What Is The Te Reo word For Ocean?")
options_1 = print("A) Moana | B) Rangi | C) Papa | D) Moko")
answer_1 = "a"

for i in range (chances):
  answer = input("Answer: ")
  if (answer.lower() == answer_1):
    print ("Ka Pai " +name)
    score = score + 1
    break
else:
    print("Hē / Incorrect")
    print("The Correct Answer Is Moana")

#question 2
question_2 = print("2) What Is the Te Reo word For Left?")
options_2 = print("A) Pounamu | B) Poaka | C) Maui | D) None")
answer_2 = "c"

for i in range (chances):
  answer = input("Answer: ")
  if (answer.lower() == answer_2):
    print ("Ka Pai " +name)
    score = score + 1
    break
else:
    print("Hē / Incorrect")
    print("The Correct Answer Is Maui")

#question 3
question_3 = print("3) What Is the Te Reo word For Right?")
options_3 = print("A) Pounamu | B) Hui | C) Iwi | D) None")
answer_3 = "d"

for i in range (chances):
  answer = input("Answer: ")
  if (answer.lower() == answer_3):
    print ("Ka Pai " +name)
    score = score + 1
    break
else:
    print("Hē / Incorrect")
    print("The Correct Answer Is None")

#question 4
question_4 = print("4) What Is the Te Reo word For Hungry?")
options_4 = print("A) Hiakai | B) Kai | C) Hākari | D): Whāngai")
answer_4 = "a"

for i in range (chances):
  answer = input("Answer: ")
  if (answer.lower() == answer_4):
    print ("Ka Pai " +name)
    score = score + 1
    break
else:
    print("Hē / Incorrect")
    print("The Correct Answer Is Hiakai")

#question 5
question_5 = print("5) What Is the Te Reo word For Love?")
options_5 = print("A) Whānau | B) Tautoko | C) Awhi | D) Aroha")
answer_5 = "d"

for i in range (chances):
  answer = input("Answer: ")
  if (answer.lower() == answer_5):
    print ("Ka Pai " +name)
    score = score + 1
    break
else:
    print("Hē / Incorrect")
    print("The Correct Answer Is Aroha")

#print the score
while score >= 5:
  print ("Tino Pai! Your Score Was", score)
  break

while score <=4:
  print ("Aroha Mai, Your Score Was", score ,"Better Luck Next Time")
  break

#Goodbye message
print("Nga Mihi " + name, "For Playing My Te Reo Quiz")