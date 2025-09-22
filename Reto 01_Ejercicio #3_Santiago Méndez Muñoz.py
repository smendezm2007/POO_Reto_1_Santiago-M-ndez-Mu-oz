#Ejercicio 3
def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#Aqui, creo una funcion llamada "prime" la cual me va a decir si un
#numero es primo o no. Los numeros primos son mayores o iguales que
#dos, por esa razon si es menor, no es primo. Luego en el for se mira
#si el numero solo es divisible entre 1 y el mismo. Ya que de lo
#contrario, no es primo.

def list(list_amount):
    number_list = []
    prime_number = []
    

    for i in range(list_amount):
        element = int(input(f"Ingrese el numero #{i+1}: "))
        number_list.append(element)

        if prime(element):
            prime_number.append(element)
    
    print("La lista original es: ")
    print(number_list)
    print("La lista de numeros primos es: ")
    print(prime_number)

#En esta funcion "list" lo que hago es que creo un for para hacer la lista original de numeros
#y luego creo otra lista de numeros llamada "prime_list" en la cual van a ir los numeros primos
#de la lista original
#En la linea 21 y 22 llamo a la funcion "prime" para que revise si los elementos o numeros de
#la lista original o "number_list" son primos; y si son, los agrega a la lista "prime_number"

new_list_amount = int(input("Ingrese la cantidad de numeros de la lista: "))
print(list(new_list_amount))

