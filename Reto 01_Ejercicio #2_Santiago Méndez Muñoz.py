#Ejercico 2
def reverse_chain(chain):  
    new_chain = ""
    for word in chain:
        new_chain = word + new_chain
    return new_chain

#En la funcion "reversed_chain" lo que hago es que creo un for para que la palbra que ingrese, 
#la lea al reves ya que va leyendo cada letra del objeto chain en orden, y luego las va agregando 
# a new_chain pero para que la palabra este al reves pues luego de agregar la primera letra, 
# agrega la sigueinte antes de la primera letra, y asi sucesivamente. Hasta que la ultima letra 
# esta antes que las otras, y la primer letra esta de ultimas

def palindrome(chain):
    return chain == reverse_chain(chain)

#Esta funcion "palindrome" lo que hace es que me dice si "chain" que es la palabra original es igual a
#"reversed_chain(chain)" que es la palabra al reves. Y si es cierto, me retorna un "true", y si no, 
#me retorna un "flase"

print("Ingrese su palabra: ")
term = str(input())

print(palindrome(reverse_chain(term)))