# =============================================
# SISTEMA DE GESTIÓN DE INVENTARIOS
# =============================================
# Este sistema utiliza polimorfismo, clases abstractas e interfaces
# para manejar diferentes tipos de productos en un inventario.

from abc import ABC, abstractmethod  # Importamos para crear clases abstractas
from datetime import datetime
from typing import List, Optional
import json

# =============================================
# CLASE ABSTRACTA PRODUCTO
# =============================================
# Define la estructura base para todos los productos en el inventario
# Implementa el concepto de clase abstracta con ABC

class Producto(ABC):
    """
    Clase abstracta que define la estructura común de todos los productos.
    Utiliza ABC (Abstract Base Class) para garantizar que no se pueda instanciar directamente.
    """
    
    # Atributos estáticos para generar IDs únicos
    _ultimo_id = 0
    
    def __init__(self, nombre: str, precio: float, cantidad: int, categoria: str):
        """
        Constructor de la clase Producto.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio unitario
            cantidad (int): Cantidad en inventario
            categoria (str): Categoría general del producto
        """
        Producto._ultimo_id += 1
        self._id = Producto._ultimo_id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        self.fecha_registro = datetime.now()
        
    @property
    def id(self) -> int:
        """Getter para el ID del producto (lectura única)"""
        return self._id
    
    # =============================================
    # MÉTODOS ABSTRACTOS - Deben ser implementados por las subclases
    # =============================================
    
    @abstractmethod
    def calcular_valor_inventario(self) -> float:
        """
        Método abstracto que calcula el valor total del producto en inventario.
        Cada subclase implementará su propia lógica.
        
        Returns:
            float: Valor total del inventario para este producto
        """
        pass
    
    @abstractmethod
    def obtener_informacion(self) -> str:
        """
        Método abstracto que retorna información detallada del producto.
        
        Returns:
            str: Información formateada del producto
        """
        pass
    
    @abstractmethod
    def aplicar_descuento(self, porcentaje: float) -> float:
        """
        Método abstracto para aplicar descuento al producto.
        
        Args:
            porcentaje (float): Porcentaje de descuento a aplicar
            
        Returns:
            float: Nuevo precio después del descuento
        """
        pass
    
    # =============================================
    # MÉTODOS CONCRETOS - Comunes a todos los productos
    # =============================================
    
    def actualizar_stock(self, cantidad: int) -> bool:
        """
        Actualiza la cantidad de stock disponible.
        
        Args:
            cantidad (int): Cantidad a agregar o restar (positivo para agregar, negativo para restar)
            
        Returns:
            bool: True si la operación fue exitosa, False si no hay suficiente stock
        """
        nueva_cantidad = self.cantidad + cantidad
        if nueva_cantidad < 0:
            print(f"Error: No hay suficiente stock de {self.nombre} (Stock actual: {self.cantidad})")
            return False
        
        self.cantidad = nueva_cantidad
        return True
    
    def __str__(self) -> str:
        """Representación en string del producto"""
        return f"ID: {self._id} | {self.nombre} | ${self.precio:.2f} | Stock: {self.cantidad}"

# =============================================
# INTERFAZ (CLASE ABSTRACT) PARA PRODUCTOS PERECIBLES
# =============================================

class ProductoPerecedero(ABC):
    """
    Interface para productos que tienen fecha de caducidad.
    Define métodos que deben implementar los productos perecederos.
    """
    
    @abstractmethod
    def esta_caducado(self) -> bool:
        """Verifica si el producto ha caducado"""
        pass
    
    @abstractmethod
    def obtener_dias_restantes(self) -> int:
        """Obtiene los días restantes antes de la fecha de caducidad"""
        pass

# =============================================
# SUBCLASE ELECTRÓNICO
# =============================================

class Electronico(Producto):
    """
    Subclase de Producto que representa productos electrónicos.
    Hereda de Producto e implementa todos sus métodos abstractos.
    """
    
    def __init__(self, nombre: str, precio: float, cantidad: int, 
                 marca: str, modelo: str, garantia_meses: int):
        """
        Constructor de Electrónico.
        
        Args:
            marca (str): Marca del producto
            modelo (str): Modelo del producto
            garantia_meses (int): Duración de la garantía en meses
        """
        super().__init__(nombre, precio, cantidad, "Electrónico")
        self.marca = marca
        self.modelo = modelo
        self.garantia_meses = garantia_meses
        
    # Implementación de métodos abstractos de Producto
    def calcular_valor_inventario(self) -> float:
        """Calcula el valor total considerando un impuesto electrónico del 16%"""
        valor_base = self.precio * self.cantidad
        impuesto = valor_base * 0.16  # IVA para electrónicos
        return valor_base + impuesto
    
    def obtener_informacion(self) -> str:
        """Retorna información detallada del electrónico"""
        return (f"📱 ELECTRÓNICO: {self.nombre}\n"
                f"   Marca: {self.marca} | Modelo: {self.modelo}\n"
                f"   Precio: ${self.precio:.2f} | Stock: {self.cantidad}\n"
                f"   Garantía: {self.garantia_meses} meses\n"
                f"   Valor total en inventario: ${self.calcular_valor_inventario():.2f}")
    
    def aplicar_descuento(self, porcentaje: float) -> float:
        """Aplica descuento (máximo 30% para electrónicos)"""
        if porcentaje > 30:
            print("⚠️  Los electrónicos solo pueden tener descuento máximo del 30%")
            porcentaje = 30
        
        descuento = self.precio * (porcentaje / 100)
        self.precio = self.precio - descuento
        return self.precio
    
    def extender_garantia(self, meses_extra: int) -> None:
        """Método específico de Electrónico - Extiende la garantía"""
        self.garantia_meses += meses_extra
        print(f"✅ Garantía extendida a {self.garantia_meses} meses para {self.nombre}")

# =============================================
# SUBCLASE ALIMENTO
# =============================================

class Alimento(Producto, ProductoPerecedero):
    """
    Subclase de Producto que representa alimentos.
    Implementa también la interface ProductoPerecedero.
    """
    
    def __init__(self, nombre: str, precio: float, cantidad: int,
                 peso_kg: float, fecha_caducidad: str, es_organico: bool = False):
        """
        Constructor de Alimento.
        
        Args:
            peso_kg (float): Peso en kilogramos
            fecha_caducidad (str): Fecha de caducidad en formato YYYY-MM-DD
            es_organico (bool): Indica si es orgánico
        """
        super().__init__(nombre, precio, cantidad, "Alimento")
        self.peso_kg = peso_kg
        self.fecha_caducidad = datetime.strptime(fecha_caducidad, "%Y-%m-%d")
        self.es_organico = es_organico
        
    # Implementación de métodos abstractos de Producto
    def calcular_valor_inventario(self) -> float:
        """Calcula el valor total considerando descuento por cercanía a caducidad"""
        valor_base = self.precio * self.cantidad
        
        # Si está cerca de caducar, aplicar descuento
        if self.esta_caducado():
            return 0  # No tiene valor si caducó
        
        dias = self.obtener_dias_restantes()
        if dias < 7:  # Descuento por proximidad a caducar
            return valor_base * 0.7  # 30% de descuento
        elif dias < 15:
            return valor_base * 0.85  # 15% de descuento
        
        return valor_base
    
    def obtener_informacion(self) -> str:
        """Retorna información detallada del alimento"""
        estado = "🔴 CADUCADO" if self.esta_caducado() else "✅ Fresco"
        if not self.esta_caducado():
            estado = f"{estado} ({self.obtener_dias_restantes()} días restantes)"
        
        return (f"🍎 ALIMENTO: {self.nombre}\n"
                f"   Peso: {self.peso_kg}kg | Orgánico: {'Sí' if self.es_organico else 'No'}\n"
                f"   Precio: ${self.precio:.2f} | Stock: {self.cantidad}\n"
                f"   Estado: {estado}\n"
                f"   Valor total en inventario: ${self.calcular_valor_inventario():.2f}")
    
    def aplicar_descuento(self, porcentaje: float) -> float:
        """Aplica descuento (máximo 50% para alimentos)"""
        if porcentaje > 50:
            print("⚠️  Los alimentos solo pueden tener descuento máximo del 50%")
            porcentaje = 50
        
        descuento = self.precio * (porcentaje / 100)
        self.precio = self.precio - descuento
        return self.precio
    
    # Implementación de métodos de ProductoPerecedero
    def esta_caducado(self) -> bool:
        """Verifica si el producto ha caducado"""
        return datetime.now() > self.fecha_caducidad
    
    def obtener_dias_restantes(self) -> int:
        """Calcula los días restantes antes de caducar"""
        if self.esta_caducado():
            return -1
        
        diferencia = self.fecha_caducidad - datetime.now()
        return diferencia.days
    
    def es_caducado(self) -> bool:
        """Método específico de Alimento - Verifica si está caducado"""
        return self.esta_caducado()

# =============================================
# SUBCLASE ROPA
# =============================================

class Ropa(Producto):
    """
    Subclase de Producto que representa prendas de vestir.
    Hereda de Producto e implementa todos sus métodos abstractos.
    """
    
    def __init__(self, nombre: str, precio: float, cantidad: int,
                 talla: str, material: str, temporada: str):
        """
        Constructor de Ropa.
        
        Args:
            talla (str): Talla de la prenda (S, M, L, XL, etc.)
            material (str): Material de la prenda
            temporada (str): Temporada de uso (Verano, Invierno, etc.)
        """
        super().__init__(nombre, precio, cantidad, "Ropa")
        self.talla = talla
        self.material = material
        self.temporada = temporada
        
    # Implementación de métodos abstractos de Producto
    def calcular_valor_inventario(self) -> float:
        """Calcula el valor total con ajuste por temporada"""
        valor_base = self.precio * self.cantidad
        
        # Ajuste por temporada
        temporadas_actual = {
            'Verano': ['Verano'],
            'Invierno': ['Invierno'],
            'Primavera': ['Primavera'],
            'Otoño': ['Otoño']
        }
        
        # Si es temporada actual, mantener precio, sino aplicar descuento
        # Este es un ejemplo simplificado
        return valor_base
    
    def obtener_informacion(self) -> str:
        """Retorna información detallada de la prenda"""
        return (f"👕 ROPA: {self.nombre}\n"
                f"   Talla: {self.talla} | Material: {self.material}\n"
                f"   Temporada: {self.temporada} | Precio: ${self.precio:.2f}\n"
                f"   Stock: {self.cantidad} | Valor total: ${self.calcular_valor_inventario():.2f}")
    
    def aplicar_descuento(self, porcentaje: float) -> float:
        """Aplica descuento (máximo 40% para ropa)"""
        if porcentaje > 40:
            print("⚠️  La ropa solo puede tener descuento máximo del 40%")
            porcentaje = 40
        
        descuento = self.precio * (porcentaje / 100)
        self.precio = self.precio - descuento
        return self.precio
    
    def cambiar_talla(self, nueva_talla: str) -> None:
        """Método específico de Ropa - Cambia la talla del producto"""
        self.talla = nueva_talla
        print(f"✅ Talla actualizada a {nueva_talla} para {self.nombre}")

# =============================================
# SISTEMA DE GESTIÓN DE INVENTARIO
# =============================================

class SistemaInventario:
    """
    Clase que gestiona el inventario completo.
    Demuestra el uso de polimorfismo al manejar diferentes tipos de productos.
    """
    
    def __init__(self):
        self.productos: List[Producto] = []
        self._historial_acciones: List[str] = []
    
    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un producto al inventario"""
        self.productos.append(producto)
        self._registrar_accion(f"Agregado: {producto.nombre} (ID: {producto.id})")
        print(f"✅ Producto agregado exitosamente: {producto.nombre}")
    
    def eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto del inventario por su ID"""
        for i, producto in enumerate(self.productos):
            if producto.id == id_producto:
                nombre = producto.nombre
                del self.productos[i]
                self._registrar_accion(f"Eliminado: {nombre} (ID: {id_producto})")
                print(f"✅ Producto eliminado: {nombre}")
                return True
        
        print(f"❌ Producto con ID {id_producto} no encontrado")
        return False
    
    def buscar_producto(self, id_producto: int) -> Optional[Producto]:
        """Busca un producto por su ID"""
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None
    
    # =============================================
    # DEMOSTRACIÓN DE POLIMORFISMO
    # =============================================
    
    def mostrar_inventario(self) -> None:
        """
        Demuestra el polimorfismo: llama al método obtener_informacion()
        de diferentes objetos sin saber su tipo específico.
        """
        if not self.productos:
            print("📦 El inventario está vacío")
            return
        
        print("\n" + "="*60)
        print("📊 INVENTARIO COMPLETO")
        print("="*60)
        
        for producto in self.productos:
            # POLIMORFISMO EN ACCIÓN: Cada producto responde diferente
            print("\n" + producto.obtener_informacion())
            print("-"*50)
    
    def calcular_valor_total_inventario(self) -> float:
        """
        Demuestra polimorfismo al sumar valores calculados por cada tipo de producto.
        Cada producto tiene su propia implementación de calcular_valor_inventario().
        """
        total = 0
        for producto in self.productos:
            # POLIMORFISMO: Cada producto calcula su valor de manera diferente
            total += producto.calcular_valor_inventario()
        
        return total
    
    def aplicar_descuentos(self, porcentaje: float) -> None:
        """
        Demuestra polimorfismo aplicando descuentos a todos los productos.
        Cada producto aplica el descuento según sus propias reglas.
        """
        print(f"\n💰 Aplicando descuento del {porcentaje}% a todos los productos...")
        print("="*50)
        
        for producto in self.productos:
            # POLIMORFISMO: Cada producto maneja el descuento de manera diferente
            precio_anterior = producto.precio
            producto.aplicar_descuento(porcentaje)
            print(f"✅ {producto.nombre}: ${precio_anterior:.2f} → ${producto.precio:.2f}")
    
    def _registrar_accion(self, accion: str) -> None:
        """Registra acciones en el historial"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._historial_acciones.append(f"[{timestamp}] {accion}")
    
    def mostrar_historial(self) -> None:
        """Muestra el historial de acciones del sistema"""
        print("\n📋 HISTORIAL DE ACCIONES")
        print("="*50)
        for accion in self._historial_acciones:
            print(f"   {accion}")
    
    def exportar_a_json(self, archivo: str = "inventario.json") -> None:
        """Exporta el inventario a un archivo JSON"""
        data = []
        for producto in self.productos:
            # Convertir objetos a diccionarios para JSON
            producto_data = {
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'cantidad': producto.cantidad,
                'categoria': producto.categoria,
                'fecha_registro': producto.fecha_registro.isoformat()
            }
            
            # Agregar atributos específicos según el tipo
            if isinstance(producto, Electronico):
                producto_data.update({
                    'tipo': 'Electronico',
                    'marca': producto.marca,
                    'modelo': producto.modelo,
                    'garantia_meses': producto.garantia_meses
                })
            elif isinstance(producto, Alimento):
                producto_data.update({
                    'tipo': 'Alimento',
                    'peso_kg': producto.peso_kg,
                    'fecha_caducidad': producto.fecha_caducidad.isoformat(),
                    'es_organico': producto.es_organico
                })
            elif isinstance(producto, Ropa):
                producto_data.update({
                    'tipo': 'Ropa',
                    'talla': producto.talla,
                    'material': producto.material,
                    'temporada': producto.temporada
                })
            
            data.append(producto_data)
        
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Inventario exportado a {archivo}")

# =============================================
# PROGRAMA PRINCIPAL - PRUEBAS Y DEMOSTRACIÓN
# =============================================

def main():
    """
    Función principal que demuestra el sistema de inventario con polimorfismo.
    """
    print("="*60)
    print("🏪 SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("="*60)
    print("\nDemostrando POLIMORFISMO con diferentes tipos de productos\n")
    
    # Crear el sistema de inventario
    inventario = SistemaInventario()
    
    # =============================================
    # CREACIÓN DE PRODUCTOS DE DIFERENTES TIPOS
    # =============================================
    
    # Producto Electrónico
    laptop = Electronico(
        nombre="Laptop Pro",
        precio=1200.00,
        cantidad=5,
        marca="TechCorp",
        modelo="Pro X1",
        garantia_meses=24
    )
    
    # Producto Alimento (implementa ProductoPerecedero)
    leche = Alimento(
        nombre="Leche Entera",
        precio=25.50,
        cantidad=20,
        peso_kg=1.0,
        fecha_caducidad="2026-08-15",  # Ajusta la fecha según necesites
        es_organico=True
    )
    
    # Producto Ropa
    camisa = Ropa(
        nombre="Camisa Casual",
        precio=450.00,
        cantidad=30,
        talla="M",
        material="Algodón",
        temporada="Verano"
    )
    
    # Otro Electrónico
    telefono = Electronico(
        nombre="Smartphone X",
        precio=800.00,
        cantidad=10,
        marca="MobileTech",
        modelo="SX-200",
        garantia_meses=12
    )
    
    # Otro Alimento con fecha más cercana para demostrar caducidad
    yogurth = Alimento(
        nombre="Yogurth Natural",
        precio=35.00,
        cantidad=15,
        peso_kg=0.5,
        fecha_caducidad="2026-07-28",  # Fecha más cercana para demostración
        es_organico=False
    )
    
    # =============================================
    # AGREGAR PRODUCTOS AL INVENTARIO
    # =============================================
    
    print("📦 Agregando productos al inventario...")
    print("-"*50)
    inventario.agregar_producto(laptop)
    inventario.agregar_producto(leche)
    inventario.agregar_producto(camisa)
    inventario.agregar_producto(telefono)
    inventario.agregar_producto(yogurth)
    
    # =============================================
    # DEMOSTRACIÓN DE POLIMORFISMO
    # =============================================
    
    # 1. Mostrar inventario completo (polimorfismo en obtener_informacion())
    inventario.mostrar_inventario()
    
    # 2. Calcular valor total (polimorfismo en calcular_valor_inventario())
    print("\n" + "="*60)
    print("💰 VALOR TOTAL DEL INVENTARIO")
    print("="*60)
    valor_total = inventario.calcular_valor_total_inventario()
    print(f"💰 Valor total del inventario: ${valor_total:,.2f}")
    
    # 3. Aplicar descuentos (polimorfismo en aplicar_descuento())
    inventario.aplicar_descuentos(20)  # Aplica 20% de descuento
    
    # Mostrar inventario actualizado después de descuentos
    print("\n📊 Inventario después de aplicar descuentos:")
    inventario.mostrar_inventario()
    
    # 4. Demostrar métodos específicos de cada subclase
    print("\n" + "="*60)
    print("🎯 MÉTODOS ESPECÍFICOS DE CADA SUBCLASE")
    print("="*60)
    
    # Electrónico - extender garantía
    laptop.extender_garantia(6)
    print(f"✅ Garantía extendida: {laptop.garantia_meses} meses totales")
    
    # Alimento - verificar caducidad
    print(f"\n📅 {leche.nombre}:", end=" ")
    if leche.esta_caducado():
        print("❌ CADUCADO")
    else:
        print(f"✅ Válido por {leche.obtener_dias_restantes()} días más")
    
    # Ropa - cambiar talla
    camisa.cambiar_talla("L")
    
    # 5. Demostrar operaciones del sistema
    print("\n" + "="*60)
    print("🔄 OPERACIONES DEL SISTEMA")
    print("="*60)
    
    # Actualizar stock
    print("\n📦 Actualizando stock...")
    laptop.actualizar_stock(-2)  # Vender 2 laptops
    leche.actualizar_stock(10)   # Agregar 10 unidades de leche
    
    print(f"✅ Nuevo stock de {laptop.nombre}: {laptop.cantidad}")
    print(f"✅ Nuevo stock de {leche.nombre}: {leche.cantidad}")
    
    # Buscar producto
    print("\n🔍 Buscando producto por ID...")
    producto_encontrado = inventario.buscar_producto(3)
    if producto_encontrado:
        print(f"✅ Producto encontrado:\n{producto_encontrado}")
    
    # Mostrar historial
    inventario.mostrar_historial()
    
    # Exportar a JSON
    print("\n" + "="*60)
    inventario.exportar_a_json("inventario_demo.json")
    
    # =============================================
    # DEMOSTRACIÓN DE POLIMORFISMO CON LISTA
    # =============================================
    
    print("\n" + "="*60)
    print("🔬 DEMOSTRACIÓN DE POLIMORFISMO CON LISTA")
    print("="*60)
    
    # Crear una lista con diferentes tipos de productos
    productos_mixtos = [
        Electronico("Tablet", 300, 8, "TechPad", "Mini 5", 12),
        Alimento("Pan", 15, 50, 0.5, "2026-08-20", False),
        Ropa("Jeans", 600, 20, "32", "Mezclilla", "Otoño"),
        Electronico("Monitor", 250, 6, "ViewTech", "4K 27", 18),
        Alimento("Queso", 80, 10, 0.3, "2026-08-10", True)
    ]
    
    print("\nProcesando lista de productos mixtos con POLIMORFISMO:")
    print("-"*50)
    
    for producto in productos_mixtos:
        # Cada producto responde diferente aunque usamos el mismo método
        print(f"\n📦 {producto.nombre} ({type(producto).__name__}):")
        print(f"   {producto.obtener_informacion()}")
        print(f"   Valor en inventario: ${producto.calcular_valor_inventario():.2f}")
        print("-"*40)
    
    # Finalizar
    print("\n" + "="*60)
    print("🏁 Sistema de inventario ejecutado exitosamente")
    print("="*60)
    print("\n✅ Demostración de polimorfismo completada")
    print("   - Múltiples tipos de productos")
    print("   - Métodos comunes con comportamientos diferentes")
    print("   - Clases abstractas e interfaces implementadas")
    print("   - Herencia y polimorfismo en acción")

# =============================================
# EJECUCIÓN DEL PROGRAMA
# =============================================

if __name__ == "__main__":
    main()