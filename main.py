import random

def main():
    print()
    raw_list = read_file()
    ranges = calculate_values(raw_list)
    random = generate_random()
    
    print()
    print(random)
    print()

    selection = pick_team(ranges, random)
    print(raw_list[selection][0])
    print()

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

    print_list = []

    for i in range (len(raw_list)):
        played = int(raw_list[i][1])
        val = 1
        if played < 10:
            val = 10 - played
            
        if raw_list[i][2] == 'y':
            val = val * 2

        ranges.append(val)
        print_list.append([raw_list[i][0], val])
        total += val

    ranges[0] = ranges[0] / total

    print(print_list[0], ranges[0])

    for i in range (1, (len(ranges))):
        ranges[i] = ranges[i] / total + ranges[i-1]
        print(print_list[i], ranges[i])


    return ranges

# generate the random values.
def generate_random():
    return random.random()

# actually pick the team given the random input
def pick_team(ranges, rand):
    if rand <= ranges[0]:
        return 0
    
    for i in range(1, len(ranges)):
        if rand <= ranges[i] and rand > ranges[i - 1]:
            return i
main()