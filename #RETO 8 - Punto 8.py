#RETO 8 - Punto 8
#Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. 

#Se importa math para concoer el valor real de la función
import math

def introducir():
    #Se ingresan las dos variables
    x : float = float(input("Ingrese el valor de x: "))
    n : int = int(input("Ingrese el número de términos a utilizar: "))
    desarrollo(x,n)

def desarrollo(x,n):
    maclaurin(x,n)
    #Se crean las tres variables como los resultados
    aprox : float
    v_real : float
    difer : float
    aprox, v_real, difer = maclaurin(x, n)
    print(f"Aproximación utilizando {n} términos de la serie de Maclaurin: {aprox}")
    print(f"Valor real de la función exponencial: {v_real}")
    print(f"Diferencia entre la aproximación y el valor real: {difer}")
    error_menor(x)

def maclaurin(x,n):
    #Se define la variable
    aproximacion : float = 0
    #Se repite el número de terminos a usar
    for i in range(n+1):
        a : int = factorial_numero(i)
        aproximacion += (x**i) / a
    #Se calcula el valor real
    valor_real : float = math.exp(x)
    #Se calcula la diferencia
    diferencia : float = valor_real - aproximacion
    #Se halla el valor absoluto de la ddiferencia
    diferencia_abs = diferencia if diferencia >= 0 else -diferencia
    return aproximacion, valor_real, diferencia_abs

def factorial_numero(i):
    #Se define la varibale que va a llevar el valor final
    factorial : int = 1
    #se repite i veces
    for j in range(1,i+1):
        factorial *= i
        i -=1
    return factorial
  
def error_menor(x):
    #Para calcular el número de terminos necesarios para que el error sea menor al 0.1%
    m : int = 0
    #Se halla el error máximo
    error = 0.001 * math.exp(x)
    #Se repite el ciclo hasta que la diferencia sea menor al error
    while True:
        aprox, v_real, difer = maclaurin(x, m)
        if difer < error:
            break
        m += 1
    print(f"Para obtener menos del 0.1% de error, se necesitan al menos {m} términos.")

def continuar():
    #El usuario decide si deea repetir el código
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin.")
    #El programa se repeitrá hasta que el usuario lo desee
    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
