import os
import json
from pathlib import Path

TRABAJOS_DIR = Path("assets/trabajos")
OUTPUT_FILE  = Path("gallery-data.json")
EXTENSIONES  = {".jpg", ".jpeg", ".png", ".webp"}

# ── Diccionarios de detección ─────────────────────────────

CATEGORIAS = {
    "ventanas":   "ventanas",
    "puerta":     "puertas",
    "puertas":    "puertas",
    "termopanel": "termopanel",
    "cortina":    "cortinas",
    "cortinas":   "cortinas",
    "baranda":    "cortinas",
    "instalacion":"instalacion",
    "montaje":    "instalacion",
    "obra":       "instalacion",
}

UBICACIONES = {
    "lascondes":    "Las Condes",
    "las_condes":   "Las Condes",
    "providencia":  "Providencia",
    "vitacura":     "Vitacura",
    "nunoa":        "Ñuñoa",
    "ñuñoa":        "Ñuñoa",
    "maipu":        "Maipú",
    "maipú":        "Maipú",
    "santiago":     "Santiago",
    "lamina":       "Laminado",
    "peñalolen":    "Peñalolén",
    "penalolen":    "Peñalolén",
    "lacisterna":   "La Cisterna",
    "la_cisterna":  "La Cisterna",
    "sanmiguel":    "San Miguel",
    "san_miguel":   "San Miguel",
    "florida":      "La Florida",
    "laflorida":    "La Florida",
    "la_florida":   "La Florida",
    "macul":        "Macul",
    "recoleta":     "Recoleta",
    "independencia":"Independencia",
    "quilicura":    "Quilicura",
    "pudahuel":     "Pudahuel",
    "conchali":     "Conchalí",
    "conchalí":     "Conchalí",
    "estacion":     "Estación Central",
    "huechuraba":   "Huechuraba",
    "renca":        "Renca",
    "cerrillos":    "Cerrillos",
    "buin":         "Buin",
    "lampa":        "Lampa",
    "colina":       "Colina",
}

# ── Funciones ─────────────────────────────────────────────

def detectar_categoria(nombre):
    nombre_lower = nombre.lower()
    for clave, valor in CATEGORIAS.items():
        if clave in nombre_lower:
            return valor
    return "general"

def detectar_ubicacion(nombre):
    nombre_lower = nombre.lower().replace("-", "").replace("_", "")
    for clave, valor in UBICACIONES.items():
        if clave.replace("_", "") in nombre_lower:
            return valor
    return ""

def limpiar_titulo(nombre):
    sin_ext = Path(nombre).stem
    partes  = sin_ext.replace("-", " ").replace("_", " ").split()
    # Elimina números sueltos al final (ej: 01, 02)
    partes  = [p for p in partes if not p.isdigit()]
    return " ".join(partes).title()

def generar_descripcion(categoria, ubicacion):
    desc = {
        "ventanas":    "Instalación de ventanas PVC",
        "puertas":     "Instalación de puertas PVC",
        "termopanel":  "Proyecto con termopanel",
        "cortinas":    "Cierre con cortinas o barandas de cristal",
        "instalacion": "Trabajo de instalación técnica",
        "general":     "Trabajo realizado por TECNO HERMET",
    }
    base = desc.get(categoria, "Trabajo realizado por TECNO HERMET")
    return f"{base}{' en ' + ubicacion if ubicacion else ''}."

# ── Main ──────────────────────────────────────────────────

def main():
    items = []

    if not TRABAJOS_DIR.exists():
        print(f"Carpeta {TRABAJOS_DIR} no encontrada. Creándola...")
        TRABAJOS_DIR.mkdir(parents=True, exist_ok=True)

    archivos = sorted([
        f for f in TRABAJOS_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in EXTENSIONES
    ])

    for archivo in archivos:
        categoria = detectar_categoria(archivo.name)
        ubicacion = detectar_ubicacion(archivo.name)
        item = {
            "title":       limpiar_titulo(archivo.name),
            "category":    categoria,
            "image":       f"./assets/trabajos/{archivo.name}",
            "description": generar_descripcion(categoria, ubicacion),
            "location":    ubicacion,
        }
        items.append(item)
        print(f"  ✓ {archivo.name} → {categoria} | {ubicacion or 'sin ubicación'}")

    data = {"items": items}

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\ngallery-data.json actualizado con {len(items)} imagen(es).")

if __name__ == "__main__":
    main()
