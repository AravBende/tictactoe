oxo = [["#","#","#"],["#","#","#"],["#","#","#"]]
win = False

while win == False:
    print("  1 2 3")
    for i in range(3):
        print(i,*oxo[i])

    XorO = input("are you X or O? ")

    horizontal_input = int(input("Please input horizontal axis: "))

    verticle_input = int(input("Please input verticle axis: "))

    if oxo[verticle_input][horizontal_input-1] == "#":
        if XorO.upper() == "X":
            oxo[verticle_input][horizontal_input - 1] = "X"
        elif XorO.upper() == "O":
            oxo[verticle_input][horizontal_input - 1] = "O"
        else:
            print("this is not X or O")
    else:
        print("this space is already taken")

    print("  1 2 3")
    for i in range(3):
        print(i, *oxo[i])

    winorlose = input("did anyone win?(y/n): ")
    if winorlose.upper() == "Y":
        win = True
    else:
        win = False
