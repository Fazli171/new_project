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