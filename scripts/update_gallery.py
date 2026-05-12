import os
import json
from pathlib import Path

TRABAJOS_DIR = Path("assets/trabajos")
OUTPUT_FILE  = Path("gallery-data.json")
EXTENSIONES  = {".jpg", ".jpeg", ".png", ".webp"}

# Categorías detectadas por nombre de archivo
# Ejemplo: ventanas_proyecto01.jpg → categoría "ventanas"
CATEGORIAS = ["ventanas", "puertas", "termopanel", "cortinas", "instalacion"]

def detectar_categoria(nombre):
    nombre_lower = nombre.lower()
    for cat in CATEGORIAS:
        if cat in nombre_lower:
            return cat
    return "general"

def limpiar_titulo(nombre):
    # Elimina extensión y guiones/guiones bajos
    sin_ext = Path(nombre).stem
    return sin_ext.replace("-", " ").replace("_", " ").title()

def main():
    items = []

    if not TRABAJOS_DIR.exists():
        print(f"Carpeta {TRABAJOS_DIR} no encontrada.")
        return

    archivos = sorted([
        f for f in TRABAJOS_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in EXTENSIONES
    ])

    for archivo in archivos:
        item = {
            "title":       limpiar_titulo(archivo.name),
            "category":    detectar_categoria(archivo.name),
            "image":       f"./assets/trabajos/{archivo.name}",
            "description": f"Trabajo realizado por TECNO HERMET.",
            "location":    ""
        }
        items.append(item)

    data = {"items": items}

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"gallery-data.json actualizado con {len(items)} imagen(es).")

if __name__ == "__main__":
    main()
