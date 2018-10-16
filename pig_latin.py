string = input()
wordList = string.split()
vowels = ["a", "e", "i", "o", "u", "y"]  # Put all vowels in a list to reduce number of if statements below.
latinWordList = []
for word in wordList:
    if word[0] in vowels:
        latinWordList.append(word + "yay")
    else:
        for x in range (0, len(word)-1):
            if word[x] in vowels:
                latinWordList.append(word[x:] + word[0:x] + "ay")
                print(word)
                break
for word in latinWordList:
    print(word, end =" ")
