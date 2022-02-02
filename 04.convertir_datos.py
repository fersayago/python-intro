numero_1 = input("Ingrese el primer numero")
print(numero_1)

numero_2 = input("Ingrese el segundo numero")
print(numero_2)

mal_resultado = numero_1 + numero_2
print(f"suma mal hecha ya que los toma como strings: {mal_resultado}")

# para pasar un numero de string a int se usa int

resultado_correcto = int(numero_1) + int(numero_2)
print(f"suma correcta luego de convertir a int: {resultado_correcto}")

# para pasar un numero a string se usa str