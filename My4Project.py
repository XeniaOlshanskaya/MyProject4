text = input()
letter = input()

new_str = ''
str_letter = 'аеёиоуыэюя'
n = 0

for text_letter in text:
    while n < 10 and text_letter != str_letter[n]:
        n += 1
    if n == 10:
        new_str += text_letter
    elif n < 10:
        new_str += text_letter + letter + text_letter
    n = 0

print(new_str)

