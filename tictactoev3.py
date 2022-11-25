
oxo = [["#","#","#"],["#","#","#"],["#","#","#"]]

win = False

XorO = True

while win == False:
    print("  1 2 3")
    for i in range(3):
        print(i,*oxo[i])



    horizontal_input = int(input("Please input horizontal axis: "))

    verticle_input = int(input("Please input verticle axis: "))

    if oxo[verticle_input][horizontal_input-1] == "#":
        if XorO == True:
            oxo[verticle_input][horizontal_input - 1] = "X"
            XorO = False
        elif XorO == False:
            oxo[verticle_input][horizontal_input - 1] = "O"
            XorO = True
    else:
        print("this space is already taken")


    if oxo[0] == ["O", "O", "O"] or oxo[1] == ["O", "O", "O"] or oxo[2] == ["O", "O", "O"]:
        print("O won!")
        break
    elif oxo[0][0] and oxo[1][0] and oxo[2][0] == "O":
        print("O won!")
        break
    elif oxo[0][1] and oxo[1][1] and oxo[2][1] == "O":
        print("O won!")
        break
    elif oxo[0][2] and oxo[1][2] and oxo[2][2] == "O":
        print("O won!")
        break
    elif oxo[0][0] and oxo[1][1] and oxo[2][2] == "O":
        print("O won!")
        break
    elif oxo[0][2] and oxo[1][1] and oxo[2][0] == "O":
        print("O won!")
        break

    if oxo[0] == ["X", "X", "X"] or oxo[1] == ["X", "X", "X"] or oxo[2] == ["X", "X", "X"]:
        print("X won!")
        break
    elif oxo[0][0] and oxo[1][0] and oxo[2][0] == "X":
        print("X won!")
        break
    elif oxo[0][1] and oxo[1][1] and oxo[2][1] == "X":
        print("X won!")
        break
    elif oxo[0][2] and oxo[1][2] and oxo[2][2] == "X":
        print("X won!")
        break
    elif oxo[0][0] and oxo[1][1] and oxo[2][2] == "X":
        print("X won!")
        break
    elif oxo[0][2] and oxo[1][1] and oxo[2][0] == "X":
        print("X won!")
        break
