import sys

holes_1 = ["A", "D", "O", "P", "Q", "R", "W", "6", "9", "0", "4"]
holes_2 = ["B", "8"]

for line in sys.stdin.readlines():
    holes = 0
    for c in str(line):
        if c in holes_1:
            holes += 1
            if c in holes_2:
                holes += 2
                if holes != 0:
                    print holes
