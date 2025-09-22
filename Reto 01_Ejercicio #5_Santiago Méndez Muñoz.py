def filter_same_caracters(list):
    groups = []   # lista de grupos (cada grupo será otra lista)

    for i in range(len(list)):
        word1 = list[i]
        sorted1 = "".join(sorted(word1))
        group = [word1]

        # Buscar otras palabras que tengan los mismos caracteres
        for j in range(i + 1, len(list)):
            word2 = list[j]
            sorted2 = "".join(sorted(word2))

            if sorted1 == sorted2:
                group.append(word2)

        # Si el grupo tiene más de un elemento, lo guardamos
        if len(group) > 1:
            groups.append(group)

    return groups

list = []
list_size = int(input("Digame el tamaño de la lista: "))
for i in range(list_size):
    word = str(input(f"Ingrese la palabra #{i+1}: "))
    list.append(word)


print(filter_same_caracters(list))
