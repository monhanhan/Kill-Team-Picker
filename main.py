def main():
    raw_list = readFile()

# Read the CSV file input
def readFile():
    in_file = open("TeamList.csv")
    raw_list = []

    for line in in_file:
        raw_list.append(line.split(", "))

    return raw_list

# Take the input from the file and process it into the arrays that will be output
def calculateValues(inputArray):
    pass

# generate the random values.
def generateRandom():
    pass

# actually pick the team given the random input
def pickTeam(teams, ranges, rand):
    pass

main()