# PRACTICA NRO 2
#  DEFINA EL SIGUIENTE DICCIONARIO "VENTAS "
ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_F",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

while True:
    print("\nBIENBENIDO AL MENÚ")
    print(
        """
        1. Mostrar el listado de ventas.
        2. Añadir un producto.
        3. Calcular la suma total de ventas.
        4. Calcular el promedio de la suma total de ventas.
        5. Mostrar el producto más vendido.
        6. Mostrar el listado de productos.
        7. Salir del menú"""
    )

    opcion = input("Ingrese la opción a elergir: ")

    match opcion:
        case "1":
            print("\nListado de ventas:")
            for i in ventas:
                print(i)
            continue
        case "2":
            fecha = input("Ingrese la fecha (dd-mm-yyyy): ")
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            precio = float(input("Ingrese el precio del producto: "))
            promocion = input("¿Está en promoción? (S/N): ")
            if promocion.upper == "s":
                promocion = True
            else:
                promocion = False
            nueva_venta = {
                "fecha": fecha,
                "producto": producto,
                "cantidad": cantidad,
                "precio": precio,
                "promocion": promocion
            }
            ventas.append(nueva_venta)
            print("\nProducto añadido exitosamente.")
            continue
        case "3":
            VentaTotal = sum(i["cantidad"]*i["precio"] for i in ventas)
            print(f"La suma total de ventas es: ${VentaTotal}")
            continue
        case "4":
            VentaTotal = sum(i["cantidad"]*i["precio"] for i in ventas)
            Promedio = VentaTotal/len(ventas)
            print(f"\nEl promedio de la suma total de ventas es: ${Promedio}")
            continue
        case "5":
            Cantidad = [i["cantidad"] for i in ventas]
            CantidadMaxima = max(Cantidad)
            print(f"\nLa cantidad máxima es: {CantidadMaxima} u") 
            continue
        case "6":
            ListadoProductos = set(i["producto"] for i in ventas)
            for a in ListadoProductos:
                print([a])
            continue
        case "7":
            break
        case default: 
            print("\nIngrese una de las opciones.")
