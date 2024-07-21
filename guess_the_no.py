import random
computer_no = random.randint(0,100)
tries = 20
print("Welcome to")
print("Guess the number!")
print("The no is b/w 0 & 100")
print("You have 20 tries!")
print("Lets start!")
while True:
    inp = int(input("Enter a no.: "))
    if inp < computer_no:
        tries = tries - 1
        if tries == 0:
            print("You ran out of tries!")
            print("The number was "+str(computer_no)+"!")
            break
        else:
            print("Too low!")
            print("You have "+str(tries)+" tries left!")
    elif inp > computer_no:
        tries = tries - 1
        if tries == 0:
            print("You ran out of tries!")
            print("The number was "+str(computer_no)+"!")
            break
        else:
            print("Too high!")
            print("You have "+str(tries)+" tries left!")
    else:
        print("You guessed it")
        print("correctly!")
        print("The number was "+str(computer_no)+"!")
        break