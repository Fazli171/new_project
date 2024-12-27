def yak_res(funk):
    def wrapper(*args):
        sonlar = funk(*args)
        natija = list(filter(lambda i : i % 2 == 0 , sonlar))
        return natija
    return wrapper
def tub_s(funk):
    def wrapper(*args):
        natija = []
        sonlar = funk(*args)
        for i in sonlar:
            bol = []
            for j in range(1, i + 1):
                if i % j == 0:
                    bol.append(j)
            if len(bol) == 2:
                natija.append(i)
        return natija
    return wrapper
def new_res(funk):
    def wrapper(*args):
        sonlar = funk(*args)
        natija = [i ** 3 for i in sonlar]
        return natija
    return wrapper

def new_log(funk):

    def wrapper(*args):

        natija = funk(*args)
        log = input('login kriting: ')
        while True:
            if log == args[0]:
                while True:
                    por = input('parol kriting: ')
                    if por == args[1] :
                        return natija
                else:
                    print('parol  xato')
        else:
            print ("login xato")
    return wrapper
@yak_res
@new_res
@tub_s
@new_log
def admi(login: str, porol: str, n : int = 10 ):

    nev = []
    for i in range(n):
        nev.append(i)
    return nev

print(admi('fazli','fazli'))