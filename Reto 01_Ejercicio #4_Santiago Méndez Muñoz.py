#Ejercicio 4
def list(list_amount):
    number_list = []
    
    for i in range(list_amount):
        element = int(input(f"Ingrese el numero #{i+1}: "))
        number_list.append(element)

 
    print("La lista original es: ")
    print(number_list)

    max_add = 0
    new_j = 0
    for j in range(list_amount-1):
        current_add = number_list[j] + number_list[j+1]
        if current_add > max_add:
            max_add = current_add
            new_j = j

    #En este for, va a recorrer todas las posicicones de la lista, y como el primer valor esta en la posicion [0], tengo que 
    #restar 1 a el numero total de elementos de la lista. Y luego comparo la suma de numeros consecutivos de la lista. Para
    #asi hallar la mayor suma
    
    print("La suma mayor entre los numeros consecutivos", number_list[new_j], " y ", number_list[new_j+1], " es igual a: ", max_add)

new_list_amount = int(input("Ingrese la cantidad de numeros de la lista: "))

print(list(new_list_amount))
