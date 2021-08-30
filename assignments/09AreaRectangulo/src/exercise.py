def area(b,h):
    a = (b * h)

    return a
def main():
    #escribe tu código abajo de esta línea
    base = float(input('Dame la base: '))
    altura = float(input('Dame la altura: '))

    print('El área del rectángulo es: ' + str(area(base,altura)))

if __name__=='__main__':
    main()
