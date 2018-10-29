# Welcomes player to the game
def loadGame():
    print("Hi! Let's play mad libs :-)")

    # prints 10 dots for the user to have a starting game experience
    for dot in "." * 10:
        print(dot)

def play():
    print("Give me ...")

    # English compounds for player to answer
    firstNoun = input("a noun: ")
    secondNoun = input("another noun: ")
    thirdNoun = input("a plural noun:")
    firstPlace = input("A place: ")
    firstAdjective = input("An adjective: ")

    # Injects English compounds values into the template below
    madlibsTemplate = "I went to my {} and got {}. Then, I got a {} and put it in my {}. I wish someody could take care of my {} stuff and sleep with it. It will be really {} am I right?".format(firstNoun, thirdNoun, secondNoun, firstNoun, secondNoun, firstAdjective)
    print(madlibsTemplate)

loadGame()
play()
