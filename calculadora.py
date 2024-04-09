def calcular_descuento(forma_pago, precio_con_iva):
    """
    Función para calcular el descuento según la forma de pago.
    """
    descuento = 0
    if forma_pago.lower() == 'efectivo':
        descuento = precio_con_iva * 0.10
    elif forma_pago.lower() == 'tarjeta de credito':
        descuento = precio_con_iva * 0.05
    elif forma_pago.lower() == 'vale de regalo':
        descuento = precio_con_iva * 0.15
    return descuento


def generar_detalle_pago(cantidad_impresoras, forma_pago):
    """
    Función para generar el detalle del pago.
    """
    precio_unitario_con_iva = 80000 * 1.16  # Precio unitario con IVA
    total_sin_descuento = cantidad_impresoras * precio_unitario_con_iva
    descuento = calcular_descuento(forma_pago, total_sin_descuento)
    total_a_pagar = total_sin_descuento - descuento

    detalle_pago = {
        "Cantidad de impresoras": cantidad_impresoras,
        "Precio unitario con IVA": precio_unitario_con_iva,
        "Total sin descuento": total_sin_descuento,
        "Forma de pago": forma_pago,
        "Descuento realizado": descuento,
        "Total a pagar": total_a_pagar
    }
    return detalle_pago


def main():
    try:
        cantidad = int(input("Ingrese la cantidad de impresoras a comprar: "))
        forma_pago = input("Seleccione la forma de pago (Efectivo/Tarjeta de credito/Vale de regalo): ")

        detalle_pago = generar_detalle_pago(cantidad, forma_pago)

        print("\nDetalle del pago:")
        for clave, valor in detalle_pago.items():
            print(f"{clave}: {valor}")
    except ValueError:
        print("Error: La cantidad de impresoras debe ser un número entero.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")


if __name__ == "__main__":
    main()