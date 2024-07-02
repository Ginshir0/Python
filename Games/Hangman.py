import random

words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry",
    "strawberry", "tangerine", "watermelon", "apricot", "blueberry", "cantaloupe",
    "dragonfruit", "grapefruit", "huckleberry", "jackfruit", "kumquat", "lime",
    "melon", "papaya", "pineapple", "rhubarb", "starfruit", "tamarind", "ugli fruit",
    "boysenberry", "cranberry", "guava", "lychee", "persimmon", "pomegranate",
    "blackberry", "currant", "gooseberry", "mulberry", "passionfruit", "rambutan",
    "soursop", "kiwifruit", "lingonberry"
]

gameOver = False
selectedWord = random.choice(words)
displayWord = []

for letter in selectedWord:
    displayWord.append("_")

print(selectedWord)
print()


#while not gameOver:
