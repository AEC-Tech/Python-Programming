import time
data =[['1','2','3'],['4','5','6'],['7','8','9']]
for i in range(3):
    print("_"*18)
    for j in range(3):
        print("| ",data[i][j],end='  ')
    print("|")
print("_"*18)

p1 = input("Enter Name Player 1 : ")
p2 = input("Enter Name Player 2 : ")
turn = 1
while True:
    if turn % 2 == 1 :
        print(p1 +"'s Turn")
        pos = input("Enter the position to place X : ")
        for i in range(3):
            for j in range(3):
                if data[i][j] == pos:
                    data[i][j] = 'X'
    else:
        print(p2+"'s Turn")
        pos = input("Enter the position to place O : ")
        for i in range(3):
            for j in range(3):
                if data[i][j] == pos:
                    data[i][j] = 'O'
    turn += 1

    time.sleep(2)
    for i in range(3):
        print("_" * 18)
        for j in range(3):
            print("| ", data[i][j], end='  ')
        print("|")
    print("_" * 18)
    time.sleep(2)
    if data[0][0] == data[0][1] == data[0][2]:
        if data[0][0] == "X":
            print("Player 1 ",p1," WINS !!!!")
        else:
            print("Player 2 ", p2, " WINS !!!!")
        break
    elif data[1][0] == data[1][1] == data[1][2]:
        if data[1][0] == "X":
            print("Player 1 ",p1," WINS !!!!")
        else:
            print("Player 2 ", p2, " WINS !!!!")
        break
    elif turn > 9:
        print("It is a draw")
        break