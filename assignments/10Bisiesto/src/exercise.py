def es_bisiesto(a):
    if a%4 == 0:
        return True
    elif a%400 == 0:
        return True
    else:
        return False

def main():
    #escribe tu código abajo de esta línea
    año = int(input())
    print( es_bisiesto(año))

if __name__=='__main__':
    main()
