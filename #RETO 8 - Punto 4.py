#RETO 8 - Punto 4
#Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

def introducir():
    numero : int = int(input("Ingrese el número hasta el que quiere conocer su factorial. Ejemplo: 5: "))
    desarrollar(numero)
    return

def desarrollar(numero):
    if numero < 0:
        print(f"No existe el factorial de {numero}.")
        return
    elif numero == 0:
        print(f"El factorial de {numero} es 1.")
        return
    else:
        for i in range(1,numero+1):
            n : int = numero
            factorial : int = 1
            factorial_numero(numero,factorial,n)
            numero -= 1
        return

def factorial_numero(numero,factorial,n):
    for j in range(1,n+1):
        factorial *= n
        n -=1
    print(f"El factorial de {numero} es {factorial}")
    return
    
def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para imprimir los números desde el 1 hasta determinado número con su respectivo factorial.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/