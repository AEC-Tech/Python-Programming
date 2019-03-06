import math
def generateSQ(N):

    for a in range(100, N+1):
        print(math.sqrt(a))

def main():
    N= int(input("Enter N : "))
    generateSQ(N)

main()




