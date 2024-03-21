#RETO 8 - Punto 9
#Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin.
import math

def introducir():
    x : float = float(input("Ingrese el valor de x en el rango [-1,1]. Ejemplo: -0.3: "))
    n : int = int(input("Ingrese el número de términos a utilizar: "))
    desarrollo(x,n)

def desarrollo(x,n):
    maclaurin(x,n)
    aprox : float
    v_real : float
    difer : float
    aprox, v_real, difer = maclaurin(x, n)
    print(f"Aproximación utilizando {n} términos de la serie de Maclaurin: {aprox}")
    print(f"Valor real de la función seno: {v_real}")
    print(f"Diferencia entre la aproximación y el valor real: {difer}")
    error_menor(x)

def maclaurin(x,n):
    aproximacion : float = 0
    for i in range(n):
        aproximacion += ((-1)**i) * (x**(2*i+1)) / (2*i + 1)
    valor_real : float = math.atan(x)
    diferencia : float = valor_real - aproximacion
    diferencia_abs = diferencia if diferencia >= 0 else -diferencia
    return aproximacion, valor_real, diferencia_abs

def error_menor(x):
    m : int = 0
    error = 0.001 * math.atan(x)
    while True:
        aprox, v_real, difer = maclaurin(x, m)
        if difer < error:
            break
        m += 1
    print(f"Para obtener menos del 0.1% de error, se necesitan al menos {m} términos.")
        
def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/