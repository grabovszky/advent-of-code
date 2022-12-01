data = open("input_files/01_input.txt").read()

current_carried = 0
sum_carried_by_one = []

for food in data.split("\n"):
    if len(food) == 0:
        sum_carried_by_one.append(current_carried)
        current_carried = 0
    else:
        current_carried += int(food)


sum_carried_by_one.append(current_carried)
sum_carried_by_one.sort()
sum_of_three_biggest = (
    sum_carried_by_one[-1] + sum_carried_by_one[-2] + sum_carried_by_one[-3]
)

print(sum_of_three_biggest)
