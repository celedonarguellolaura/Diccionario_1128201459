# Gestor de Compras

"""
Programa que gestiona una lista de artículos de compra.
Cada artículo es un diccionario con: producto, precio y cantidad.
"""

compras = []

def agregar_articulo():
    producto = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    articulo = {"producto": producto, "precio": precio, "cantidad": cantidad}
    compras.append(articulo)
    print(f"Artículo '{producto}' agregado.")

def ver_lista():
    if not compras:
        print("La lista de compras está vacía.")
    else:
        print("\nLista de compras:")
        for i, articulo in enumerate(compras, 1):
            print(f"{i}. {articulo['producto']} - Precio: {articulo['precio']} x Cantidad: {articulo['cantidad']}")

def calcular_total():
    total = 0
    for articulo in compras:
        total += articulo['precio'] * articulo['cantidad']
    print(f"Total a pagar: ${total:.2f}")

def eliminar_articulo():
    nombre = input("Nombre del producto a eliminar: ")
    for articulo in compras:
        if articulo['producto'] == nombre:
            compras.remove(articulo)
            print(f"Artículo '{nombre}' eliminado.")
            return
    print(f"No se encontró el producto '{nombre}'.")

def menu():
    while True:
        print("\nGestor de Compras")
        print("1. Agregar artículo")
        print("2. Ver lista de compras")
        print("3. Calcular total")
        print("4. Eliminar artículo")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_articulo()
        elif opcion == "2":
            ver_lista()
        elif opcion == "3":
            calcular_total()
        elif opcion == "4":
            eliminar_articulo()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
