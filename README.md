
## 📲 WhatsApp de contacto

+56 9 6722 3543

Enlace directo: https://wa.me/56967223543

## 🖼️ Cómo agregar nuevos trabajos a la galería

1. Sube la foto a `assets/trabajos/` en el repositorio.
2. Abre `admin/upload.html` en el navegador.
3. Completa el formulario y haz clic en **Generar JSON**.
4. Copia el bloque generado y pégalo dentro de `"items"` en `gallery-data.json`.
5. Sube los cambios a GitHub. La galería se actualiza automáticamente.

### Ejemplo de entrada en gallery-data.json

```json
{
  "title": "Ventanas PVC Las Condes",
  "category": "ventanas",
  "image": "./assets/trabajos/las-condes-01.jpg",
  "description": "Instalación de ventanales de gran formato en vivienda unifamiliar.",
  "location": "Las Condes, Santiago"
}
```

## 🔐 Panel administrador

Acceso en: `admin/index.html`

| Campo      | Valor (cámbialo antes de publicar) |
|------------|------------------------------------|
| Usuario    | admin                              |
| Contraseña | TECNO2026!                         |
| Código 2FA | 123456                             |

> ⚠️ Cambia las credenciales en `admin/index.html` dentro de las variables `ADMIN_USER`, `ADMIN_PASS` y `ADMIN_OTP`.

## ✏️ Pendientes antes de publicar

- [ ] Actualizar correo de contacto en `index.html`.
- [ ] Cambiar credenciales del admin en `admin/index.html`.
- [ ] Reemplazar imágenes de ejemplo en `gallery-data.json` por fotos reales.
- [ ] Actualizar URL del sitio en este README una vez publicado.

## 🔒 Nota de seguridad

El panel admin es solo visual en GitHub Pages. Para autenticación real usa Firebase Auth o Auth0.

---

Repositorio: https://github.com/tecnohermetespecialistasenpvc-tech/tecnohermet.cl
