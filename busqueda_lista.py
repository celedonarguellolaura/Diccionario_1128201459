# Ejercicio 2: Búsqueda en Lista

numeros = [12, 45, 78, 23, 56, 89, 34, 67]

def buscar_numero(numero):
    """Devuelve el índice del número en la lista, o -1 si no existe."""
    try:
        return numeros.index(numero)
    except ValueError:
        return -1

def numeros_mayores(umbral):
    """Devuelve una lista con los números mayores que el umbral."""
    return [n for n in numeros if n > umbral]

def promedio_lista(lista):
    """Devuelve el promedio de los elementos de la lista."""
    if not lista:
        return 0
    return sum(lista) / len(lista)

def ordenar_lista(lista):
    """Devuelve la lista ordenada de menor a mayor."""
    return sorted(lista)

def menu():
    while True:
        print("\nLista de números:", numeros)
        print("1. Buscar número")
        print("2. Números mayores que un umbral")
        print("3. Promedio de la lista")
        print("4. Ordenar lista")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            n = int(input("Número a buscar: "))
            idx = buscar_numero(n)
            if idx != -1:
                print(f"El número {n} está en la posición {idx}.")
            else:
                print(f"El número {n} no está en la lista.")
        elif opcion == "2":
            u = int(input("Umbral: "))
            mayores = numeros_mayores(u)
            print("Números mayores que", u, ":", mayores)
        elif opcion == "3":
            prom = promedio_lista(numeros)
            print(f"El promedio es: {prom:.2f}")
        elif opcion == "4":
            ordenada = ordenar_lista(numeros)
            print("Lista ordenada:", ordenada)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
