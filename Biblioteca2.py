import json


def cargar_biblioteca():
    try:
        with open("biblioteca.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        return []


def guardar_biblioteca(biblioteca):
    with open("biblioteca.json", "w", encoding="utf-8") as archivo:
        json.dump(biblioteca, archivo, ensure_ascii=False, indent=4)

    print("Datos guardados correctamente.")


def agregar_libro(biblioteca):
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el autor del libro: ")

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor
    }

    biblioteca.append(nuevo_libro)

    print("Libro agregado correctamente.")


def mostrar_libros(biblioteca):
    if len(biblioteca) == 0:
        print("No hay libros registrados.")

    else:
        print("------ BIBLIOTECA ------")

        for libro in biblioteca:
            print("Título:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("-" * 20)


def buscar_libro(biblioteca):
    busqueda = input("Ingrese el título del libro: ")

    for libro in biblioteca:

        if libro["titulo"] == busqueda:
            print("\nLibro encontrado")
            print("Título:", libro["titulo"])
            print("Autor:", libro["autor"])
            break

    else:
        print("Libro no encontrado.")


def eliminar_libro(biblioteca):
    eliminar = input("Ingrese el título del libro a eliminar: ")

    for libro in biblioteca:

        if libro["titulo"] == eliminar:
            biblioteca.remove(libro)
            print("Libro eliminado correctamente.")
            break

    else:
        print("Libro no encontrado.")


def editar_libro(biblioteca):
    editar = input("Ingrese el título del libro que desea editar: ")

    for libro in biblioteca:

        if libro["titulo"] == editar:

            print(
                f"\nLibro encontrado: {libro['titulo']} por {libro['autor']}\n"
            )

            nuevo_titulo = input("Ingrese el nuevo título: ")
            nuevo_autor = input("Ingrese el nuevo autor: ")

            libro["titulo"] = nuevo_titulo
            libro["autor"] = nuevo_autor

            print("Libro editado correctamente.")
            break

    else:
        print("Libro no encontrado.")


# Cargar datos guardados
biblioteca = cargar_biblioteca()

ejecutando = True

while ejecutando:

    print("\n====== BIBLIOTECA ======")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Editar libro")
    print("6. Salir")
    print("========================")

    opcion = input("Seleccione una opción: ")
    print()


    if opcion == "1":

        agregar_libro(biblioteca)
        guardar_biblioteca(biblioteca)


    elif opcion == "2":

        mostrar_libros(biblioteca)


    elif opcion == "3":

        buscar_libro(biblioteca)


    elif opcion == "4":

        eliminar_libro(biblioteca)
        guardar_biblioteca(biblioteca)


    elif opcion == "5":

        editar_libro(biblioteca)
        guardar_biblioteca(biblioteca)


    elif opcion == "6":

        print("Hasta luego.")
        ejecutando = False


    else:

        print("Opción no válida.")
        