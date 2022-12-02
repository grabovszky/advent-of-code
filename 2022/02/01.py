data = open("input_files/02_input.txt").read()

score = 0
for line in data.split("\n"):
    player1, player2 = line.split()

    if player2 == "X":
        if player1 == "C":
            score += 6
        if player1 == "A":
            score += 3
        score += 1

    if player2 == "Y":
        if player1 == "A":
            score += 6
        if player1 == "B":
            score += 3
        score += 2

    if player2 == "Z":
        if player1 == "B":
            score += 6
        if player1 == "C":
            score += 3
        score += 3

print(score)
