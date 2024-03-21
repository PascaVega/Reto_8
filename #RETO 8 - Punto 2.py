#RETO 8 - Punto 2
#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

n : int = 1
m : int = 2

if __name__ == "__main__":
    print("Números impares del 1 al 999")
    for i in range (1,501):
        print(str(n))
        n += 2

    print("Números pares del 2 al 1000")

    for j in range (2,502):
        print(str(m))
        m += 2

# ! /\|=\/