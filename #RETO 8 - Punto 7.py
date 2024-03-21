#RETO 8 - Punto 7
#Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

if __name__ == "__main__":
    print("Tablas de multiplicar del 1 al 9")
    n : int = 1
    p : int = 1
    for i in range(1,10):
        print(f"Tabla del {p}") 
        for j in range(1,11):
            m : int = n*p
            print(f"{p} por {n} es {m}")
            n += 1
        p += 1
        n = 1

# ! /\|=\/