import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dataDict = {letter[1]:word[1] for letter,word in zip(data["letter"].iteritems(), data["code"].iteritems())}



while 1:
    print([dataDict[letter.upper()] for letter in input("Type a word: ")])
