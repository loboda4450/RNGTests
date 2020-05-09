def shittyoverlappingsums():
    with open('output.txt', 'r') as f:
        floats = []
        [floats.append(int(i.strip()) / 4294967295) for i in f.readlines()]

    f.close()

    return [sum([floats[j] for j in range(i, i + 100)]) for i in range(len(floats) - 100)]
