#RETO 8 - Punto 4
#Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

def introducir():
    #El usuario introduce el número
    numero : int = int(input("Ingrese el número hasta el que quiere conocer su factorial. Ejemplo: 5: "))
    desarrollar(numero)
    return

def desarrollar(numero):
    #Los números negativos no tienen factorial
    if numero < 0:
        print(f"No existe el factorial de {numero}.")
        return
    #El factorial de 0 siempre va a ser 1
    elif numero == 0:
        print(f"El factorial de {numero} es 1.")
        return
    #Factorial para todos los números naturales diferentes de 0
    else:
        for i in range(1,numero+1):
            #Se añaden dos nuevas variables
            n : int = numero
            factorial : int = 1
            factorial_numero(numero,factorial,n)
            numero -= 1
        return

def factorial_numero(numero,factorial,n):
    #Se inician a multiplicar los números desde el mayor
    for j in range(1,n+1):
        factorial *= n
        n -=1
    print(f"El factorial de {numero} es {factorial}")
    return
    
def continuar():
    #El usuario decide si desea continuar
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para imprimir los números desde el 1 hasta determinado número con su respectivo factorial.")
    #Ciclo para repetir el código tantas veces como el usuario desee
    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
