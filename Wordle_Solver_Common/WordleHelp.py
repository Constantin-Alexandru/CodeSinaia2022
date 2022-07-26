###
# Main code for WordleHelper program
# Implements the command loop and uses a CmdProcessor
# object to process each of the supported commands
import CmdProcessor as cp

wordsDic = {}

if __name__ == "__main__":

    reader = open("words.txt", 'r')

    lines = reader.readlines()

    for line in lines:
        pair = line.split()
        wordsDic[pair[0]] = int(pair[1])
    print("\x1b[33m[INFO] ", end="")
    print("\x1b[32mSuccessfully loaded {count} words".format(
        count=len(wordsDic)))
    print("\x1b[0m", end="")

    print("This is Wordle helper!")
    #cmdProcessor = cp.CmdProcessor()
    cmdProcessor = None
    line = input("Command?> ").lower()
    while(line != "quit" and line != "exit"):
        if line == "?" or line == "help":
            cmdProcessor.processHelp()
        elif line.startswith("add"):
            cmdProcessor.processAdd(line)
        elif line.startswith("match"):
            cmdProcessor.processMatch(line)
        elif line.startswith("reset"):
            cmdProcessor.processReset(line)
        elif line.startswith("stats"):
            cmdProcessor.processStats(line)
        elif line.startswith("config"):
            cmdProcessor.processConfig(line)
        elif line.strip():
            # Anything else which is not an empty string
            # is a command which is not supported
            print("#Error: Command not recognized")
        line = input("Command?> ").lower()
    print("Goodbye!")
