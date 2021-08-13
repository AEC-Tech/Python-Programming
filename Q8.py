def countWords():
    '''
    Function to read a text file and count
    how many words starts with A
    :return:
    '''
    f = open("sample.txt","r")
    cnt = 0
    words = f.read().split()
    for w in words:
        if w[0] in 'aA':
            print(w)
            cnt += 1
    f.close()
    print("No. of words starting with A are ",cnt)

countWords()
