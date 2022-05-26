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
question_1 = print("1) What Is Te Reo For Ocean?")
options_1 = print("A) Moana | B) Rangi | C) Papa | D) Moko")
answer_1 = "a"

for i in range (chances):
  answer = input("Answer: ")
  if (answer.lower() == answer_1):
    print ("Kai Pai" +name)
    score = score + 1
    break
else:
    print