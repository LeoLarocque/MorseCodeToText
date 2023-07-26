print('This program will convert your morse code into text. Type "finished", if you are done typing in your code, so you can see the decrypted message. Also, when you are typing in your characters type a space before you press enter or it will not recognize it.\n')
morseDict = {
    "._ ": "A",
    "_... ": "B",
    "_._. ": "C",
    "_.. ": "D",
    ". ": "E",
    ".._. ": "F",
    "_ _. ": "G",
    ".... ": "H",
    ".. ": "I",
    "._ _ _ ": "J",
    "_._ ": "K",
    "._.. ": "L",
    "_ _ ": "M",
    "_. ": "N",
    "_ _ _ ": "O",
    "._ _. ": "P",
    "_ _._ ": "Q",
    "._. ": "R",
    "... ": "S",
    "_ ": "T",
    ".._ ": "U",
    "..._ ": "V",
    "._ _ ": "W",
    "_.._ ": "X",
    "_._ _ ": "Y",
    "_ _.. ": "Z",
    "/ ": " "
}
lst = []
x = 0
while 1 == 1:
    x += 1
    q = input("Enter " + str(x) + "ST character. ")
    if q == "._ ":
        print(morseDict["._ "])
        lst.append("A")
    elif q == "_... ":
        print(morseDict["_... "])
        lst.append("B")
    elif q == "_._. ":
        print(morseDict["_._. "])
        lst.append("C")
    elif q == "_.. ":
        print(morseDict["_.. "])
        lst.append("D")
    elif q == ". ":
        print(morseDict[". "])
        lst.append("E")
    elif q == ".._. ":
        print(morseDict[".._. "])
        lst.append("F")
    elif q == "_ _. ":
        print(morseDict["_ _. "])
        lst.append("G")
    elif q == ".... ":
        print(morseDict[".... "])
        lst.append("H")
    elif q == ".. ":
        print(morseDict[".. "])
        lst.append("I")
    elif q == "._ _ _ ":
        print(morseDict["._ _ _ "])
        lst.append("J")
    elif q == "_._ ":
        print(morseDict["_._ "])
        lst.append("K")
    elif q == "._.. ":
        print(morseDict["._.. "])
        lst.append("L")
    elif q == "_ _ ":
        print(morseDict["_ _ "])
        lst.append("M")
    elif q == "_. ":
        print(morseDict["_. "])
        lst.append("N")
    elif q == "_ _ _ ":
        print(morseDict["_ _ _ "])
        lst.append("O")
    elif q == "._ _. ":
        print(morseDict["._ _. "])
        lst.append("P")
    elif q == "_ _._ ":
        print(morseDict["_ _._ "])
        lst.append("Q")
    elif q == "._. ":
        print(morseDict["._. "])
        lst.append("R")
    elif q == "... ":
        print(morseDict["... "])
        lst.append("S")
    elif q == "_ ":
        print(morseDict["_ "])
        lst.append("T")
    elif q == ".._ ":
        print(morseDict[".._ "])
        lst.append("U")
    elif q == "..._ ":
        print(morseDict["..._ "])
        lst.append("V")
    elif q == "._ _ ":
        print(morseDict["._ _ "])
        lst.append("W")
    elif q == "_.._ ":
        print(morseDict["_.._ "])
        lst.append("X")
    elif q == "_._ _ ":
        print(morseDict["_._ _ "])
        lst.append("Y")
    elif q == "_ _.. ":
        print(morseDict["_ _.. "])
        lst.append("Z")
    elif q == "/ ":
        print(morseDict["/ "])
        lst.append(" ")
    elif q == "finished":
        code = str(lst)
        code2 = code.replace("'", "")
        code3 = code2.replace(",", "")
        print(code3)
        break
    elif q == "exit":
        print("Goodbye!")
        break
