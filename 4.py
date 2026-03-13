with open('input.txt', 'r', encoding='utf-8') as inp:
    lines = inp.readlines()

with open('output.txt', 'w', encoding='utf-8') as out:
    for line in lines:
        if len(line) > 20:
            out.write(line)
