with open('input.txt', 'r', encoding='utf-8') as file:
    text = f.read()

text = text.upper()

with open('output.txt', 'w', encoding='utf-8') as file:
    f.write(text)
