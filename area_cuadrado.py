# Calcula el area de un cuadrado

# Solicitamos el dato al usuario
lado = float(input("Ingrese en centimetros la longitud de un lado del cuadrado: "))

# Calculamos el area del cuadrado
area = lado * lado

# Mostramos el resultado
print(f"El area del cuadrado con lado {lado} es: {area}.")

# Tambien podemos calcular el perimetro
print("Tambien podemos calcular el perimetro del cuadrado...")

perimetro = lado * 4

print(f"El perimetro del cuadrado con lado {lado} es: {perimetro}.")
