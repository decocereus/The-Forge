# To verify the authenticity of a card multiply every other digit by
# 2 starting with second last digit then add those products digits
# add the sum to the sum of the digits left from earlier
# if the totals last digit is 0 or if the remainder is 0 when taken mod 10
# then the number is valid.
# 4 0 0 3 6 0 0 0 0 0 0 0 0 0 1 4
# 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 (index)
# multiply every digit by 2 whose index is even.
# for 14 digs index is 13 thus 14 and 16 are same
# for 13 digs index is 12 thus 13 and 15 are same
# This is for repromting the user if the input is not valid
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

#4003600000000014 this is the sample input











# This piece is check for which type of card it is.
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
