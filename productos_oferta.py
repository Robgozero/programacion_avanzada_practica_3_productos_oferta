# Unidad 3: Herencia, polimorfismo y sobrecarga
# Práctica 3: Productos y productos en oferta


class Producto:
    """Representa un producto y encapsula su precio."""

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = 0
        self.stock = stock

        if not self.modificar_precio(precio):
            raise ValueError("El precio inicial debe ser mayor que cero.")

    def consultar_precio(self):
        """Devuelve el precio actual del producto."""
        return self.__precio

    def modificar_precio(self, nuevo_precio):
        """Modifica el precio únicamente si el valor es mayor que cero."""
        if nuevo_precio <= 0:
            print("Error: el precio debe ser mayor que cero.")
            return False

        self.__precio = nuevo_precio
        print(f"Precio de '{self.nombre}' actualizado a ${self.__precio:.2f}.")
        return True

    def mostrar_informacion(self):
        """Muestra la información básica del producto."""
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.__precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def __eq__(self, otro):
        """Dos productos son iguales si coinciden nombre y precio."""
        if not isinstance(otro, Producto):
            return NotImplemented

        return (
            self.nombre == otro.nombre
            and self.__precio == otro.consultar_precio()
        )


class ProductoOferta(Producto):
    """Producto que incluye un descuento porcentual."""

    def __init__(self, nombre, precio, stock, descuento):
        super().__init__(nombre, precio, stock)

        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        self.descuento = descuento

    def mostrar_informacion(self):
        """Sobrescribe el método para incluir descuento y precio final."""
        precio_original = self.consultar_precio()
        precio_final = precio_original * (1 - self.descuento / 100)

        return (
            f"Producto en oferta: {self.nombre} | "
            f"Precio original: ${precio_original:.2f} | "
            f"Descuento: {self.descuento}% | "
            f"Precio final: ${precio_final:.2f} | "
            f"Stock: {self.stock}"
        )


def main():
    print("=== Práctica 3: Productos y ofertas ===")

    # Crear productos
    producto1 = Producto("Teclado", 450.00, 12)
    producto2 = Producto("Teclado", 450.00, 8)
    producto3 = Producto("Mouse", 250.00, 20)

    # Consultar precio usando el método de la clase
    print("\\n1. Consulta de precio:")
    print(f"Precio de {producto1.nombre}: ${producto1.consultar_precio():.2f}")

    # Modificación válida
    print("\\n2. Modificación válida del precio:")
    producto1.modificar_precio(475.00)
    print(producto1.mostrar_informacion())

    # Rechazo de precio no válido
    print("\\n3. Rechazo de precio no válido:")
    producto1.modificar_precio(0)
    print(f"Precio actual: ${producto1.consultar_precio():.2f}")

    # Producto derivado y sobrescritura
    print("\\n4. Producto en oferta:")
    oferta = ProductoOferta("Audífonos", 800.00, 6, 15)
    print(oferta.mostrar_informacion())

    # Sobrecarga del operador ==
    print("\\n5. Comparación de productos con ==:")
    print(f"producto2 == producto3: {producto2 == producto3}")
    producto4 = Producto("Teclado", 450.00, 99)
    print(f"producto2 == producto4: {producto2 == producto4}")


if __name__ == "__main__":
    main()
