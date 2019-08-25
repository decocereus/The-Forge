while True:
    try:
        card = float(input('Enter card number: '))
        if len(card) > 16 or len(card) < 13:
            continue
    except:
        print()
        continue


    for i in card:
        product = card[2*(0+1):]
        print(product)
