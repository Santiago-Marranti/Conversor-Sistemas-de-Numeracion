# Conversor de sistemas de numeracion
 Universidad Provincial de Córdoba - UPC
 Alumno: Santiago Elias Marranti
 Fecha: 06/08/2025
 Profesor: Narciso Perez
 
# Actividad
 Codificar en Python los algoritmos de conversión de binario a decimal, de decimal a binario, conversión de números decimales, cálculo de complemento.

Este programa tiene una interfaz por consola que permite que el usuario pueda acceder a las distintas funcionalidades que pide la actividad. Los pasajes a través de los distintos sistemas de representacion estan escritos respetando los pasos y reglas (algoritmo) enseñado en clase.

# Decimal a Binario
El algoritmo se desarrolló pensando en que el decimal debe ser dividido por la base del sistema de numeracion, en este caso por 2, luego se guarda el resto y el cociente es dividido nuevamente por 2, y asi iterativamente hasta que el cociente es 0. Esa es la condicion de corte.
Luego todo el binario se invierte la posicion de los bits, es decir el bit MSB (mas significativo) pasa a ser bit LSB (menos significativo).

Ejemplo: 10010011 -> 11001001

# Binario a decimal
Para este pasaje se utiliza el sigueinte polinomio:

(Polinomio de potencias de la base)
a * 2^n donde:

a -> es el valor de un bit en una posicion determinada.
n -> es la posicion que ocupa dentro del binario.

cada bit representa un termino del polinomio

Ejemplo: 11001

(Izquierda a derecha)
1 * 2^4 + 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0

16      + 8       + 0       + 0       + 1

25 decimal.

