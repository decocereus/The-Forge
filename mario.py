while True:
    try:
        h = int(input('Height: '))
        if h<1 or h>8:
            continue
    except:
        print('Need a valid input.')
        continue


    def pyramid():
        for j in range(0, h):
            for r in range(0, j + 1):
                print('#  ', end='')

            print()


    pyramid()
