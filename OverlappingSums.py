from scipy.stats import kstest
import numpy as np

def shittyoverlappingsums():
    print("\n\n\nOverlapping sums:")
    try:
        with open('output32bit.txt', 'r') as f:
            floats = []
            [floats.append(int(i.strip()) / 4294967295) for i in f.readlines() if i.strip()]

        f.close()

        tmp = []
        [tmp.append(sum([floats[j] for j in range(i, i + 100)])) for i in range(len(floats) - 100)]
        tmp.sort()
        x = np.linspace(tmp[0], tmp[len(tmp) - 1], num=len(tmp)-1)
        print(f'x={x}, len={len(tmp)},\n{kstest(x, "norm")}')

        # return [sum([floats[j] for j in range(i, i + 100)]) for i in range(len(floats) - 100)] # if u want to use them (rocket science here, fuck u PEP8.)

    except Exception as e:
        print(e)

    return
