data = open("input_files/01_input.txt").read()

current_carried = 0
max_carried_by_one = 0

for food in data.split("\n"):
    if len(food) == 0:
        current_carried = 0
    else:
        current_carried += int(food)

    max_carried_by_one = max(max_carried_by_one, current_carried)

print(max_carried_by_one)
