f = open("story.txt")
content = f.readlines()
for line in content:
    for word in line.split(" "):
        print(word,end='#')
    print()

f.close()

