Este proyecto es una aplicación de consola desarrollada en Python para la administración básica de un inventario de productos. Permite realizar operaciones esenciales de control de stock, valoración económica y filtrado de artículos mediante un menú interactivo.

## 🏗️ Estructura de Datos: Clase `Producto`

El núcleo del sistema se basa en la programación orientada a objetos a través de la clase **`Producto`**, la cual modela cada artículo almacenado en el inventario.

### Atributos de Clase

* `idContador` (`int`): Variable estática que lleva el conteo global de productos creados para asignar identificadores únicos automáticamente.

### Atributos de Instancia

* `id` (`int`): Identificador único autoincremental asignado al instanciar el producto.

* `nombre` (`str`): Nombre descriptivo del artículo.

* `precio` (`float`): Valor monetario unitario del producto.

* `stock` (`int`): Cantidad de unidades disponibles actualmente en el inventario.

* `categoria` (`str`): Clasificación o grupo al que pertenece el artículo.

## ⚙️ Funcionalidades del Programa

La aplicación cuenta con un menú interactivo en consola (`iniciar_app()`) que ofrece las siguientes operaciones:

1. **Añadir un producto al inventario (`crear_producto` / `agregar_producto`)**:

   * Solicita al usuario los datos del nuevo artículo (nombre, precio, stock inicial y categoría).

   * Incluye validación básica de tipos de datos (`float` para el precio e `int` para el stock) mediante bloques `try-except`.

   * Instancia el objeto `Producto` y lo almacena en la lista principal del inventario.

2. **Actualizar el stock (`encontrar_producto_por_id` / `actualizar_stock`)**:

   * Localiza un producto específico utilizando su `ID` único.

   * Permite incrementar (`AÑADIR`) o decrementar (`RESTAR`) la cantidad de unidades disponibles en tiempo real.

   * Valida si el inventario está vacío, si el `ID` existe o si la orden introducida es válida.

3. **Buscar producto por categoría (`buscar_producto_por_categoria`)**:

   * Filtra todos los productos registrados que coincidan con una categoría específica ingresada por el usuario.

   * Devuelve un diccionario (`mapaProducto`) donde la clave es la categoría buscada y el valor es la lista de objetos `Producto` coincidentes.

4. **Calcular valor total del inventario (`calcular_valor_total`)**:

   * Recorre todo el listado de productos multiplicando el `precio` unitario por el `stock` disponible de cada uno.

   * Retorna el valor económico total acumulado de la tienda expresado en euros (`€`).

5. **Mostrar productos disponibles (`mostrar_inventario`)**:

   * Despliega en consola un listado detallado de todos los artículos registrados, mostrando su `ID`, `nombre`, `precio`, `stock` y `categoría`.

6. **Salir del sistema**:

   * Finaliza la ejecución del bucle principal del programa de forma controlada.

## 🚀 Cómo ejecutar el proyecto

1. Asegúrate de tener **Python 3.10 o superior** instalado en tu sistema (necesario para el soporte de la estructura `match-case` utilizada en el menú).

2. Clona o descarga este repositorio.

3. Ejecuta el archivo principal desde tu terminal:

```bash
python gestioninventario.py
```

## 🔮 Estado del Proyecto y Próximas Actualizaciones

> **Nota importante:** Este software se encuentra en desarrollo activo y **seguirá recibiendo actualizaciones** periódicas para mejorar su rendimiento, manejo de excepciones y persistencia de datos (como la futura integración para importar y exportar inventarios mediante archivos `.csv`).
>
> Actualmente, **se está desarrollando el frontend** de la aplicación para ofrecer una interfaz gráfica intuitiva y moderna que complementará la lógica de negocio actual.