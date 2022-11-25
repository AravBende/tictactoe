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

    print("  1 2 3")
    for i in range(3):
        print(i, *oxo[i])

    winorlose = input("did anyone win?(y/n): ")
    if winorlose.upper() == "Y":
        win = True
    else:
        win = False
