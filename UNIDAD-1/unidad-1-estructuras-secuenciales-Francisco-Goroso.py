# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre ")

print(f'Hola {nombre}')


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
# 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# A DISTANCIA

nombre = input("Ingresa tu nombre ")
apellido = input("Ingresa tu apellido ")
edad = input("Ingresa tu edad ")
residencia = input("Ingresa el lugar en donde resides ")


print(f'Hola, soy {nombre} {apellido}, tengo {edad} años y vivo actualmente en {residencia}')

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

pi = 3.1416

radio = float(input("Ingresa el radio del circulo: "))

area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"Area: {area}")
print(f"Perimetro: {area}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Coloca una cantidad de segundos asi calculo las hora que equivalen esos segundos"))

horas = segundos / 3600

 
print(f"Los segundos que colocaste, quivalen a {horas}")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Ingresa un numero y te paso toda su tabla de multiplicar "))
resultado = 0

for i in range(1, 11):      
    resultado = numero * i  
    print(f"{numero} X {i} = {resultado}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numeroUno = int(input("Ingresa un numero distinto de cero y voy a mostrarte el resultado de las operaciones basicas aplicados entre estos 2 numeros "))
numeroDos = int(input("Ingresa el otro numero para hacer la operacion "))

numerosSumados = numeroUno + numeroDos
numerosDivididos = numeroUno / numeroDos
numerosMultiplicados = numeroUno * numeroDos
numerosRestados = numeroUno - numeroDos

print(f"""El resultado de las operaciones básicas con los números que me pasaste, son los siguientes:
SUMADOS: {numerosSumados}
MULTIPLICADOS: {numerosMultiplicados}
DIVIDIDOS: {numerosDivididos}
RESTADOS: {numerosRestados}""")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
# (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

altura = float(input("Ingresa tu altura en metros "))
peso = float(input("Ingresa tu peso en kg "))

IMC = peso / (altura ** 2)

print(f"Tu índice de masa corporal (IMC) es: {IMC}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9
# 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temperaturaCelsius = float(input("Ingresa una temperatura en Celsius y la convierto en Fahrenheit "))
temperaturaFar = (temperaturaCelsius * 1.8) + 32

print(f"La temperatura en celsius: {temperaturaCelsius}, equivale a {temperaturaFar} grados Fahrenheit")
# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

numeroUno = int(input("Ingresa un numero "))
numeroDos = int(input("Ingresa otro numero "))
numeroTres = int(input("Ingresa el ultimo numero "))

promedio = (numeroUno + numeroDos + numeroTres) / 3 
print(f"El promedio de los 3 numeros que me pasaste es: {promedio}")


