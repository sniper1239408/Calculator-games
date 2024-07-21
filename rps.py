import random
list1 = ["rock", "paper", "scissor"]
print("Welcome to RPS!")
print("0 means Rock")
print("1 means paper")
print("2 means Scissor")
print("Choose a no b/w 0 & 2")
personno = eval(input("Enter a no: "))
personchose = ""
personchose = list1[personno]
print("You chose "+personchose)
comno = random.randint(0, 2)
comchose = str(list1[comno])
print("Com chose "+comchose)
winner = ""

if comchose == personchose:
    winner = "tie"
elif personchose == "rock":
    if comchose == "scissor":
        winner = "person"
    elif comchose == "paper":
        winner = "computer"
elif personchose == "paper":
    if comchose == "rock":
        winner = "person"
    elif comchose == "scissor":
        winner = "computer"
elif personchose == "scissor":
    if comchose == "paper":
        winner = "person"
    elif comchose == "rock":
        winner = "computer"

if winner == "computer":
    print("Computer wins!")
elif winner == "person":
    print("You won!")
elif winner == "tie":
    print("Its a TIE!")
print("Thanks for playing!")