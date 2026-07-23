
📦 SISTEMA DE GESTIÓN DE INVENTARIOS
Con Polimorfismo, Clases Abstractas e Interfaces
📋 DESCRIPCIÓN GENERAL
Este proyecto implementa un sistema de gestión de inventarios utilizando Programación Orientada a Objetos (POO) en Python, demostrando conceptos fundamentales como:

✅ Polimorfismo: Mismos métodos, comportamientos diferentes

✅ Clases Abstractas: Definición de estructuras base

✅ Interfaces: Contratos para comportamientos específicos

✅ Herencia: Reutilización y extensión de código

✅ Encapsulamiento: Protección de datos internos

El sistema permite manejar diferentes tipos de productos (electrónicos, alimentos y ropa) con comportamientos específicos para cada uno, demostrando cómo el polimorfismo facilita la gestión de objetos de diferentes tipos de manera uniforme.

🏗️ ESTRUCTURA DEL PROYECTO
text
inventario-sistema/
│
├── sistema_inventario.py        # Código principal del sistema
├── README.md                    # Documentación del proyecto
├── requirements.txt             # Dependencias del proyecto
├── .gitignore                   # Archivos ignorados por Git
│
├── tests/
│   └── test_polimorfismo.py     # Pruebas unitarias de polimorfismo
│
└── docs/
    ├── diagrama_clases.png      # Diagrama de clases UML
    └── guia_usuario.md          # Guía de usuario
📊 DIAGRAMA DE CLASES
text
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA DE INVENTARIOS                    │
│                         (UML)                               │
└─────────────────────────────────────────────────────────────┘

                    ┌─────────────────┐
                    │   ABC (Abstract)│
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │    Producto     │  ← CLASE ABSTRACTA
                    │   (Clase Base)  │
                    │─────────────────│
                    │ - _id: int      │
                    │ - nombre: str   │
                    │ - precio: float │
                    │ - cantidad: int │
                    │ - categoria: str│
                    │─────────────────│
                    │ + calcular_     │
                    │   valor_invent.()│ ← ABSTRACTOS
                    │ + obtener_info()│
                    │ + aplicar_      │
                    │   descuento()   │
                    │ + actualizar_   │
                    │   stock()       │ ← CONCRETOS
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
     ┌──────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐
     │ Electrónico │ │   Alimento  │ │    Ropa     │
     │ (Subclase)  │ │ (Subclase)  │ │ (Subclase)  │
     │─────────────│ │─────────────│ │─────────────│
     │ - marca     │ │ - peso_kg   │ │ - talla     │
     │ - modelo    │ │ - fecha_cad │ │ - material  │
     │ - garantia  │ │ - organico  │ │ - temporada │
     │─────────────│ │─────────────│ │─────────────│
     │ + calcular_ │ │ + calcular_ │ │ + calcular_ │
     │   valor()   │ │   valor()   │ │   valor()   │
     │ + obtener_  │ │ + obtener_  │ │ + obtener_  │
     │   info()    │ │   info()    │ │   info()    │
     │ + aplicar_  │ │ + aplicar_  │ │ + aplicar_  │
     │   desc()    │ │   desc()    │ │   desc()    │
     │ + extender_ │ │ + esta_     │ │ + cambiar_  │
     │   garantia()│ │   caducado()│ │   talla()   │
     └─────────────┘ └──────┬──────┘ └─────────────┘
                            │
                     ┌──────▼──────┐
                     │  Producto   │  ← INTERFAZ
                     │ Perecedero  │
                     │─────────────│
                     │ + esta_     │
                     │   caducado()│
                     │ + obtener_  │
                     │   dias_rest.│
                     └─────────────┘
🎯 CONCEPTOS DEMOSTRADOS
1. CLASES ABSTRACTAS
Producto es una clase abstracta que no puede ser instanciada directamente

Define métodos abstractos que obligan a las subclases a implementarlos

Proporciona una estructura común para todos los productos

2. HERENCIA
Electronico, Alimento y Ropa heredan de Producto

Reutilizan atributos y métodos de la clase base

Extienden funcionalidades específicas para cada tipo

3. POLIMORFISMO
Mismo método, diferentes comportamientos:

obtener_informacion(): Cada producto muestra su información específica

calcular_valor_inventario(): Cada producto calcula su valor de manera única

aplicar_descuento(): Cada producto tiene reglas de descuento diferentes

4. INTERFACES
ProductoPerecedero define un contrato para productos que caducan

Alimento implementa esta interfaz, demostrando herencia múltiple

5. ENCAPSULAMIENTO
Atributos privados (con _) como _id

Getters (propiedades) para acceso controlado

Métodos públicos para interacción segura

🚀 CARACTERÍSTICAS DEL SISTEMA
Tipos de Productos
Tipo	Características	Métodos Especiales
Electrónico	Marca, modelo, garantía	extender_garantia()
Alimento	Peso, fecha caducidad, orgánico	esta_caducado(), obtener_dias_restantes()
Ropa	Talla, material, temporada	cambiar_talla()
Funcionalidades del Sistema
✅ Agregar productos al inventario

✅ Eliminar productos por ID

✅ Buscar productos

✅ Actualizar stock (aumentar/disminuir)

✅ Calcular valor total del inventario

✅ Aplicar descuentos a todos los productos

✅ Mostrar inventario detallado

✅ Exportar inventario a JSON

✅ Historial de acciones

✅ Demostración de polimorfismo

Reglas de Negocio
Producto	IVA	Descuento Máximo	Valor Inventario
Electrónico	16%	30%	Precio × Cantidad + IVA
Alimento	0%	50%	Descuento por proximidad a caducar
Ropa	0%	40%	Ajuste por temporada
💻 INSTALACIÓN Y EJECUCIÓN
Requisitos Previos
Python 3.8 o superior

Git (opcional, para clonar el repositorio)

Instalación
bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/inventario-sistema.git

# Navegar al directorio
cd inventario-sistema

# Verificar Python
python --version
Ejecución
bash
# Ejecutar el sistema principal
python sistema_inventario.py

# Ejecutar pruebas específicas
python tests/test_polimorfismo.py
📝 EJEMPLOS DE CÓDIGO
Demostración de Polimorfismo
python
# Crear lista de productos mixtos
productos = [
    Electronico("Laptop", 1200, 5, "Dell", "XPS", 24),
    Alimento("Leche", 25.50, 20, 1.0, "2026-08-15", True),
    Ropa("Camisa", 450, 30, "M", "Algodón", "Verano")
]

# POLIMORFISMO EN ACCIÓN
for producto in productos:
    # Mismo método, diferentes comportamientos
    print(producto.obtener_informacion())
    print(f"Valor: ${producto.calcular_valor_inventario():.2f}")
    print("-" * 40)
Resultado Esperado
text
📱 ELECTRÓNICO: Laptop
   Marca: Dell | Modelo: XPS
   Precio: $1200.00 | Stock: 5
   Garantía: 24 meses
   Valor total: $6960.00

🍎 ALIMENTO: Leche
   Peso: 1.0kg | Orgánico: Sí
   Precio: $25.50 | Stock: 20
   Estado: ✅ Fresco (24 días restantes)
   Valor total: $510.00

👕 ROPA: Camisa
   Talla: M | Material: Algodón
   Temporada: Verano
   Precio: $450.00 | Stock: 30
   Valor total: $13500.00
🧪 PRUEBAS DE POLIMORFISMO
Pruebas Incluidas
Prueba de herencia: Verificar que todas las subclases hereden de Producto

Prueba de métodos abstractos: Verificar que todos los métodos estén implementados

Prueba de polimorfismo: Verificar comportamientos diferentes para el mismo método

Prueba de interfaces: Verificar implementación de ProductoPerecedero

Prueba de reglas de negocio: Verificar límites de descuento y cálculos

Ejecutar Pruebas
python
# En tests/test_polimorfismo.py

def ejecutar_pruebas():
    # Crear productos de prueba
    p1 = Electronico("Test", 100, 1, "Marca", "Modelo", 12)
    p2 = Alimento("Test", 50, 1, 1.0, "2026-12-31", False)
    p3 = Ropa("Test", 200, 1, "M", "Algodón", "Verano")
    
    # Verificar polimorfismo
    for p in [p1, p2, p3]:
        assert isinstance(p, Producto)  # Todos son Producto
        print(f"✅ {type(p).__name__} pasa pruebas de polimorfismo")
📖 DOCUMENTACIÓN DEL CÓDIGO
El código está completamente documentado con comentarios que explican:

Documentación de Clases
python
class Producto(ABC):
    """
    CLASE ABSTRACTA: Producto
    
    Define el CONTRATO que deben cumplir todos los productos.
    Al ser abstracta, garantiza que:
    1. No se puedan crear objetos "Producto" genéricos
    2. Todas las subclases implementen los métodos obligatorios
    3. Se mantenga una estructura común en todo el sistema
    """
Documentación de Métodos
python
@abstractmethod
def calcular_valor_inventario(self) -> float:
    """
    MÉTODO ABSTRACTO: Calcular valor total en inventario.
    
    PROPÓSITO: Cada tipo de producto calcula su valor de manera diferente:
    - Electrónico: Aplica IVA del 16%
    - Alimento: Aplica descuentos por proximidad a caducidad
    - Ropa: Aplica ajustes por temporada
    
    Returns:
        float: Valor total del inventario para este producto
    """
Documentación de Herencia
python
class Alimento(Producto, ProductoPerecedero):
    """
    SUBCLASE DE Producto QUE IMPLEMENTA ProductoPerecedero.
    
    RELACIÓN DE HERENCIA:
    Alimento → HEREDA DE → Producto (Clase Base)
    Alimento → IMPLEMENTA → ProductoPerecedero (Interfaz)
    
    Esto demuestra HERENCIA MÚLTIPLE.
    """
🔧 REQUISITOS DEL SISTEMA
Dependencias
Python estándar (no requiere librerías externas)

Módulos utilizados: abc, datetime, typing, json

Compatibilidad
✅ Windows

✅ macOS

✅ Linux

🤝 CONTRIBUCIÓN
Si deseas contribuir al proyecto:

Fork el repositorio

Crea tu rama de características (git checkout -b feature/AmazingFeature)

Commit tus cambios (git commit -m 'Add some AmazingFeature')

Push a la rama (git push origin feature/AmazingFeature)

Abre un Pull Request

📄 LICENCIA
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

👤 AUTOR
Tu Nombre

GitHub: @tu_usuario

Email: tu@email.com

📚 RECURSOS ADICIONALES
Documentación de Python

Programación Orientada a Objetos en Python

Guía de Polimorfismo en Python

Clases Abstractas en Python

📊 ESTADO DEL PROYECTO
https://img.shields.io/badge/Estado-Completado-brightgreen
https://img.shields.io/badge/Versi%C3%B3n-1.0-blue
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Licencia-MIT-green

🎯 OBJETIVOS DE APRENDIZAJE
Al completar este proyecto, habrás demostrado:

✅ Comprensión de clases abstractas y su aplicación

✅ Implementación de interfaces en Python

✅ Uso de herencia y herencia múltiple

✅ Aplicación de polimorfismo en situaciones reales

✅ Documentación profesional de código

✅ Gestión de versiones con Git y GitHub

✅ Pruebas de conceptos de POO

🏆 CRITERIOS DE EVALUACIÓN
Criterio	Puntuación	Estado
Clases abstractas implementadas	20%	✅
Interfaces definidas	15%	✅
Herencia correcta	15%	✅
Polimorfismo demostrado	25%	✅
Documentación completa	15%	✅
Commit y push a GitHub	10%	✅
📞 CONTACTO Y SOPORTE
Para preguntas o soporte:


