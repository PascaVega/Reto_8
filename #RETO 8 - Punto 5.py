#RETO 8 - Punto 5
#Calcular el valor de 2 elevado a la potencia n usando ciclos for.

def introducir():
    numero : int = int(input("Introduzca el exponente. Ejemplo: 5: "))
    desarrollo(numero)

def desarrollo(numero):
    potencia : int = 1
    for i in range(1, numero+1):
        potencia *=2
    print(f"2 elevado a {numero} es {potencia}")
        

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para calcular el valor de 2 elevado a un número dado")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/