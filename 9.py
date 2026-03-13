with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('simple/output.txt', 'w', encoding='utf-8') as f:
    for i in range(1, len(lines), 2):
        f.write(lines[i])
