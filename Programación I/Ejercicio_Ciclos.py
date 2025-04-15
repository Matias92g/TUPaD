num =  int((input)("ingrese un nro Positivo: "))

if num > 0:
    if num % 2 != 0:
        num -= 1
    cont = num
    while cont >= 0:
        print(cont, end=" ")
        cont -= 2
else:    print("El numero no es positivo")