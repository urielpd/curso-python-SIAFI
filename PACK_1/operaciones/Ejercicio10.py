from math import sqrt

A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el término independiente\n"))

if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con numeros complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte positiva
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte negativa
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)
