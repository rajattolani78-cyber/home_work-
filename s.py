#-------------random die roll 
# import random 
# while True:
#     i = input("if you want to play press 'enter', if you want to quit press 'q':  ")
#     if i == 'q':
#         print("Thank you!")
#         break
#     elif i == '':
#         print(random.randint(1,6))
#-------------find word by letter
# random_words = ["india3","idonasia","japan","inderpresh","sunio","prestige","procetion","iodine","iron"]
# finder_word  = input("enter the word you want to find in dic: ")
# cont = 0
# ra_output = []
# for i in random_words:
#     if i[0]== finder_word:
#         cont = cont + 1
#         ra_output.append(i)
# print(f"the number of output present in the dic {cont}, the output that is matches your word {ra_output}")
#-------------number guess game
# secreat_number = random.randint(1,90)
# attampts = 10

# while attampts >= 1:
#     user_input = int(input("a guess number between (1 to 90): "))
#     if user_input == secreat_number:
#         print("you made it")
#         break
#     else:
#         print (f"you have {attampts} left")
#         if user_input < secreat_number:
#             print ("try a higher number")
#         else:
#             print("try lower number")
#     attampts-=1
# print (f"GAME OVER,the seacreat number was {secreat_number}")
for i in range (6,0-1,):
    for j in range (i):
          print("*",end = " ")
    print()