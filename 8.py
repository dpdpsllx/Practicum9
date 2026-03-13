daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
with open('input.txt', 'r', encoding='utf-8') as inp:
    steps = []
    for line in inp:
        steps.append(int(line.strip()))

index = 0

with open('output.txt', 'w', encoding='utf-8') as out:
    for days in daysinmonth:
        total = 0

        for i in range(days):
            total += steps[index]
            index += 1

        average = total / days
        out.write(str(average) + '\n')
