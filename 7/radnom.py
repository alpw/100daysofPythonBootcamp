
stages = ["""
    +-------+
    |       |
    |       |
    O       |
   /|\      |
   / \      |
            |
############+""",
"""
    +-------+
    |       |
    |       |
    O       |
   /|\      |
   /        |
            |
############+""","""
    +-------+
    |       |
    |       |
    O       |
   /|\      |
            |
            |
############+""",
 """
    +-------+
    |       |
    |       |
    O       |
   /|       |
            |
            |
############+""",
 """
    +-------+
    |       |
    |       |
    O       |
    |       |
            |
            |
############+""",
 """
    +-------+
    |       |
    |       |
    O       |
            |
            |
            |
############+""",
 """
    +-------+
    |       |
    |       |
            |
            |
            |
            |
############+"""]
import random

words = ["Akyurt", "Altındağ", "Ayaş", 'Balâ', 'Beypazarı', 'Çamlıdere', 'Çankaya', 'Çubuk', 'Elmadağ', 'Etimesgut', 'Evren', 'Gölbaşı', 'Güdül', 'Haymana', 'Kahramankazan', 'Kalecik', 'Keçiören', 'Kızılcahamam', 'Mamak', 'Nallıhan', 'Polatlı', 'Pursaklar', 'Sincan', 'Şereflikoçhisar', 'Yenimahalle']

theWord = random.choice(words).lower()

listWord = []
for _ in range(len(theWord)):
    listWord.append("_")
print(listWord)

health = len(stages)
while "_" in listWord and health > 1:
    inLetter = input("Type a letter: ")
    isTouched = False
    if inLetter in listWord:
        print("You've already tried this idiot")
        continue
    for index, letter in enumerate(theWord):
        if inLetter == letter:
            listWord[index] = letter
            isTouched = True
    if not isTouched:
        health -= 1
    


    print("""                           {}
{}      health = {}""".format(str(listWord).replace("', '"," "),stages[health-1],health-1))

if health > 1:
    print("""\n\n ...::: YO WIN BITTCH :::... \n\n""")
else:
    print("go and jerk off loser".upper())
    print(theWord)