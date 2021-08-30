def area(b,h):
    a = (b * h)

    return a

def vol(a,l):
    v = a * l

    return v
def main():
    #escribe tu código abajo de esta línea
base = float(input('Dame la base: '))
altura = float(input('Dame la altura: '))
prof = float(input('Dame la profundidad: '))

print('El volumen del prisma es: ' + str(vol(area(base, altura),prof)))

if __name__=='__main__':
    main()
