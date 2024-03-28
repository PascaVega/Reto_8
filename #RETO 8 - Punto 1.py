#RETO 8 - Punto 1
#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

#Se define una variable inicial
n : int = 1

if __name__ == "__main__":
    print("Números del 1 al 100 con su respectivo cuadrado.")
    #Se crea un ciclo for para que se impriman los números en el intervalo [1,100]
    for i in range(1,101):
        #m se utiliza para expresar el cuadrado de los números
        m : int = n**2
        print(f"El cuadrado de {n} es {m}")
        n += 1

# ! /\|=\/
