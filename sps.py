import random
print("-"*40)
print("    \tSTONE/PAPER/SCISSOR  ")
print("-" * 40)
player = input("\nEnter Player Name : ")
for i in range(5):
    option = input("Enter Stone, Paper or Scissor : ")
    print("-" * 40)
    print(player," selected ",option)

    opt = ["Stone","Paper","Scissor"]
    coption = random.choice(opt)
    print("Computer selected ",coption)
    print("-" * 40)

    if option == "Paper":
        if coption == "Paper":
            print("IT IS A DRAW")
        elif coption == "Scissor":
            print("COMPUTER WINS")
        else:
            print(player," WINS")
    elif option == "Stone":
        if coption == "Stone":
            print("IT IS A DRAW")
        elif coption == "Paper":
            print("COMPUTER WINS")
        else:
            print(player," WINS")
    elif option == "Scissor":
        if coption == "Scissor":
            print("IT IS A DRAW")
        elif coption == "Stone":
            print("COMPUTER WINS")
        else:
            print(player," WINS")

