#snake water gun
print("Welcome to the Snake, Water, Gun game you have 10 chances")
chance = 10
Score_computer = 0
Score_user = 0
import random
trial = 0
try:
    while(trial < 10):
        SWG = ["S", "W", "G"]
        Computer = random.choice(SWG)
        User = input("Choose One Letter Between S ,W ,G \n")
        User = User.upper()

        if (Computer == "S" and User == "W") or (Computer == "W" and User == "G") or (Computer == "G" and User == "S"):
            print(" Match outcome = Computer won")
            Score_computer = Score_computer+1
        elif(User == "S" and Computer == "W") or (User == "W" and Computer == "G") or (User == "G" and Computer == "S"):
            print("Match outcome = Congratulations You Won ")
            Score_user = Score_user+1
        elif(User==Computer):
            print("Match outcome Its a draw")
        if (Score_user > Score_computer):
            print("You won", "Your Score:", Score_user,":", "Computer Score:", Score_computer)
        elif(Score_computer > Score_user):
            print("You lost","Computer Score:", Score_computer,":","Your Score", Score_user)
        else:
            print("Its a Tie","Your Score:", Score_user,":","Computer Score", Score_computer)
        trial = trial+1
        chance = chance - 1
        print("Chances Left", chance)
except Exception as e:
    print(e)
