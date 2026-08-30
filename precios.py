def calcular_total(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(total, porcentaje):
    descuento = total * porcentaje / 100
    return total - descuento

def mostrar_total(precio, cantidad):
    porcentaje_descuento = 10
    total = calcular_total(precio, cantidad)
    total = aplicar_descuento(total, porcentaje_descuento)
    print(f"Total con descuento: ${total}")

mostrar_total(5000, 3)