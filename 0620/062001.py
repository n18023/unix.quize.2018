moko = 1
while moko < 100:
    if moko % 15 == 0:
        print("FIZZBUZZ")
    elif moko % 3 == 0:
        print("FIZZ")
    elif moko % 5 == 0:
        print("BUZZ")
    else:
        print(moko)
    moko = moko + 1 
