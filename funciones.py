def suma(a,b):
    suma = a+b
    return suma

def resta(a,b):
    resta = a - b
    return resta

def multiplicacion(a,b):
    mult = a*b
    return mult

#ESTE CODIGO SIMULA EL COMPORTAMIENTO DE UN SWITCH
operaciones = { 'suma': suma(2,3), 'resta': resta(3,2), 'multiplicacion':multiplicacion(3,2) }
opcion = 'multiplicacion'
res = operaciones[opcion]
print("La operacion "+ str(opcion)+ "es " + str(res))
