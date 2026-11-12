#Gestión de INVENTARIO en Python
#El inventario lo vamos a almacenar en una clase

class Producto:
    idContador = 0
    def __init__(self,nombre, precio, stock, categoria):
        Producto.idContador+=1
        self.id = Producto.idContador
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria


#Necesitamos un menú con las siguientes opciones:
#1. Agregar producto
#Primero crearemos la función crear_producto que nos permitirá crear un producto
def crear_producto(nombre: str, precio: float, stock: int, categoria: str):
    return Producto(nombre, precio, stock, categoria)
def agregar_producto(producto: Producto, inventario: list):
    inventario.append(producto)
    return f"Producto {producto.nombre} agregado al inventario."
#2. Actualizar stock
#Hay que hacer una función para encontrar el producto por el ID
def encontrar_producto_por_id(inventario: list, id_producto: int):
    #Variable para saber si el producto está o no dentro de la lista
    encontrado = False
    #Instanciamos una variable p como None
    p = None
    #Realizamos un bucle for para encontrar el producto e instanciarlo
    for producto in inventario:
        if producto.id == id_producto:
            #Igualamos p con producto aprovechando el tipado dinámico de Python
            p = producto
            encontrado = True
            break
        else:
            encontrado = False
    if encontrado:
        return p
    else:
        return f"No se ha encontrado el producto con ID {id_producto}"

#Ahora hay que hacer la función para actualizar el stock
def actualizar_stock(id_producto: int, nuevo_stock: int,inventario: list, orden: str):
    #Buscamos el producto por su id
    producto = encontrar_producto_por_id(inventario,id_producto)
    if type(producto) != Producto:
        #Devolvemos producto si no existe para que salte el mensaje de error
        return producto
    elif orden == "AÑADIR":
        producto.stock += nuevo_stock
    elif orden == "RESTAR":
        producto.stock -= nuevo_stock
    else:
        return f"Orden {orden} no reconocida"
    return f"Stock actualizado correctamente: {producto.stock}"

#3. Buscar producto por categoría
def buscar_producto_por_categoria(categoria: str, inventario: list):
    mapaProducto = {categoria: []}
    for producto in inventario:
        if producto.categoria == categoria:
            mapaProducto[categoria].append(producto)
    return mapaProducto

#4. Calcular valor total de la tienda
# Para realizar esta función necesitamos recorrer el inventario y multiplicar el precio por el stock de cada producto
# Cada resultado lo vamos a ir almacenando en una variable llamada "total" y es lo que devolveremos al final
def calcular_valor_total(inventario: list):
    total = 0
    for producto in inventario:
        total += producto.precio * producto.stock
    return f"El inventario tiene un valor total de {total}€"

#5. Mostrar los productos disponibles
def mostrar_inventario(inventario: list):
    #Recorremos el inventario para mostrar los productos
    print("Productos dentro del inventario: ")
    for producto in inventario:
        print(f"{producto.id}-{producto.nombre} - {producto.precio} - {producto.stock} - {producto.categoria}")
#Ahora creamos nuestro menú para que el usuario pueda interactuar con el inventario
def menu():
    # Aqui mostraremos las opciones del menú
    print("1. Añadir un producto al inventario")
    print("2. Actualizar el stock")
    print("3. Buscar producto por categoría")
    print("4. Calcular valor total del inventario")
    print("5. Mostrar productos")
    print("6. Salir")

# Ahora escribiremos la función principal que será la que inicie la lógica de negocio
def iniciar_app():
    # Crearemos una lista con el inventario disponible actualmente
    # NOTA: incluiré también una versión donde podamos añadir los productos desde un archivo .csv
    inventario = []
    opcion: int = 0
    while opcion != 6:
        menu()
        opcion = int(input("Introduce una opción "))
        match opcion:
            #Añadir el producto al inventario
            case 1:
                nombre = input("Introduce el nombre del producto: ")
                try:
                    precio = float(input("Introduce el precio del producto: "))
                except ValueError:
                    print("El precio debe ser de tipo decimal (con o sin decimales)")
                try:
                    stock = int(input("Introduce el stock actual del producto: "))
                except ValueError:
                    print("El stock debe ser de tipo entero")
                categoria = input("Introduce la categoría del producto: ")
                producto = crear_producto(nombre, precio, stock, categoria)
                print(agregar_producto(producto, inventario)+"\n")
            #Actualizar el stock de un producto
            case 2:
                if len(inventario) == 0:
                    print("El inventario se encuentra vacio")
                else:
                    id_producto = int(input("Introduce el id del producto: "))
                    nuevo_stock = int(input("Introduce la cantidad que quieras actualizar para el stock: "))
                    orden = input("Introduzca por texto la orden (AÑADIR - RESTAR): ")
                    print(actualizar_stock(id_producto,nuevo_stock,inventario,orden)+"\n")
            #Buscar producto por categoría
            case 3:
                if len(inventario) == 0:
                    print("El inventario se encuentra vacio")
                else:
                    categoria = input("Introduce la categoría la cual quieras encontrar los productos: ")
                    print(buscar_producto_por_categoria(categoria,inventario)+"\n")
            #Calcular valor total del inventario
            case 4:
                if len(inventario) == 0:
                    print("El inventario se encuentra vacio")
                else:
                    print(calcular_valor_total(inventario)+"\n")
            #Mostrar la lista de productos
            case 5:
                if len(inventario) == 0:
                    print("El inventario se encuentra vacio")
                else:
                    mostrar_inventario(inventario)
            #Salir del programa con un mensaje de agradecimiento
            case 6:
                print("Gracias por usar mi software de gestión. Hasta pronto!!!")
            #Caso por defecto por si no ponemos la opción correcta
            case _:
                print(f"\nOpción {opcion} no reconocida\n")

iniciar_app()