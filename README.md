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

n : int = 1

if __name__ == "__main__":
    print("Números del 1 al 100 con su respectivo cuadrado.")

    for i in range(1,101):
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
    n : int = int(input("Introduzca un numero natural mayor o igual a 2: "))
    desarrollo(n)

def desarrollo(n):
    if n%2==0:
        m : int = int((n/2)+1)
        for i in range(1,m):
            if n%2==0:
                print(str(n))
                n -=2
            else:
                n = n-1
    else:
        k : int = int(((n+1)/2)+1)
        for j in range(1,k):
            if n%2==0:
                print(str(n))
                n -=2
            else:
                n = n-1

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
    numero : int = int(input("Ingrese el número hasta el que quiere conocer su factorial. Ejemplo: 5: "))
    desarrollar(numero)
    return

def desarrollar(numero):
    if numero < 0:
        print(f"No existe el factorial de {numero}.")
        return
    elif numero == 0:
        print(f"El factorial de {numero} es 1.")
        return
    else:
        for i in range(1,numero+1):
            n : int = numero
            factorial : int = 1
            factorial_numero(numero,factorial,n)
            numero -= 1
        return

def factorial_numero(numero,factorial,n):
    for j in range(1,n+1):
        factorial *= n
        n -=1
    print(f"El factorial de {numero} es {factorial}")
    return
    
def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para imprimir los números desde el 1 hasta determinado número con su respectivo factorial.")

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
    numero : int = int(input("Introduzca el exponente. Ejemplo: 5: "))
    desarrollo(numero)

def desarrollo(numero):
    potencia : int = 1
    for i in range(1, numero+1):
        potencia *=2
    print(f"2 elevado a {numero} es {potencia}")
        

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para calcular el valor de 2 elevado a un número dado")

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
    base : float = float(input("Introduzca la base. Ejemplo: 5: "))
    exponente : int = int(input("Introduzca el exponente. Ejemplo: 5: "))
    desarrollo(base,exponente)

def desarrollo(base,exponente):
    potencia : float = 1
    for i in range(1, exponente+1):
        potencia *=base
    print(f"{base} elevado a {exponente} es {potencia}")
        
def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para calcular el valor de x^n.")

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
import math

def introducir():
    x : float = float(input("Ingrese el valor de x: "))
    n : int = int(input("Ingrese el número de términos a utilizar: "))
    desarrollo(x,n)

def desarrollo(x,n):
    maclaurin(x,n)
    aprox : float
    v_real : float
    difer : float
    aprox, v_real, difer = maclaurin(x, n)
    print(f"Aproximación utilizando {n} términos de la serie de Maclaurin: {aprox}")
    print(f"Valor real de la función exponencial: {v_real}")
    print(f"Diferencia entre la aproximación y el valor real: {difer}")
    error_menor(x)

def maclaurin(x,n):
    aproximacion : float = 0
    for i in range(n):
        a : int = factorial_numero(i)
        aproximacion += (x**i) / a
    valor_real : float = math.exp(x)
    diferencia : float = valor_real - aproximacion
    diferencia_abs = diferencia if diferencia >= 0 else -diferencia
    return aproximacion, valor_real, diferencia_abs

def factorial_numero(i):
    factorial : int = 1
    for j in range(1,i+1):
        factorial *= i
        i -=1
    return factorial
  
def error_menor(x):
    m : int = 0
    error = 0.001 * math.exp(x)
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
    print("Programa para calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin.")

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
import math

def introducir():
    x : float = float(input("Ingrese el valor de x: "))
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
        a : int = factorial_numero(2*i + 1)
        aproximacion += ((-1)**i) * (x**(2*i+1)) / a
    valor_real : float = math.sin(x)
    diferencia : float = valor_real - aproximacion
    diferencia_abs = diferencia if diferencia >= 0 else -diferencia
    return aproximacion, valor_real, diferencia_abs

def factorial_numero(i):
    factorial : int = 1
    for j in range(1,i+1):
        factorial *= i
        i -=1
    return factorial

def error_menor(x):
    m : int = 0
    error = 0.001 * math.sin(x)
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
```
