
def card_Verification():
    while True:
        try:
            card_num = int(input('Enter your card number: '))
            card_string = str(card_num)
            if len(card_string) < 13 or len(card_string) > 16:
                continue
        except:
            print('Invalid input')
            continue

        even_num = card_string[::2]
        odd_num = card_string[1::2]
        elist = [int(x)*2 for x in even_num]
        olist = [int(y) for y in odd_num]
        osum = sum(olist)
        gten = sum([g-9 for g in elist if g >= 10])
        lten = sum([l for l in elist if l < 10])
        final_sum = osum + gten + lten
        if final_sum % 10 == 0:
            print('Valid Card number')

        first_num = card_string[0]
        first_num = int(first_num)

        if first_num % 3 == 0:
            print('American Express')
        elif first_num % 4 == 0:
            print('Visa')
        elif first_num % 5 == 0:
            print('MasterCard')
        else:   print('Your Card is valid but its provider is not known.')

        break

card_Verification()
