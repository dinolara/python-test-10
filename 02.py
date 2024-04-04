text = input().split() + input().split() + input().split()
answer = set()
n = 0
for word in text:
    if text.count(word) == 1:
        answer.add(word)
        n += len(word)
print(f'{'#'.join(answer)}\n{n}')
