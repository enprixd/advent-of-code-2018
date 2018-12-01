puzzleInput = open("day-1-puzzle-input.txt")

answer = 0

def determine_sign(line):
    if line.startswith("+"):
        return int(line[1:])
    return int(line[1:]) * -1

for line in puzzleInput:
    result = determine_sign(line)
    answer = answer + result
    print("Total: " + str(answer))

puzzleInput.close()
