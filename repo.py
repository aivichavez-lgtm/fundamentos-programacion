import os
import shutil
from datetime import date

# =========================
# CONFIGURACIÓN
# =========================

# Modo seguro: NO borra nada.
# Si quieres eliminar carpetas antiguas (ej. T1_Algoritmos), pon True.
DELETE_OLD = False

OLD_FOLDERS_TO_DELETE = ["T1_Algoritmos"]

# Estructura alineada al programa TecNM (5 unidades)
UNITS = [
    {
        "folder": "U1_Diseno_Algoritmico",
        "title": "Unidad 1. Diseño Algorítmico",
        "topics": [
            "1.1 Conceptos básicos",
            "1.2 Representación de algoritmos: gráfica y pseudocódigo",
            "1.3 Diseño de algoritmos",
            "1.4 Diseño de funciones",
        ],
        "subfolders": ["pseudocodigo", "diagramas", "evidencias"],
        "examples": {"pseudocodigo": True, "python": False, "csharp": False},
    },
    {
        "folder": "U2_Introduccion_Programacion",
        "title": "Unidad 2. Introducción a la Programación",
        "topics": [
            "2.1 Conceptos básicos",
            "2.2 Características del lenguaje de programación",
            "2.3 Estructura básica de un programa",
            "2.4 Elementos del lenguaje",
            "2.5 Compilación, ejecución y errores",
        ],
        "subfolders": ["pseudocodigo", "python", "csharp", "evidencias"],
        "examples": {"pseudocodigo": True, "python": True, "csharp": True},
    },
    {
        "folder": "U3_Control_de_Flujo",
        "title": "Unidad 3. Control de Flujo",
        "topics": [
            "3.1 Secuenciales",
            "3.2 Selectivas",
            "3.3 Iterativas",
        ],
        "subfolders": ["pseudocodigo", "python", "csharp", "evidencias"],
        "examples": {"pseudocodigo": True, "python": True, "csharp": True},
    },
    {
        "folder": "U4_Organizacion_Datos",
        "title": "Unidad 4. Organización de Datos",
        "topics": [
            "4.1 Arreglos",
            "4.2 Unidimensionales",
            "4.3 Multidimensionales",
            "4.4 Registros",
        ],
        "subfolders": ["pseudocodigo", "python", "csharp", "evidencias"],
        "examples": {"pseudocodigo": True, "python": True, "csharp": True},
    },
    {
        "folder": "U5_Modularidad",
        "title": "Unidad 5. Modularidad",
        "topics": [
            "5.1 Módulos",
            "5.2 Parámetros",
            "5.3 Implementación",
        ],
        "subfolders": ["pseudocodigo", "python", "csharp", "evidencias"],
        "examples": {"pseudocodigo": True, "python": True, "csharp": True},
    },
]

# =========================
# UTILIDADES
# =========================

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def gitkeep(folder):
    write_file(os.path.join(folder, ".gitkeep"), "")

def safe_delete(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f"Eliminado: {folder}")

# =========================
# PLANTILLAS
# =========================

PSEUDO = """Proceso {nombre}
    // ENTRADAS
    // PROCESO
    // SALIDAS
FinProceso
"""

DESIGN = """# Diseño del algoritmo

## Problema
Describe el problema.

## Entradas
-

## Salidas
-

## Proceso
1.
2.

## Casos de prueba
| Entrada | Salida esperada |
|--------|----------------|
"""

DIAGRAM = """```mermaid
flowchart TD
A([Inicio]) --> B[/Leer datos/]
B --> C[Procesar]
C --> D[/Mostrar resultado/]
D --> E([Fin])
```"""

PY_EXAMPLE = """# Ejemplo base
nombre = input("Nombre: ")
a = float(input("Numero 1: "))
b = float(input("Numero 2: "))
print("Resultado:", a + b)
"""

CS_NOTE = """Para usar C#:

dotnet new console -n Ux_Tx -o .
dotnet run
"""

UNIT_README = """# {titulo}

## Temas
{temas}

## Evidencias
- Tareas: U{u}_T#.ext
- Prácticas: U{u}_P_##.ext

## Flujo
1. Diseñar
2. Pseudocódigo
3. Implementación (desde U2)
4. Commit descriptivo
"""

# =========================
# GENERACIÓN
# =========================

def create_units():
    for unit in UNITS:
        base = unit["folder"]
        ensure_dir(base)

        u_num = base.split("_")[0].replace("U","")

        temas = "\n".join(f"- {t}" for t in unit["topics"])
        write_file(f"{base}/README.md", UNIT_README.format(
            titulo=unit["title"],
            temas=temas,
            u=u_num
        ))

        for sub in unit["subfolders"]:
            path = f"{base}/{sub}"
            ensure_dir(path)
            gitkeep(path)

        if "pseudocodigo" in unit["subfolders"]:
            write_file(f"{base}/pseudocodigo/PLANTILLA.psc", PSEUDO.format(nombre="Ejemplo"))
            write_file(f"{base}/pseudocodigo/U{u_num}_T0.psc", PSEUDO.format(nombre="Prueba"))

        if "diagramas" in unit["subfolders"]:
            write_file(f"{base}/diagramas/PLANTILLA.md", DIAGRAM)

        write_file(f"{base}/evidencias/PLANTILLA.md", DESIGN)

        if unit["examples"].get("python"):
            write_file(f"{base}/python/U{u_num}_T0.py", PY_EXAMPLE)

        if unit["examples"].get("csharp"):
            write_file(f"{base}/csharp/LEEME.md", CS_NOTE)

def main():
    print("Creando estructura del curso...\n")
    create_units()

    if DELETE_OLD:
        for f in OLD_FOLDERS_TO_DELETE:
            safe_delete(f)
    else:
        print("Modo seguro activo: no se eliminó nada")

    print("\nEstructura lista ✔")

if __name__ == "__main__":
    main()
