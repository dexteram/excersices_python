myArray = ["3", "-2", "x", "9", "0"]
if myArray[2] == "x":
    del myArray[2]
    myArray1 = []

    for x in myArray:
        if int(x) <= 10:
            myArray1.append(x)
            myArray1.sort(reverse=True)
    del myArray1[-1]
    print(myArray1)
            




