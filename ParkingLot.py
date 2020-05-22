def shittyparkinglot():
    xi = 0
    test_no = 0
    results = {}

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

        res = (crashed - 3523)/21.9

        # print(f'\nCrashed {crashed} cars.\nParked {parked} cars.\nTried {12000 - tries} times.\n {res}')

        results[test_no] = {'crashed': crashed,
                            'parked': parked,
                            'no. tries': 12000 - tries,
                            'result': res}
        test_no += 1

    for i in results:
        print(results[i])


