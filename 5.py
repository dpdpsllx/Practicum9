try:
    with open('input.txt', 'r', encoding='utf-8') as inp:
        a = int(inp.readline())
        b = int(inp.readline())
        c = int(inp.readline())

    result = a / b + c

    with open('output.txt', 'w', encoding='utf-8') as out:
        out.write(str(result))

except ValueError:
    with open('output.txt', 'w', encoding='utf-8') as out:
        out.write('ValueError')

except ZeroDivisionError:
    with open('output.txt', 'w', encoding='utf-8') as out:
        out.write('ZeroDivisionError')
