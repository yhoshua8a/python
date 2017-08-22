

try:
    num1 = int(input("Dame el primer numero"))
    num2 = int(input("Dame el segundo numero"))

except ValueError:
    print("ocurrio un error solo se aceptan numeros")

else:

    suma = num1 + num2

    print("La suma es " + str(suma))