
def cardCompany():
    while True:
            try:
                card_num = int(input('Enter card number: '))
                check = str(card_num)
                if len(check) < 13 or len(check) > 16:
                    continue
            except:
                print('INVALID')
                continue

            even_nos = check[::2]
            odd_nos = check[1::2]
            sum_even = [int(x)*2 for x in even_nos]
            sum_odd = [int(y) for y in odd_nos]
            lten = [p for p in sum_even if p<10]
            gten = [i - 9 for i in sum_even if i >= 10]
            tbh_e = sum(gten) + sum(lten)
            tbh_o = sum(sum_odd)
            final = tbh_e + tbh_o
            if final % 10 == 0:
                print("Your card is")
            else:
                print('Fraud')
                break

            first_num = check[0]
            first_num = int(first_num)
            if first_num % 3 == 0:
                print('AMEX')
            elif first_num % 4 == 0:
                print('Visa')
            elif first_num % 5 == 0:
                print('MasterCard')
            else: print('Not Valid')
            break

cardCompany()
