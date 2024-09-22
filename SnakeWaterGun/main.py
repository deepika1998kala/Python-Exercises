import random
list = ["Snake", "Water", "Gun"]
chance=5
myScore=0
computerScore=0
for i in range(chance):
    myChoice = str(input("Enter your choice in Snake, Water or Gun "))
    computerChoice = random.choice(list)
    print("Computer'/s Choice: ", computerChoice)
    print("My Choice: ",myChoice)
    if((computerChoice == "Snake" and  myChoice == "Water") or (computerChoice == "Water" and  myChoice == "Gun") or (computerChoice == "Gun" and  myChoice == "Snake")):
        computerScore=computerScore+1
    elif((computerChoice == "Snake" and  myChoice == "Gun") or (computerChoice == "Water" and  myChoice == "Snake") or computerChoice == "Gun" and  myChoice == "Water"):
        myScore=myScore+1
print("Computer'/s Score: ",computerScore)

print("Your Score", myScore)

if(myScore > computerScore):
    print("!You won")
elif(myScore < computerScore):
    print("!Computer won")
else:
    print("Draw")
