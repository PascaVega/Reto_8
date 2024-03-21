#RETO 8 - Punto 6
#Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

def introducir():
    base : float = float(input("Introduzca la base. Ejemplo: 5: "))
    exponente : int = int(input("Introduzca el exponente. Ejemplo: 5: "))
    desarrollo(base,exponente)

def desarrollo(base,exponente):
    potencia : float = 1
    for i in range(1, exponente+1):
        potencia *=base
    print(f"{base} elevado a {exponente} es {potencia}")
        
def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para calcular el valor de x^n.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/