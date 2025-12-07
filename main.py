def main():
    raw_list = read_file()
    ranges = calculate_values(raw_list)

# Read the CSV file input
def read_file():
    in_file = open("TeamList.csv")
    raw_list = []

    for line in in_file:
        raw_list.append(line.strip().split(", "))

    in_file.close()
    return raw_list

# Take the input from the file and process it into the arrays that will be output
def calculate_values(raw_list):
    ranges = []
    total = 0

    for i in range (len(raw_list)):
        played = int(raw_list[i][1])
        val = 1
        if played < 10:
            val = 10 - played
            
        if raw_list[i][2] == 'y':
            val = val * 2

        ranges.append(val)
        total += val

    ranges[0] = ranges[0] / total

    for i in range (1, (len(ranges))):
        ranges[i] = ranges[i] / total + ranges[i-1]

    return ranges

# generate the random values.
def generate_random():
    pass

# actually pick the team given the random input
def pick_team(teams, ranges, rand):
    pass

main()