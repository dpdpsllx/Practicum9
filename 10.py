with open('input.txt') as f:
    today = f.readline().strip()
    n = int(f.readline())

    d, m = map(int, today.split('.'))
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    today = sum(days[:m-1]) + d

    res = []

    for _ in range(n):
        cell, date = f.readline().split()
        d, m = map(int, date.split('.'))
        day = sum(days[:m-1]) + d

        if today - day > 3:
            res.append(cell)

with open('output.txt','w') as f:
    f.write('\n'.join(res))
