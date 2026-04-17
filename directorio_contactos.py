# Ejercicio 3: Directorio de Contactos

directorio = {}

def agregar_contacto():
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    ciudad = input("Ciudad: ")
    directorio[nombre] = {
        "email": email,
        "telefono": telefono,
        "ciudad": ciudad
    }
    print(f"Contacto '{nombre}' agregado.")

def ver_contactos():
    if not directorio:
        print("No hay contactos.")
    else:
        print("\nDirectorio de Contactos:")
        for nombre, datos in directorio.items():
            print(f"- {nombre}: Email: {datos['email']}, Teléfono: {datos['telefono']}, Ciudad: {datos['ciudad']}")

def buscar_por_nombre():
    nombre = input("Nombre a buscar: ")
    datos = directorio.get(nombre)
    if datos:
        print(f"Datos de {nombre}: Email: {datos['email']}, Teléfono: {datos['telefono']}, Ciudad: {datos['ciudad']}")
    else:
        print(f"No se encontró el contacto '{nombre}'.")

def actualizar_telefono():
    nombre = input("Nombre del contacto a actualizar: ")
    if nombre in directorio:
        nuevo_tel = input("Nuevo teléfono: ")
        directorio[nombre]["telefono"] = nuevo_tel
        print(f"Teléfono de '{nombre}' actualizado.")
    else:
        print(f"No se encontró el contacto '{nombre}'.")

def eliminar_contacto():
    nombre = input("Nombre del contacto a eliminar: ")
    if directorio.pop(nombre, None):
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"No se encontró el contacto '{nombre}'.")

def menu():
    while True:
        print("\nDirectorio de Contactos")
        print("1. Agregar contacto")
        print("2. Ver todos los contactos")
        print("3. Buscar por nombre")
        print("4. Actualizar teléfono")
        print("5. Eliminar contacto")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            ver_contactos()
        elif opcion == "3":
            buscar_por_nombre()
        elif opcion == "4":
            actualizar_telefono()
        elif opcion == "5":
            eliminar_contacto()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
