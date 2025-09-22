#Ejercicio 5
def filter_same_caracters(lista):
    groups = []          #Lista de grupos
    usados = set()       #Conjunto para guardar palabras ya agrupadas

    for i in range(len(lista)):
        word1 = lista[i]

        #Si ya está usada, la saltamos
        if word1 in usados:
            continue

        sorted1 = "".join(sorted(word1))
        group = [word1]
        usados.add(word1)   #La marcamos como usada

        #Buscamos otras palabras con los mismos caracteres con este for
        for j in range(i + 1, len(lista)):
            word2 = lista[j]
            sorted2 = "".join(sorted(word2))

            if sorted1 == sorted2:
                group.append(word2)
                usados.add(word2)  #La volvemos a marcar como usada

        # Si el grupo tiene más de un elemento, lo guardamos
        if len(group) > 1:
            groups.append(group)

    return groups


lista = []
list_size = int(input("Dígame el tamaño de la lista: "))
for i in range(list_size):
    word = input(f"Ingrese la palabra #{i+1}: ")
    lista.append(word)

print("Los grupos encontrados son:")
print(filter_same_caracters(lista))