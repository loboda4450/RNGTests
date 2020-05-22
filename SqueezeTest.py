def shittysqueezetest():
    over = 0
    below = 0

    try:
        with open('output32bit.txt', 'r') as f:
            floats = []
            [floats.append(int(i.strip()) / 4294967295) for i in f.readlines() if i.strip()]

        f.close()

    except Exception as e:
        print(e)

    for i in range(len(floats)):
        k = 2147483647
        j = 0

        while (k >= 1) and (j <= 48):
            k *= floats[i]
            j += 1

        if j < 6:
            below += 1
        elif j > 48:
            over += 1
        else:
            continue

    print(f'j > 48: {over} times.\nj < 6: {below} times.')
