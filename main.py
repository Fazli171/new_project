def binar(a : str , b : str):
    a1 = int(a , 2)
    b1 = int(b , 2)
    nat = b1 + a1
    natija = ''
    while nat > 0:
        natija += str(nat % 2)
        nat //= 2 
    return natija[::-1]
print(binar('11', '1'))

def my_sqrt(x):  
    if x == 0:
        return 0
    yarmi = x // 2
    while True:
        new_x = (yarmi + x // yarmi) // 2
        if new_x == yarmi :
            break
        yarmi = new_x
    return yarmi
print(my_sqrt(30))