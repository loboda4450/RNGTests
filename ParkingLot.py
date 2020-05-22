def shittyparkinglot():
    parked, crashed = 0, 0
    xi = 0
    tries = 12000
    parking = {}

    try:
        with open('output100.txt', 'r') as f:
            floats = []
            [floats.append(int(i.strip())) for i in f.readlines() if i.strip()]

        f.close()

    except Exception as e:
        print(e)

    while tries and xi + 2 != len(floats):
        if (floats[xi], floats[xi + 1]) in parking:
            crashed += 1

        else:
            parked += 1
            parking[floats[xi], floats[xi + 1]] = True

        xi += 2
        tries -= 1

    print(f'\nCrashed {crashed} cars.\nParked {parked} cars.')
