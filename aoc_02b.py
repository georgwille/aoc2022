f = open('input_02.txt')

# A Rock 1
# B Paper 2
# C Scissors 3
# X loss
# Y draw
# Z wins

score ={"A X": 0+3,
        "A Y": 3+1,
        "A Z": 6+2,
        "B X": 0+1,
        "B Y": 3+2,
        "B Z": 6+3,
        "C X": 0+2,
        "C Y": 3+3,
        "C Z": 6+1}

total = 0

for line in f:
    total += score[line.strip()]

print(total)