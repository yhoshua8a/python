lista = [1,2,3,4,5]

#concatenar lista a lista actual
#salida [1, 2, 3, 4, 5, 6, 7, 8]
lista = lista + [6,7,8]
print(lista)

#agregar elemento a lista
#salida [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.append(9)
print(lista)

#agregar lista dentro de una lista, append solo agrega un elemento a la lista
#salida [1, 2, 3, 4, 5, 6, 7, 8, 9, [2, 3, 4]]
lista.append([2,3,4])
print(lista)

#agregar mas de un elemento a la lista con extends
#salida [1, 2, 3, 4, 5, 6, 7, 8, 9, [2, 3, 4], 10, 11]
lista.extend([10,11])
print(lista)

#remover elemento de lista
#salida [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
lista.remove([2,3,4])
print(lista)

#crear lista con metodo list, separa la cadena de texto en caracteres y agrega a lista
#salida ['y', 'h', 'o', 's', 'h', 'u', 'a']
lista_nombre = list("yhoshua")
print(lista_nombre)

#agregar cadena como elemento de lista
#salida ['yhoshua', 'alejandro']
lista_nombres =  "yhoshua alejandro".split()
print(lista_nombres)

#juntando elemetos de lista en una cadena con el emtodo join
#salida yhoshua alejandro
separador = " "
nombre = separador.join(lista_nombres)
print(nombre)