data = open("input_files/02_input.txt").read()

score = 0
for line in data.split("\n"):
    player1, player2 = line.split()

    if player2 == "X":
        if player1 == "A":
            score += 3
        if player1 == "B":
            score += 1
        if player1 == "C":
            score += 2
        score += 0

    if player2 == "Y":
        if player1 == "A":
            score += 1
        if player1 == "B":
            score += 2
        if player1 == "C":
            score += 3
        score += 3

    if player2 == "Z":
        if player1 == "A":
            score += 2
        if player1 == "B":
            score += 3
        if player1 == "C":
            score += 1
        score += 6

print(score)
