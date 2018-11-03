text = input()
letter = input()

new_str = ''
str_letter = 'аеёиоуыэюя'
n = 0

for i in text:
    while n < 10 and i != str_letter[n]:
        n += 1
    if n == 10:
        new_str += i
    elif n < 10:
        new_str += i + letter + i
    n = 0

print(new_str)
