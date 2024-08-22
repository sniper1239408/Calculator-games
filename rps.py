import random
list1 = ["rock", "paper", "scissor"]
com_wins = 0
player_wins = 0
tie = 0
no_of_rounds = 0

def ban():
    clear_screen()
    print("YOU HAVE VIOLATED THE \nRULES OF RPS. \nYOU ARE BANNED FROM \nPLAYING!")

def clear_screen():
    print("\n" * 50)

def main():
    global no_of_rounds
    global com_wins
    global player_wins
    global list1
    global tie
    personchose = ""
    clear_screen()
    print("Welcome to RPS!")
    print("How many rounds would \nyou like to play?")
    no_of_rounds = int(input("Enter here: "))
    if not no_of_rounds > 0:
        ban()
        return
    clear_screen()
    for i in range(no_of_rounds):
        print("Round "+str(i+1))
        print("0 means Rock")
        print("1 means paper")
        print("2 means Scissor")
        print("Choose a no b/w 0 & 2")
        personno = eval(input("Enter a no: "))
        try:
            personchose = list1[personno]
        except:
            ban()
            return
        clear_screen()
        print("You chose "+personchose)
        comno = random.randint(0, 2)
        comchose = str(list1[comno])
        print("Com chose "+comchose)
        print("Press EXE to see \nwho wins!")
        _ = input()
        clear_screen()
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
            com_wins = com_wins+1
            print("Computer wins!")
        elif winner == "person":
            player_wins = player_wins+1
            print("You won!")
        elif winner == "tie":
            tie = tie + 1
            print("Its a TIE!")
    print("All rounds finished! \npress EXE to see the \nfinal results!")
    _ = input()
    clear_screen()
    print("Comp wins: "+str(com_wins))
    print("Player wins: "+str(player_wins))
    print("Ties: "+str(tie))
    if com_wins > player_wins:
        print("Computer wins!")
    elif com_wins < player_wins:
        print("Player wins!")
    else:
        print("Its a tie!")
    print("Thanks for playing!")
main()