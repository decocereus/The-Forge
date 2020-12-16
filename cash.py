while True:
    try:
        cash_owed = float(input('Change owed: '))
        if cash_owed < 0:
            continue
    except:
        print('Need a valid input.')
        continue

    cents = int(round(cash_owed*100))

    remainder = 0

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    while True:

        if cents >= 25:
            remainder = cents % 25
            q1 = (cents - remainder)/25

        elif cents >= 10:
            remainder = cents % 10
            q2 = (cents - remainder)/10

        elif cents >= 5:
            remainder = cents % 5
            q3 = (cents - remainder)/5

        elif cents > 1:
            remainder = cents % 1
            q4 = (cents - remainder)/1

        cents = remainder

        if remainder is 0:
            break

    quotient = q1 + q2 + q3 + q4

    print('The minimum amount of coins required are', quotient)

    break
