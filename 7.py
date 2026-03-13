with open('input.txt', 'r', encoding='utf-8') as inp:
    lines = inp.readlines()

with open('input.txt', 'w', encoding='utf-8') as out:
    for line in lines:
        if int(line.strip()) != 100:
            out.write(line)
