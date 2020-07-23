def parseBeliefs(line):
    try:
        belief = [float(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4])]
        return belief
    except:
        raise ValueError('The values of beliefs should be of type float')

def getInput():
    with open(sys.argv[1], "r") as file:
        lines, input = file.readlines(), []
        for ln in lines:
            if ln != '\n':
                ln, line = ln.split('\n')[0].split(' '), []
                for char in ln:
                    if char:
                        line.append(char)
                input.append(line)
    file.close()
    return input

def parseInput(input):
    if len(input) != 5 or len(input[0]) != 1 or len(input[1]) != 2 or len(input[2]) != 5 or len(input[3]) != 5 or len(input[4]) != 5:
        raise ValueError('Incorrect Format!')
    rollNum = input[0][0]
    try:
        x, y = float(input[1][0]), int(input[1][1])
        rollNum_toint = int(rollNum)
    except:
        raise ValueError('Roll number, x, y should be of type float or int')
    beliefs = []
    for i in range(3):
        beliefs.append(parseBeliefs(input[i + 2]))

    return rollNum, x, y, beliefs

def verifyXY(rollNum, x, y):
    tol = 0.01
    if abs(1 - (int(rollNum[-3:])%40 + 1)/100 - x) > tol or abs(int(rollNum[-2:])%3 - y) > tol:
        raise ValueError("Incorrect values of x, y")

def run():
    input = getInput()
    rollNum, x, y, beliefs = parseInput(input)
    verifyXY(rollNum, x, y)

    print("Roll Number : ", rollNum)
    print("x, y : ", x, y)
    print("Beliefs : ", beliefs)
    print("Parsed Succesfully!")
    return x, y, beliefs

def eval(x, y, beliefs):
    # HMMMM :P
    pass

if __name__ == "__main__":
    import sys
    x, y, beliefs = run()
    eval(x, y, beliefs)
