
def loadGame():
    print("Hi! Let's play mad libs :-)")

    for dot in "." * 10:
        print(dot)

loadGame()

def play():
    print("Give me ...")

    firstNoun = input("a noun: ")
    secondNoun = input("another noun: ")
    thirdNoun = input("a plural noun:")
    firstPlace = input("A place: ")
    firstAdjective = input("An adjective: ")

    madlibsTemplate = "I went to my {} and got {}. Then, I got a {} and put it in my {}. I wish someody could take care of my {} stuff and sleep with it. It will be really {} am I right?".format(firstNoun,thirdNoun,secondNoun,firstNoun,secondNoun,firstAdjective)
    print(madlibsTemplate)

play()
