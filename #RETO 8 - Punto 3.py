#RETO 8 - Punto 3
#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

def introducir():
    n : int = int(input("Introduzca un numero natural mayor o igual a 2: "))
    desarrollo(n)

def desarrollo(n):
    if n%2==0:
        m : int = int((n/2)+1)
        for i in range(1,m):
            if n%2==0:
                print(str(n))
                n -=2
            else:
                n = n-1
    else:
        k : int = int(((n+1)/2)+1)
        for j in range(1,k):
            if n%2==0:
                print(str(n))
                n -=2
            else:
                n = n-1

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Ingrese un número natural para obtener los números pares descendentes hasta 2")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/