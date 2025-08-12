TablaOctal = ('000', '0', 
              '001', '1',
              '010', '2',
              '011', '3',
              '100', '4',
              '101', '5',
              '110', '6',
              '111', '7');

run = True;

def menu():
    print("<< Conversor de Sistemas de Numeración - Santiago Marranti >> \n");
    print("1. Conversor de binario a decimal.");
    print("2. Conversor de decimal a binario.");
    print("3. Conversión de números decimales.");
    print("4. Cálculo de complemento.");
    print("0. Salir.\n")

    return int(input("Opcion> "));

def binarioDecimal(bin):
    # Apunto al MSB (bit menos significativo). Se resta 1 porque el array arranca de 0.
    puntero = len(bin) - 1;
    decimal = 0;

    for i in range(0, len(bin)):
        # obtengo bits desde el bit MSB entre iteraciones (solo un bit por vuelta).
        bit = int(bin[puntero - i]);

        # Aplico polinomio de conversion entre sistemas de numeracion.
        # n * (b ^ d)
        # n = numero ; b = base ; d = digito.
        # Se suma iteraccion a iteraccion.
        decimal += bit * (2 ** i);

    return decimal;


def decimalBinario(decimal):
    bin = "";

    # Guardo una copia del decimal especificado para ir operando.
    cociente = decimal;

    # Cuando el cociente sea 0 no hay mas nada que hacer.

    while(cociente > 0):
        # concateno resto de division por 2 (bit 1 o 0).
        bin += str(int(cociente % 2));

        # avanzo obteniendo el cociente y reingresandolo a una division por 2.
        cociente //= 2;

    # una vez obtengo el binario, que esta al revés, aplico la regla del pasaje que dice
    # que se debe ordenar del ultimo resto obtenido al primero obtenido (11001 -> 10011)
    # Aca se usa un slice.
    bin = bin[::-1];
    
    return bin;

def decimalHexadecimal(decimal):
    cociente = decimal;
    resto = 0;
    hexa = "";

    # Que sea mayor igual a uno, dado el caso de que hayan decimales no acabaria o seria muy 
    # largo lo que devuelve
    while(cociente >= 1):
        # Guardo el resto de la division en un string.
        resto = cociente % 16;
        
        # Si es superior a 10, tenemos que reemplazar por una letra.
        # Caso que no sea mayor, ingresamos el numero de un digito.
        match(resto):
            case 10:
                hex = 'A';
            case 11:
                hex = 'B';
            case 12:
                hex = 'C';
            case 13:
                hex = 'D';
            case 14:
                hex = 'E';
            case 15:
                hex = 'F';
            case _:
                hex = str(resto);

        hexa += hex;
        
        # cuando el cociente sea 0, será nuestra condicion de corte.
        cociente //= 16;
    
    # Invertimos los resultados
    return hexa[::-1];

def decimalOctal(decimal):
    cociente = decimal;
    resto = 0;
    octal = "";

    # Que sea mayor igual a uno, dado el caso de que hayan decimales no acabaria o seria
    # muy largo lo que devuelve
    while(cociente >= 1):
        resto = cociente % 8;
        octal += str(int(resto));

        cociente /= 8;

    return octal[::-1];

def complementar(base, decimal):
    """
    Funcion para calcular el valor que falta para que al complementar ese numero
    este llegue al formato esperado.
    """
    # B^n – N -> la cantidad que falta al numero N segun la base B para el formato n 
    # (digitos del numero que estamos calculando).

    numeros = [];

    formato = str(decimal).__len__();

    faltan = (base ** formato) - decimal;

    numeros.append(faltan);
    numeros.append(formato);

    return numeros;

while(run):
    op = menu();
    print();

    match(op):
        case 0:
            run = False;
        
        case 1:
            bin = input("Ingrese el binario: ");
            print(f"El valor decimal del binario ingresado es: {binarioDecimal(bin)}\n");
        
        case 2:
            decimal = int(input("Ingrese un numero decimal entero: "));
            print(f"El valor binario del decimal ingresado es: {decimalBinario(decimal)}\n");
        
        case 3:
            decimal = int(input("Ingrese un numero decimal entero: "));
            print(f"La representacion hexadecimal del decimal ingresado es: {decimalHexadecimal(decimal)}")
            print(f"La representacion binaria del decimal ingresado es: {decimalBinario(decimal)}");
            print(f"La representacion octal del decimal ingresado es: {decimalOctal(decimal)}")
        case 4:
            decimal = int(input("Ingrese un numero decimal entero: "));
            
            nums = complementar(10, decimal);

            print(f"Faltan {nums[0]} para el formato {nums[1]}");

        case _: # Caso cualquiera
            print("Opcion no valida. \n\n");
    input("Presione enter para continuar...");






