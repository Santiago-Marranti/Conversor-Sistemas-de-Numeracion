# Conversor de Sistemas de Numeración

 Universidad Provincial de Córdoba - UPC

 Profesor: Narciso Perez

 Alumno: Santiago Elias Marranti
 
 Fecha: 06/08/2025
 
# Actividad
 Codificar en Python los algoritmos de conversión de binario a decimal, de decimal a binario, conversión de números decimales, cálculo de complemento.

# Sobre el programa
Este programa tiene una interfaz por consola que permite que el usuario pueda acceder a las distintas funcionalidades que pide la actividad. Los pasajes a través de los distintos sistemas de representacion estan escritos respetando los pasos y reglas (algoritmo) enseñado en clase.

# Imagenes

<img width="466" height="152" alt="image" src="https://github.com/user-attachments/assets/b10c6dd4-9df6-42a9-bbe5-fd7216bad7d2" />
<p></p>
<img width="460" height="255" alt="image" src="https://github.com/user-attachments/assets/f10e94ab-20a0-4fdf-bca3-dbd7e3db8d3f" />
<p></p>
<img width="464" height="238" alt="image" src="https://github.com/user-attachments/assets/d336034a-9cca-4c68-89c2-1c5f7b87229a" />
<p></p>
<img width="500" height="236" alt="image" src="https://github.com/user-attachments/assets/5c946172-e54c-4992-98e6-6ab4f30b525a" />
<p></p>
<img width="485" height="225" alt="image" src="https://github.com/user-attachments/assets/cb29e73c-9e84-4820-b26e-6fe466aa6c4e" />


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

# Conversion de decimales
## Decimal a Octal
Se utilizo el mismo metodo de pasaje de decimal a binario cambiando la base 2 por 8, siendo los restos tomados y ordenados desde el ultimo obtenido al primero.

## Decimal a Hexadecimal
Se utilizo el mismo metodo de pasaje de decimal a octal cambiando la base 8 por 16, siendo los restos tomados y ordenados desde el ultimo obtenido al primero y sustituyendo valores superiores o iguales a 10 y menores o iguales a 15 por los simbolos que especifica la tabla:

A = 10
B = 11
C = 12
D = 13
E = 14
F = 15

# Calculo de complemento
Se utilizo el procedimiento explicado en clase del valor a complementar de un numero calculado para alcanzar determinado formato:

C₁₀ N = 10^n - N
Donde N -> el numero a calcular complemento
n -> posicion de digito que ocupa contando desde 1.

Ejemplo:

C₁₀ 25 = 10^2 - 25 = 75 para formato n = 2
C₁₀ 132 = 10^3 - 132 = 868 para formato n = 3

