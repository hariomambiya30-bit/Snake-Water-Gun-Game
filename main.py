import random 
'''
 1 = snake
 -1 = water
 0 = gun
 '''
while True:
    computer = random.choice([0, 1, -1])
    youstr = input("Enter your choice: ")
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0:"Gun"}

    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
    if(computer == you):
       print("Its a Draw")
       continue

    else:
        if(computer ==-1 and you == 1):
           print("You win!")
           continue

        elif(computer ==-1 and you == 0):
            print("Computer win!")
            break

        elif(computer ==1 and you == -1):
            print("Computer win!")
            break

        elif(computer ==1 and you == 0):
            print("You win!")
            continue

        elif(computer == 0 and you == 1):
            print("computer win!")
            break

        elif(computer == 0 and you == -1):
            print("You win!")
            continue