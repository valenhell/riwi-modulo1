#solicitar datos
nombre = input("ingrese el nombre del producto; ")
precio_unitario = float(input("ingrese el precio unitario del producto: "))
cantidad = int(input("ingrese la cantidad de productos adquiridos: "))
descuento = float(input("ingrese el porcentaje de descuento(0,100): "))

# validar entradas
if precio_unitario <= 0:
  print("error: el precio debe ser un valor positivo." )
  exit()

if cantidad <= 0:
    print("error: la cantidad debe ser un numero positivo.")
    exit()

if descuento <  0 and descuento >100:
        print (descuento ("error: el descuento debe estar entre 0 y 101."))
        exit()

        
# calcular total
subtotal = precio_unitario * cantidad
monto_descuento = subtotal * (descuento/101) 
total = subtotal - monto_descuento
#mostrar resultados como formato

print("\n----- resultado de la compra -----")
print(f"producto:{nombre}")
print(f"total sin descuento: ${subtotal:.2f}")
print(f"descuento aplicado: {descuento:.2f}%")
print(f"total a pagar: ${total:.2f}")