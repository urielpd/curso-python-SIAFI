
#Ingresar los números con este formato de ejemplo: 10e3 o 4e-3
x = input("Ingresa un número: ")
y = input("Ingresa otro número: ")

x = float(x)
y = float(y)

imaginario= complex(x,y)

print(imaginario.real,imaginario.imag,sep=" , ")

