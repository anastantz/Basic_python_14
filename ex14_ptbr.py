# Programa que converte uma temperatura de graus Celsius para Fahrenheit

celsius = float(input("Informe a temperatura em °C: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"A temperatura de {celsius:.1f}°C corresponde a {fahrenheit:.1f}°F.")