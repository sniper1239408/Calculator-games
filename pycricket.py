import random
#jnsm
who_won_toss = 0
batbowl_list = ["bowl", "bat"]
com_choice = 0
added_val = 0
added_val2 = 0
bat_or_bowl = ""
some_int = 5

def ban():
    clear_screen()
    print("YOU HAVE VIOLATED THE \nRULES OF PYCRICKET. \nYOU ARE BANNED FROM \nPLAYING!")

def clear_screen():
    print("\n" * 50)

def main():
    global who_won_toss
    global batbowl_list
    global com_choice
    global added_val
    global added_val2
    global bat_or_bowl
    global some_int
    #print("SONY CALCULATOR ENTERTAINMENT")
    #print("           PRESENTS")
    clear_screen()
    
    print("WELCOME TO PY-CRICKET \nVERSION 1.3 \nChoose Odd Or Even. \n0 for even\n& 1 for odd.")
    player_choice = int(input("Enter no: "))
    if player_choice > 1 or player_choice < 0:
        ban()
        return
    if player_choice == 1:
        com_choice = 0
    else:
        com_choice = 1
    clear_screen()

    print("Choose a random no. \nb/w 0 and 6 & \nenter it in.")
    number = int(input("Enter no: "))
    
    if number > 6 or number < 0:
        ban()
        return

    odd_or_eve = random.randint(0,6)
    toss_result = number + odd_or_eve
    if toss_result % 2 == 1:
        if player_choice == 1:
            who_won_toss = 0
        else:
            who_won_toss = 1
    else:
        if player_choice == 0:
            who_won_toss = 0
        else:
            who_won_toss = 1
    clear_screen()
            
    if who_won_toss == 0:
        print("YOU WON THE TOSS! \nChoose 0 to bowl \nor 1 to bat")
        bat_or_bowl_int = int(input("Enter no: "))
        try:
            bat_or_bowl = batbowl_list[bat_or_bowl_int]
        except:
            ban()
            return
        clear_screen()
        print("You've chosen to "+bat_or_bowl)
        if bat_or_bowl == "bat":
            some_int = 0
        else:
            some_int = 1

    else:
        print("YOU LOST THE TOSS.")
        bat_or_bowl_int = random.randint(0, 1)
        bat_or_bowl = batbowl_list[bat_or_bowl_int]
        print("The computer has \nchosen to "+bat_or_bowl)
        if bat_or_bowl == "bowl":
            some_int = 0
        else: 
            some_int = 1

    if some_int == 0:
        print("GAME STARTED \nEnter no. b/w 0 & 6")
        while True:
            inp = int(input("Enter no: "))
            if inp > 6 or inp < 0:
                ban()
                return
            com_inp = random.randint(0,6)
            print("Computer: "+str(com_inp))
            added_val = added_val + inp
            if inp == com_inp:
                clear_screen()
                print("YOU ARE OUT. \nTHE COMP NEEDS \n"+str(added_val + 1)+" TO WIN")
                break
        while True:
            inp = int(input("Enter no: "))
            if inp > 6 or inp < 0:
                ban()
                return
            com_inp = random.randint(0,6)
            print("Computer: "+str(com_inp))
            added_val2 = added_val2 + com_inp
            if added_val2 >= added_val + 1:
                print("YOU LOSE!")
                break
            elif inp == com_inp:
                print("COMP IS OUT \nYOU WON!")
                break
    else:
        print("GAME STARTED \nEnter no. b/w 0 & 6")
        while True:
            inp = int(input("Enter no: "))
            if inp > 6 or inp < 0:
                ban()
                return
            com_inp = random.randint(0,6)
            print("Computer: "+str(com_inp))
            added_val = added_val + com_inp
            if inp == com_inp:
                clear_screen()
                print("COMP IS OUT. YOU NEED \n"+str(added_val + 1)+" TO WIN")
                break
        while True:
            inp = int(input("Enter no: "))
            if inp > 6 or inp < 0:
                ban()
                return
            com_inp = random.randint(0,6)
            print("Computer: "+str(com_inp))
            added_val2 = added_val2 + inp
            if added_val2 >= added_val + 1:
                print("YOU HAVE WON!")
                break
            elif inp == com_inp:
                print("YOU ARE OUT! \nYOU LOSE!")
                break
    print("Do you want to play \nagain? \nPress EXE for yes \nAC for no.")
    eee = input()
    main()
main()