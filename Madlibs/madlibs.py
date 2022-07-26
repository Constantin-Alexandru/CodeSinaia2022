from time import sleep


def SET_COLOUR(colour: int):
    print("\x1b[{code:0}m".format(code=colour), end="")


def SET_MODE(mode: int):
    print("\x1b[{code:0}m".format(code=mode), end="")


def CLS():
    print("\x1b[H\x1b[J", end="")


if __name__ == '__main__':

    CLS()

    print("MADLIB PROJECT")

    print("Would you like the output on the screen? (Y/n):", end="")

    SET_COLOUR(32)
    screen = False
    if input().lower() == 'y':
        screen = True
    SET_COLOUR(37)

    print("Give me the path to the madlib you would like to play today: ", end="")

    SET_COLOUR(32)
    filename = input()
    SET_COLOUR(37)

    reader = open(filename, "r")

    contents = reader.read()

    startIndex: int = 0

    startIndexArr = []
    endIndexArr = []

    startIndex = contents.find("<")

    while startIndex != -1:
        endIndex = contents.find(">")

        startIndexArr.append(startIndex)

        madlib_help = contents[startIndex + 1:endIndex]

        print("Give me a/an " + madlib_help, end=": ")

        SET_COLOUR(31)
        SET_MODE(1)
        help = input()
        SET_MODE(22)
        SET_COLOUR(37)

        endIndexArr.append(startIndex + len(help))

        contents = contents[:startIndex] + help + contents[endIndex + 1:]

        startIndex = contents.find("<")

    if not screen:
        SET_COLOUR(0)

        output = open("output.txt", "w")

        output.write(contents)

        exit()

    i = 0

    startIndexArr.append(len(contents))

    print(contents[:startIndexArr[i]], end="")

    while i < len(startIndexArr) - 1:
        SET_MODE(1)
        SET_COLOUR(35)
        print(contents[startIndexArr[i]: endIndexArr[i]], end="")
        SET_COLOUR(0)

        print(contents[endIndexArr[i]: startIndexArr[i + 1]], end="")

        i += 1

    SET_COLOUR(0)
