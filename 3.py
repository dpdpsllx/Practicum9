with open('input.txt', 'r', encoding='utf-8') as inp:
    lines = inp.readlines()

word = ''

for line in lines:
    if line != '':                
        word += line[0]     

with open('output.txt', 'w', encoding='utf-8') as out:
    out.write(word)
