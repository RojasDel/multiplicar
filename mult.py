# Necesitamos pedir al usuario un mumero a multiplicar
num1 = int(input('Ingrese el numero a multiplicar: '))


def tabla_multi1 (num1, multiplo = 1):
    # Iniciamos la multiplicacion por los primero 10 numeros
    if multiplo > 10:
        #Caso base
        return 
    resultado = num1 *multiplo
    print(f"{num1} x {multiplo} = {resultado}")
    #Paso recursivo
    tabla_multi1(num1, multiplo + 1)

tabla_multi1(num1)

