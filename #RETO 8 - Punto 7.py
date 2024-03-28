#RETO 8 - Punto 7
#Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

#Inicia el programa
if __name__ == "__main__":
    print("Tablas de multiplicar del 1 al 9")
    #Se definen dos variables
    n : int = 1 #
    p : int = 1
    #El ciclo se repite 9 veces porque hay 9 numeros del 1 al 9
    for i in range(1,10):
        print(f"Tabla del {p}") 
        #El ciclo se repite diez veces para mostrar completamente las tablas
        for j in range(1,11):
            #m es el resultado de la multiplicación
            m : int = n*p
            print(f"{p} por {n} es {m}")
            n += 1
        p += 1
        n = 1

# ! /\|=\/
