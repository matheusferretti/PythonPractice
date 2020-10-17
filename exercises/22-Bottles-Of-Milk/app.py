def number_of_bottles():
    for i in reversed(range(0, 100)):
        if i == 1:
            print(str(i) + " bottle of milk on the wall, " + str(i) + " bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
        elif i == 0:
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            print(str(i) + " bottles of milk on the wall, " + str(i) + " bottles of milk. Take one down and pass it around, " + str(i - 1) + " bottles of milk on the wall.")

number_of_bottles()