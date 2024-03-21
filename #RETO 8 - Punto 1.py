#RETO 8 - Punto 1
#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

n : int = 1

if __name__ == "__main__":
    print("Números del 1 al 100 con su respectivo cuadrado.")

    for i in range(1,101):
        m : int = n**2
        print(f"El cuadrado de {n} es {m}")
        n += 1

# ! /\|=\/