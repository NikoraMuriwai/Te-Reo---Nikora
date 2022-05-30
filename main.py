#Welcome 
print ("Kia Ora, Ko Wai Tou Ingoa? / Hello, What Is Your Name")
name = input()
print ("Nau Mai Haere Mai / Welcome " + name)

#Chances
chances = 1
print("You Will Have", chances ,"Chance To Answer Correctly")

#Score
score = 0

#question 1
question_1 = print("1) What Is the Te Reo word For Ocean?")
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
question_2 = print("1) What Is the Te Reo word For Left?")
options_2 = print("A) Pounamu | B) Poaka | C) Maui | D) None Of The Above")
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