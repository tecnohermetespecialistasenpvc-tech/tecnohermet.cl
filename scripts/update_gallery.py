import json
from pathlib import Path

TRABAJOS_DIR = Path("assets/trabajos")
OUTPUT_FILE  = Path("gallery-data.json")
EXTENSIONES  = {".jpg", ".jpeg", ".png", ".webp"}

# ── Imágenes demo (se muestran cuando no hay fotos reales) ──
DEMO_ITEMS = [
    {
        "title": "Ventanas PVC interior",
        "category": "ventanas",
        "image": "https://pplx-res.cloudinary.com/image/upload/pplx_search_images/4f4b2ab93158181304e7509fe92a55b05f551142.jpg",
        "description": "Proyecto residencial con ventanales de gran formato.",
        "location": "Santiago"
    },
    {
        "title": "Puerta PVC moderna",
        "category": "puertas",
        "image": "https://pplx-res.cloudinary.com/image/upload/pplx_search_images/73245052e0bea4511a763f0f74c230e61eab04a3.jpg",
        "description": "Puerta con panel vidriado y diseño contemporáneo.",
        "location": "Las Condes"
    },
    {
        "title": "Cortinas de cristal",
        "category": "cortinas",
        "image": "https://pplx-res.cloudinary.com/image/upload/pplx_search_images/00b10446d7cbf17b9c453b8ccf016fa88be40c86.jpg",
        "description": "Cierre de terraza con cortina transparente.",
        "location": "Providencia"
    },
    {
        "title": "Sala con termopanel",
        "category": "termopanel",
        "image": "https://pplx-res.cloudinary.com/image/upload/pplx_search_images/1f4aed3c43bb1ce6f9f60c667ac588da07f52982.jpg",
        "description": "Mayor confort térmico y acústico.",
        "location": "Vitacura"
    },
    {
        "title": "Terraza panorámica",
        "category": "cortinas",
        "image": "https://pplx-res.cloudinary.com/image/upload/pplx_search_images/fafbdd837531111e5c3492552047700ce354f14f.jpg",
        "description": "Solución panorámica en cristal para terraza.",
        "location": "Ñuñoa"
    },
    {
        "title": "Instalación técnica",
        "category": "instalacion",
        "image": "https://pplx-res.cloudinary.com/image/upload/pplx_search_images/b6d7955aca42b445c45898e99ab68800660dd09f.jpg",
        "description": "Montaje en obra con equipo especializado.",
        "location": "Santiago"
    }
]

# ── Diccionarios de detección ─────────────────────────────

CATEGORIAS = {
    "ventanas":    "ventanas",
    "puerta":      "puertas",
    "puertas":     "puertas",
    "termopanel":  "termopanel",
    "cortina":     "cortinas",
    "cortinas":    "cortinas",
    "baranda":     "cortinas",
    "instalacion": "instalacion",
    "montaje":     "instalacion",
    "obra":        "instalacion",
}

UBICACIONES = {
     # ── Región Metropolitana ──────────────────────────────
    "lascondes":       "Las Condes",
    "las_condes":      "Las Condes",
    "providencia":     "Providencia",
    "vitacura":        "Vitacura",
    "nunoa":           "Ñuñoa",
    "santiago":        "Santiago",
    "maipu":           "Maipú",
    "peñalolen":       "Peñalolén",
    "penalolen":       "Peñalolén",
    "lacisterna":      "La Cisterna",
    "sanmiguel":       "San Miguel",
    "san_miguel":      "San Miguel",
    "florida":         "La Florida",
    "laflorida":       "La Florida",
    "macul":           "Macul",
    "recoleta":        "Recoleta",
    "independencia":   "Independencia",
    "quilicura":       "Quilicura",
    "pudahuel":        "Pudahuel",
    "conchali":        "Conchalí",
    "huechuraba":      "Huechuraba",
    "renca":           "Renca",
    "cerrillos":       "Cerrillos",
    "colina":          "Colina",
    "lampa":           "Lampa",
    "buin":            "Buin",
    "puente":          "Puente Alto",
    "puentealto":      "Puente Alto",
    "puente_alto":     "Puente Alto",
    "talagante":       "Talagante",
    "melipilla":       "Melipilla",
    "santiagocentro":  "Santiago Centro",
    "barnechea":       "Lo Barnechea",
    "lobarnechea":     "Lo Barnechea",
    "loespejo":        "Lo Espejo",
    "lo_espejo":       "Lo Espejo",
    "loprado":         "Lo Prado",
    "lo_prado":        "Lo Prado",
    "cerro":           "Cerro Navia",
    "cerronavia":      "Cerro Navia",
    "cerro_navia":     "Cerro Navia",
    "estacion":        "Estación Central",
    "sanjoaquin":      "San Joaquín",
    "san_joaquin":     "San Joaquín",
    "sanramón":        "San Ramón",
    "sanramon":        "San Ramón",
    "peñaflor":        "Peñaflor",
    "penaflor":        "Peñaflor",

    # ── Región del Biobío ─────────────────────────────────
    "concepcion":      "Concepción",
    "concepción":      "Concepción",
    "talcahuano":      "Talcahuano",
    "hualpén":         "Hualpén",
    "hualpen":         "Hualpén",
    "sanpedro":        "San Pedro de la Paz",
    "san_pedro":       "San Pedro de la Paz",
    "coronel":         "Coronel",
    "losangeles":      "Los Ángeles",
    "los_angeles":     "Los Ángeles",
    "losángeles":      "Los Ángeles",
    "biobio":          "Biobío",
    "bío_bío":         "Biobío",
    "arauco":          "Arauco",
    "lebu":            "Lebu",
    "curanilahue":     "Curanilahue",
    "losalamos":       "Los Álamos",
    "cañete":          "Cañete",
    "canete":          "Cañete",
    "tirua":           "Tirúa",
    "lota":            "Lota",
    "tomé":            "Tomé",
    "tome":            "Tomé",
    "penco":           "Penco",
    "hualqui":         "Hualqui",
    "santajuana":      "Santa Juana",
    "florida_bio":     "Florida",
    "yumbel":          "Yumbel",
    "cabrero":         "Cabrero",
    "laja":            "Laja",
    "nacimiento":      "Nacimiento",
    "mulchen":         "Mulchén",
    "mulchén":         "Mulchén",
    "negrete":         "Negrete",
    "santabarbara":    "Santa Bárbara",
    "quilaco":         "Quilaco",
    "quilleco":        "Quilleco",
    "altobishoften":   "Alto Biobío",
    "altobiobio":      "Alto Biobío",
    "contulmo":        "Contulmo",
    "cañete":          "Cañete",
    "tucapel":         "Tucapel",
    "antuco":          "Antuco",

    # ── Región de Ñuble ───────────────────────────────────
    "chillán":         "Chillán",
    "chillan":         "Chillán",
    "chillánviejo":    "Chillán Viejo",
    "chillanviejo":    "Chillán Viejo",
    "nuble":           "Ñuble",
    "ñuble":           "Ñuble",
    "bulnes":          "Bulnes",
    "quillon":         "Quillón",
    "quillón":         "Quillón",
    "yungay":          "Yungay",
    "laja_nuble":      "Laja",
    "sancarlos":       "San Carlos",
    "san_carlos":      "San Carlos",
    "niquen":          "Ñiquén",
    "ñiquen":          "Ñiquén",
    "sanfabián":       "San Fabián",
    "san_fabian":      "San Fabián",
    "ranquil":         "Ranquil",
    "cobquecura":      "Cobquecura",
    "coelemu":         "Coelemu",
    "portezuelo":      "Portezuelo",
    "treguaco":        "Trehuaco",
    "quirihue":        "Quirihue",
    "ninhue":          "Ninhue",
    "pemuco":          "Pemuco",
    "pinto":           "Pinto",
    "coihueco":        "Coihueco",
    "elcarmen":        "El Carmen",
    "el_carmen":       "El Carmen",
    "sanignacio":      "San Ignacio",
    "san_ignacio":     "San Ignacio",
    "tucapel_nuble":   "Tucapel",
    "elpinar":         "El Pinar",
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
    TRABAJOS_DIR.mkdir(parents=True, exist_ok=True)

    archivos = sorted([
        f for f in TRABAJOS_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in EXTENSIONES
    ])

    # Fotos reales desde assets/trabajos/
    items_reales = []
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
        items_reales.append(item)
        print(f"  ✓ {archivo.name} → {categoria} | {ubicacion or 'sin ubicación'}")

    # Combina: reales primero, demo al final
    items = items_reales + DEMO_ITEMS

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"items": items}, f, ensure_ascii=False, indent=2)

    print(f"\ngallery-data.json → {len(items_reales)} real(es) + {len(DEMO_ITEMS)} demo = {len(items)} total.")

if __name__ == "__main__":
    main()
