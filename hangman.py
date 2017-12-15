import random

file = open("slova.txt")
words = file.read().strip().split("\n")
file.close()

word = random.choice(words)
show = ["_"] * len(word)

for index, value in enumerate(word):
    if value in {" ", ",", ".", "-"}:
        show[index] = word[index]

file = open("hangman.txt")
images = file.read().rstrip().split("\n\n")

lives = len(images) - 1

def print_hangman():
    print()
    print(images[len(images) - 1 - lives])
    print(" ".join(show))
    print()

while lives > 0 and show.count("_") > 0:
    print_hangman()
    guess = input("Hádej písmeno: ")

    if len(guess) == 1 and guess not in {"", " ", ",", ".", "-", "_"}:
        if guess in word:
            for index, value in enumerate(word):
                if value == guess:
                    show[index] = word[index]
        else:
            lives -= 1
    else:
        print("# špatný vstup")

print_hangman()

if lives == 0:
    print("PROHRÁL JSI! Bylo to '{}'.".format(word))
else:
    print("JSI BOREC...")
