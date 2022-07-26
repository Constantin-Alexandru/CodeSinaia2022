
from time import sleep


def SET_COLOUR(colour: int):
    print("\x1b[{code:0}m".format(code=colour), end="")


def SET_MODE(mode: int):
    print("\x1b[{code:0}m".format(code=mode), end="")


def CLS():
    print("\x1b[H\x1b[J")


if __name__ == '__main__':

    print("MADLIB PROJECT")

    print("Give me the path to the madlib you would like to play today: ", end="")

    SET_COLOUR(32)
    filename = input()
    SET_COLOUR(37)

    reader = open(filename, "r")

    contents = reader.read()

    startIndex: int = 0

    contents_size = len(contents)

    startIndex = contents.find("<")

    while startIndex != -1:
        endIndex = contents.find(">")

        madlib_help = contents[startIndex + 1:endIndex]

        print("Give me a/an " + madlib_help, end=" ")

        SET_COLOUR(31)
        SET_MODE(1)
        help = input()
        SET_MODE(22)
        SET_COLOUR(37)

        contents = contents[:startIndex] + help + contents[endIndex + 1:]

        startIndex = contents.find("<")

    output = open("output.txt", "w")

    output.write(contents)

    SET_COLOUR(0)
