text1, text2, text3 = input().split(), input().split(), input().split()
repeat = text1 + text2 + text3
for word in text1:
    if word in text2 + text3:
        repeat.remove(word)
for word in text2:
    if word in text1 + text3:
        repeat.remove(word)
for word in text3:
    if word in text2 + text1:
        repeat.remove(word)
n = 0
for word in repeat:
    n += len(word)
print(f'{'#'.join(repeat)}\n{n}')
