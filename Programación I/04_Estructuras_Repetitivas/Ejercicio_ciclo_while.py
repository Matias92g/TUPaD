CORTE = "*"
nombre = input(f"Ingrese su nombre (o {CORTE} para terminar): ")
edad_minima= float("inf")

while nombre != CORTE:
    edad = int(input("Ingrese su edad: "))
    if edad < edad_minima:
        edad_minima = edad
        nombre_mas_joven = nombre
    elif edad == edad_minima:
        nombre_mas_joven += f", {nombre}"
    nombre = input(f"Ingrese otro nombre (o {CORTE} para terminar): ")
