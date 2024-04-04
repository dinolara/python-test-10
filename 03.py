text = [int(a) for a in input().split()]
while text != [100]:
    n = []
    s = 0
    for num in text:
        if '0' in str(num):
            n.append(str(num))
            s += num
    if len(n):
        print(f'{':'.join(n)}:{s}')
    else:
        print(0)
    text = [int(a) for a in input().split()]
