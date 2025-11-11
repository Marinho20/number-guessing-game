# imports
import random


dificuldades = ["easy", "medium", "hard", "insane", "custom"]
tries = 1


# função numero aleatorio
def newnumber(b):
    cnumber = random.randint(1, b)
    return cnumber


# region SCORES
# função ler scores
def readscores():
    lscores = []
    with open("scores.txt", "r") as f:
        for line in f:
            parts = line.split("=")
            if parts[1].strip() == "None":
                scores = None
                lscores.append(scores)
            else:
                scores = int(parts[1].strip())
                lscores.append(scores)

    return lscores


def printscores(lscores):
    dificulties = ["easy", "medium", "hard", "insane"]
    print("scores:")
    for i in range(4):
        print(f"{dificulties[i]}= {lscores[i]}")


def newscores(dif, lscores):
    # defenição do current score
    if dif == "easy":
        a = 0
        cscore = lscores[a]
    if dif == "medium":
        a = 1
        cscore = lscores[a]
    if dif == "hard":
        a = 2
        cscore = lscores[a]
    if dif == "insane":
        a = 3
        cscore = lscores[a]
    if dif == "custom":
        a = 4
        cscore = lscores[a]

    if cscore == None:
        lscores[a] = tries
    else:

        if tries < cscore:
            lscores[a] = tries

    return lscores


def writescores(lscores):
    dificulties = ["easy", "medium", "hard", "insane","Custom"]
    with open("scores.txt", "w") as f:
        for i in range(5):
            f.write(f"{dificulties[i]} = {lscores[i]}\n")


# endregion


# region DIFICULTIES
def printdif():
    print(
        "dificulties: \n easy mode -> numbers betwen 1 and 50 \n medium mode-> numbers betwen 1 and 100 \n hard mode-> numbers betwen 1 and 500 \n insane mode-> numbers betwen 1 and 1000 \n custom mode -> you chose"
    )


def chosedif():

    dif = input("choose game dificulty:")

    while dif not in dificuldades:
        dif = input("invalid option chose again:")

    if dif == "easy":
        ncorreto = newnumber(50)
        limite = 50
        print("you chose easy dificulty")

    if dif == "medium":
        ncorreto = newnumber(100)
        limite = 100
        print("you chose medium dificulty")

    if dif == "hard":
        ncorreto = newnumber(500)
        limite = 500
        print("you chose hard dificulty")

    if dif == "insane":
        ncorreto = newnumber(1000)
        limite = 1000
        print("you chose insane dificulty")

    if dif == "custom":
        a = int(input("chose the max number:"))
        ncorreto = newnumber(a)
        limite = a
        print("you chose custom dificulty")

    return ncorreto, limite, dif


# endregion


# region PLAYFUNCITON
def play(ncorreto, limite):
    global tries
    tries = 0

    ntried = int(input("choose a number:"))

    if ntried > limite or ntried < 1:
        ntried = int(input("invalid number try again:"))

    if ntried > ncorreto:
        print(f"the correct number is lower than {ntried}")

    if ntried < ncorreto:
        print(f"the correct number is higher than {ntried}")

    while ntried != ncorreto:
        ntried = int(input("wrong number try again: "))

        if ntried > limite or ntried < 1:
            ntried = int(input("invalid number try again:"))

        if ntried > ncorreto:
            print(f"the correct number is lower than {ntried}")

        if ntried < ncorreto:
            print(f"the correct number is higher than {ntried}")

        tries = tries + 1
    print(f"congrats you guessed the number in {tries} tries")
    return tries


# endregion


# region MENU
def pmenu():
    choice = int(
        input("\nMENU:\n 1-> Play Game\n 2-> View Leader Board\n 3-> Exit\n choice:")
    )
    return choice


# endregion

a = pmenu()


# region principal while
while a != 3:
    if a == 1:
        yn = "Y"
        while yn == "Y":
            printdif()
            scores = readscores()
            ncorreto, limite, dif = chosedif()
            play(ncorreto, limite)
            newscores(dif, scores)
            writescores(scores)
            tries = 1
            yn = input("wanna play again(Y/N):")
            while yn not in ("Y", "N"):
                yn = input("Invalid choice. Choose Y or N: ")

    elif a == 2:
        scores = readscores()
        printscores(scores)

    else:
        print("invalid option try again:")

    a = pmenu()

# endregion
