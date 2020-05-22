def shittyoverlappingsums():
    try:
        with open('output.txt', 'r') as f:
            """slower, but more economical (my choice tbh)"""
            floats = []
            [floats.append(int(i.strip()) / 4294967295) for i in f.readlines() if i.strip()]
            """10% quicker, consumes much more PowerPC (hehe XD)"""
            # floats = [int(i.strip()) / 4294967295 for i in f.readlines() if i.strip()]

        f.close()

        [print(sum([floats[j] for j in range(i, i + 100)])) for i in range(len(floats) - 100)]  # printing
        # return [sum([floats[j] for j in range(i, i + 100)]) for i in range(len(floats) - 100)] # if u want to use them (rocket science here, fuck u PEP8.)

    except Exception as e:
        print(e)

    return
