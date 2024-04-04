n = int(input())
text = input().split('; ')
words = []
for word in text:
    if len(word) % n:
        words.append(word.upper())
print(' - '.join(words))
