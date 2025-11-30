import random

user_score = 0
PC_score = 0
run = True

# step 1
options = ["s", "k", "q"]

while run:

    # step 2
    print("\033[34ms:snag, k:kaqas, q:qeichi\033[0m")
    user_choice = input("Az bein mavared yeki ro entekhab kon \n")

    PC_choice = random.choice(options)
    print(f"PC choice: {PC_choice}")

    # step 4
    if PC_choice == user_choice:
        print("\033[33mmosavi, dobare bazi kon \033[0m")
    elif user_choice == "s":
        if PC_choice == "q":
            print("\033[32mindasto bordi\033[0m")
            user_score+=1
        if PC_choice == "k":
            print("\033[31mindasto bakhti\033[0m")
            PC_score+=1
    elif user_choice == "k":
        if PC_choice == "s":
            print("\033[32mindasto bordi\033[0m")
            user_score+=1
        if PC_choice == "q":
            print("\033[31mindasto bakhti\033[0m")
            PC_score+=1
    elif user_choice == "q":
        if PC_choice == "k":
            print("\033[32mindasto bordi\033[0m")
            user_score+=1
        if PC_choice == "s":
            print("\033[31mindasto bakhti\033[0m")
            PC_score+=1
    
    #sharte tamam
    if user_score == 3 or PC_score == 3:
        if user_score == 3:
            print("\033[42mbazi ro bordid\033[0m")
        else:
            print("\033[41mbazi ro bakhtid\033[0m")
        break
    else:
        print(f"shoma: {user_score} computer: {PC_score} =>  berim daste badi")