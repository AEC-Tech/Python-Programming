import time
import random
movies = ["DIL BECHARA","RADHE","SARDAR DA GRANDSON","URI","ASPIRANTS"]
hint = ["aaaa","bbbb","ccccc","dddddd","eeee"]
m = random.randint(0,4)
movie = movies[m]
print("HINT ", hint[m])
guess = [' ']
h = "HANGMAN"
while True:
    print("=" * 20)
    print("\t",h)
    print("=" * 20)
    dash = False
    for ch in movie:
        if ch in guess:
            print(ch,end=' ')
        else:
            print("_",end=' ')
            dash = True
    if dash == False:
        print ("YOU WIN !!!!")
        break
    print()
    print("=" * 20)
    g = input("Enter the Guess Alphabet ")
    if len(g) != 1:
        print("Please Enter single alphabet only ")
        continue
    if not g.isalpha():
        print("No symbol, digit or space is acceptable")
        continue
    g = g.upper()
    if g not in movie:
        h = h[:len(h)-1]
        if len(h) == 0:
            print("YOU LOOSE, GAME OVER !!!")
            break
    guess.append(g)
    time.sleep(2)