numeroReal = float(input("Ingresa la parte real del número complejo: "))
numeroImag = float(input("Ingresa la parte imaginaria del número complejo: "))
imaginario = complex(numeroReal, numeroImag)
print(imaginario.real,imaginario.imag,sep=" , ")
