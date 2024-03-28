#RETO 8 - Punto 3
#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

def introducir():
    #Se introduce la variable
    n : int = int(input("Introduzca un numero natural mayor o igual a 2: "))
    desarrollo(n)

def desarrollo(n):
    #Si el número ingresado es divisible en 2 entonces se utiliza el condicional if
    if n%2==0:
        m : int = int((n/2)+2) #Se divide en dos y se le suma uno al resultado por el contador, asi dse pbtiene el número de veces que se va a repetir el ciclo for
        for i in range(1,m):
            if n%2==0:
                print(str(n))
                n -=2

    #Si el número no es divisible por 2 entonces ingresa en el condicional else
    else:
        #Se suma uno al número y luego se divide por 2 ya que es un número impar, y luego se suma uno por el contador
        k : int = int(((n+1)/2)+1) 
        n = n-1
        for j in range(1,k):
            #Como el número es impar es necesario definir los condicionales para mantener todos los números siendo pares
            print(str(n))
            n -=2
            
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
