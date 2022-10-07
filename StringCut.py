str1 = input()
if len(str1) <= 8:
    print(str1 + "0" * (8 - len(str1)))
else:
    lens = len(str1)
    m = len(str1) // 8
    n = len(str1) % 8
    for i in range(m):
        print(str1[(i * 8):((i + 1) * 8)])
    if n > 0:
        print(str1[((-1) * n):] + "0" * (8 - n))
