from scipy.stats import kstest
import numpy as np


def shittyparkinglot():
    print("\n\n\nParkingLot")
    xi = 0
    test_no = 0
    results = {}
    data = list()

    try:
        with open('output100v2.txt', 'r') as f:
            floats = []
            [floats.append(int(i.strip())) for i in f.readlines() if i.strip()]

        f.close()

    except Exception as e:
        print(e)

    while xi + 2 < len(floats):
        parked, crashed = 0, 0
        tries = 12000
        parking = {}

        while tries and xi + 2 != len(floats):
            if (floats[xi], floats[xi + 1]) in parking:
                crashed += 1

            else:
                parked += 1
                parking[floats[xi], floats[xi + 1]] = True

            xi += 2
            tries -= 1

        res = (crashed - 3523) / 21.9

        data.append(res)

        if tries == 0:
            results[test_no] = {'crashed': crashed,
                                'parked': parked,
                                'no. tries': 12000 - tries,
                                'result': res}
            test_no += 1

    data.sort()

    x = np.linspace(data[0], data[len(data) - 1], num=len(data) - 1)
    print(kstest(x, 'norm'))

    return results
