# Práctica 3: Productos y productos en oferta

**Materia:** Programación Avanzada  
**Unidad:** Herencia, polimorfismo y sobrecarga  
**Archivo principal:** `productos_oferta.py`

## Descripción

Programa de consola para administrar información básica de productos. Incluye una clase `Producto` con precio privado, una clase derivada `ProductoOferta` y una prueba de comparación entre objetos con el operador `==`.

## Conceptos aplicados

- **Encapsulamiento:** el precio se almacena en el atributo privado `__precio` y se consulta con `consultar_precio()`.
- **Validación:** `modificar_precio()` acepta únicamente precios mayores que cero y rechaza los valores no válidos.
- **Herencia:** `ProductoOferta` deriva de `Producto` y agrega el porcentaje de descuento.
- **Sobrescritura:** `ProductoOferta` redefine `mostrar_informacion()` para mostrar el precio original, el descuento y el precio final.
- **Sobrecarga de operador:** `__eq__()` permite comparar productos con `==`. Se consideran iguales cuando tienen el mismo nombre y el mismo precio; el stock no interviene en la comparación.

## Cómo ejecutar

Requiere Python 3 y no necesita instalar bibliotecas adicionales.

```bash
python productos_oferta.py
```

En algunos sistemas, utiliza `python3 productos_oferta.py`.

## Pruebas incluidas

1. Consultar el precio mediante un método.
2. Modificar el precio con un valor válido.
3. Intentar establecer un precio de cero y comprobar que se rechaza.
4. Crear un `ProductoOferta` y mostrar el descuento y el precio final.
5. Comparar productos diferentes y productos con el mismo nombre y precio mediante `==`.
