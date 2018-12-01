puzzleInputFile = open("day-1-puzzle-input.txt")
inputLines = list(line.strip() for line in puzzleInputFile)

answer = 0
found = False
items = set()

def determine_sign(line):
    if line.startswith("+"):
        return int(line[1:])
    return int(line[1:]) * -1

while not found:
    for line in inputLines:
        result = determine_sign(line)
        answer = answer + result
        if answer in items:
            print(answer)
            found = True
            break
        else:
            items.add(answer)
        

puzzleInputFile.close()
