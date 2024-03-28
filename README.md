# Reto 8
| Nombre                 | Identificación | Grupo | Trabajo          |
|------------------------|----------------|-------|------------------|
| Angélica Pascagaza Vega| 1031652163     |   5   | Trabajo individual |

## Solución del reto
<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 1</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">En esta ocasión, se reciclo el codigo del reto pasado, pero en esta ocasión se utilizó el ciclo <i>for</i>.</td>
  </tr>
</table>

**Parte 1**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 2</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este ejercicio, se utilizaron dos ciclos <i>for</i>, el primero para imprimir los números impares y el segundo para los números pares.</td>
  </tr>
</table>

**Parte 2**
```python
#RETO 8 - Punto 2
#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

#Se definen dos variables iniciales, n para los impares y m para los pares
n : int = 1
m : int = 2

if __name__ == "__main__":
    print("Números impares del 1 al 999")
    #Se imprimen los números impares
    for i in range (1,501):
        print(str(n))
        n += 2

    print("Números pares del 2 al 1000")
    #Se imprimen los números pares
    for j in range (2,502):
        print(str(m))
        m += 2

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 3</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">En esta ocasión, se hace uso de dos ciclos <i>for</i> para determinar los números pares menores a cierto número.</td>
  </tr>
</table>

**Parte 3**
```python
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
            
def continuar():}
    #El usuario decide si desea volver a correr el programa
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Ingrese un número natural para obtener los números pares descendentes hasta 2")
    #El código se repetirá tantas veces como el usuario desee
    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 4</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este punto, se plantean condicionales que nos separan el código en tres opciones, en donde dos de ellas es por si el número es 0 y 1 (quienes tienen valores específicos al momento de obtener el factorial), y el tercer condicional se utiliza para ingresar dos ciclos for y una función, los cuales nos permiten obtener todos los factoriales.</tr>
</table>

**Parte 4**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 5</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Calcular el valor de 2 elevado a la potencia n usando ciclos for.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para el quinto punto del reto, se emplea el ciclo <i>for</i> para multiplicar el número 2 por si mismo tantas veces el usuario desee, obteniendo así la potencia de 2^n.</td>
  </tr>
</table>

**Parte 5** 
```python
#RETO 8 - Punto 5
#Calcular el valor de 2 elevado a la potencia n usando ciclos for.

def introducir():
    #Se introduce el número
    numero : int = int(input("Introduzca el exponente. Ejemplo: 5: "))
    desarrollo(numero)

def desarrollo(numero):
    #Se define una nueva variable
    potencia : int = 1
    #En el ciclo se realiza una multiplicación reiterativa para hallar la potencia
    for i in range(1, numero+1):
        potencia *=2
    print(f"2 elevado a {numero} es {potencia}")
        

def continuar():
    # El usuario decide si repetir el programa
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para calcular el valor de 2 elevado a un número dado")
    #El ciclo se repetirá tantas veces como el usuario desee
    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 6</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. <b>Disclaimer:</b> Trate de no utilizar el operador de potencia (**).</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este ejercicio, únicamente se utiliza un ciclo <i>for</i> para multiplicar la base tantas veces como diga el exponente.</td>
  </tr>
</table>

**Parte 6** 
```python
#RETO 8 - Punto 6
#Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

def introducir():
    #Se incgresan los dos números a operar
    base : float = float(input("Introduzca la base. Ejemplo: 5: "))
    exponente : int = int(input("Introduzca el exponente. Ejemplo: 5: "))
    desarrollo(base,exponente)

def desarrollo(base,exponente):
    #Se define una nueva variable que va a expresar el resultado
    potencia : float = 1
    #El ciclo se basa en una multiplicación reiterada
    for i in range(1, exponente+1):
        potencia *=base
    print(f"{base} elevado a {exponente} es {potencia}")
        
def continuar():
    #El usuario decide si desea volver a correr el programa
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para calcular el valor de x^n.")
    #El programa continuará repitiendose hasta que el usuario lo desee
    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 7 - Parte 7</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
  <td style="color:#141414" align="center">Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este punto, se definieron dos ciclos <i>for</i>, el primero para que se repitiera para todas las tablas y el segundo con un rango de <i>(1,10)</i> para obtener la tabla de multiplicar de cada número.</td>
  </tr>
</table>

**Parte 7** 
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 8</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. <b>Nota:</b> use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">En esta ocasión, se partió de la sumatoria que llegaba hasta el número <i>n</i> (número de términos a utilizar). Para después crear una función <i>error_menor</i> en la cual se utiliza un ciclo <i>while</i> y el condicional <i>if</i> para cuántos términos se necesitan para obtener menos del 0.1% de error.</td>
  </tr>
</table>

**Parte 8** 
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 9</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. <b>Nota:</b> use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">En esta ocasión, se reutilizó el código del ejercicio anterior, y se cambió únicamente el tipo de función y partes de la sumatoria.</td>
  </tr>
</table>

**Parte 9** 
```python
#RETO 8 - Punto 9
#Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin.

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
    print(f"Valor real de la función seno: {v_real}")
    print(f"Diferencia entre la aproximación y el valor real: {difer}")
    error_menor(x)

def maclaurin(x,n):
    #Se define la variable
    aproximacion : float = 0
     #Se repite el número de terminos a usar
    for i in range(n):
        a : int = factorial_numero(2*i + 1)
        aproximacion += ((-1)**i) * (x**(2*i+1)) / a
    #Se calcula el valor real
    valor_real : float = math.sin(x)
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
    error = 0.001 * math.sin(x)
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
    print("Programa para calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin.")
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 10</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Diseñar una función que permita calcular una aproximación de la función <i>arcotangente</i> alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. <b>Nota:</b> use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este último ejercicio, se reutilizó el código de la anterior parte, y se cambió únicamente el tipo de función y partes de la sumatoria.</td>
  </tr>
</table>

**Parte 10** 
```python
#RETO 8 - Punto 10
#Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin.

#Se importa math para concoer el valor real de la función
import math

def introducir():
    #Se ingresan las dos variables
    x : float = float(input("Ingrese el valor de x en el rango [-1,1]. Ejemplo: -0.3: "))
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
    print(f"Valor real de la función seno: {v_real}")
    print(f"Diferencia entre la aproximación y el valor real: {difer}")
    error_menor(x)

def maclaurin(x,n):
    #Se define la variable
    aproximacion : float = 0
    #Se repite el número de terminos a usar
    for i in range(n):
        aproximacion += ((-1)**i) * (x**(2*i+1)) / (2*i + 1)
    #Se calcula el valor real
    valor_real : float = math.atan(x)
    #Se calcula la diferencia
    diferencia : float = valor_real - aproximacion
    #Se halla el valor absoluto de la ddiferencia
    diferencia_abs = diferencia if diferencia >= 0 else -diferencia
    return aproximacion, valor_real, diferencia_abs

def error_menor(x):
    #Para calcular el número de terminos necesarios para que el error sea menor al 0.1%
    m : int = 0
    #Se halla el error máximo
    error = 0.001 * math.atan(x)
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
    print("Programa para calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin.")
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
```
