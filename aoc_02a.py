f = open('input_02.txt')

# A, X Rock 1
# B, Y Paper 2
# C, Z Scissors 3

score ={"A X": 3+1,
        "A Y": 6+2,
        "A Z": 0+3,
        "B X": 0+1,
        "B Y": 3+2,
        "B Z": 6+3,
        "C X": 6+1,
        "C Y": 0+2,
        "C Z": 3+3}

total = 0

for line in f:
    total += score[line.strip()]

print(total)