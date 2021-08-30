def numTarjetas(pl, p):
    tpl = pl * 35
    tp = p * 12

    num = min([tpl,tp])
    return num
def main():
    #escribe tu código abajo de esta línea
    papel = int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones = int(input('Dame la cantidad de plumones: '))

    print('El número máximo de tarjetas que se pueden hacer es: ' + str(numTarjetas(plumones,papel)))

if __name__=='__main__':
    main()
