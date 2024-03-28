#RETO 8 - Punto 1
#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

#Se define una variable inicial
n : int = 1

if __name__ == "__main__":
    print("Números del 1 al 100 con su respectivo cuadrado.")

    #Se utiliza el ciclo for para imprimir los números
    for i in range(1,101):
        #m funciona como la variable para los cuadrados
        m : int = n**2
        print(f"El cuadrado de {n} es {m}")
        n += 1

# ! /\|=\/
