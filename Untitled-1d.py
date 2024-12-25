from random import randint, choice, shuffle

def calkulator(s_soni: int) -> int:
    togri = 0
    xato = 0
    m = 1
    while s_soni >= m:
        a1, a2 = randint(2, 10), randint(1, 10)
        a3 = a1 * a2 
        n = randint(2, 9) * randint(1, 10)
        n1 = randint(2, 9) * randint(1, 10)
        num = [n, n1, a3]
        shuffle(num)
        if n != n1 and n != a3 and n1 != a3:
            a, b, c = num
            print(f'natijani kriting {a1} * {a2}') 
            natija = input(f"a = {a}\nb = {b}\nc = {c}\njavobni kriting ").lower()
            if natija == 'a':
                t = a
            elif natija == 'b':
                t = b
            elif natija == 'c':
                t = c
            if a3 == t:
                togri += 1
                print(f' togro javob')
            else:
                if natija != 'x':
                    xato += 1
                    print('xato')
        m += 1
        print(f"{togri} ta to'g'ri {xato} ta xato")
print(calkulator(10))

        