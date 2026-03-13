try:
    with open('input.txt', 'r', encoding='utf-8') as inp:
        lines = inp.readlines()

    n = int(lines[0].strip())     
    count = len(lines) - 1        

    with open('output.txt', 'w', encoding='utf-8') as out:
        if count == n:
            out.write("YES")
        else:
            out.write("NO")

except ValueError:
    with open('output.txt', 'w', encoding='utf-8') as out:
        out.write("ERROR")
