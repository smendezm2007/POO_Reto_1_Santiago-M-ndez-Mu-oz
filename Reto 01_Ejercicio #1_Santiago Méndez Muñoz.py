#Ejercicio 1
def OperacionesBasicas(n1 : float, n2 : float, caracter : str):
    if caracter == "+":
        Suma = n1 + n2
        print("La suma entre ", n1, "y", n2, " es: ", Suma)

    elif caracter == "-":
        Resta = n1 - n2
        print("La resta entre ", n1, "y", n2, " es: ", Resta)

    elif caracter == "*":
        Multiplicacion = n1 * n2
        print("La multiplicacion entre ", n1, "y", n2, " es: ", Multiplicacion)

    elif caracter == "/":
        Division = n1 / n2
        print("La division entre ", n1, "y", n2, " es: ", Division)
                
    else:
        print("El caracter no es valido")


print("Digame el primer numero: ")   
number1 = float(input())
print("Digame el segundo numero: ")
number2 = float(input())
print("Digame el caracter de la operacion basica que desea realizar: ")
caracter_operacion = str(input())

print(OperacionesBasicas(number1, number2, caracter_operacion))