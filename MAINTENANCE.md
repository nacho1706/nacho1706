# Mantenimiento del perfil

## Publicación

Este directorio contiene los archivos para el repositorio público `nacho1706/nacho1706`. GitHub muestra automáticamente el `README.md` de ese repositorio en el perfil.

No publicar el CV ni las notas de postulación como parte del perfil. Los documentos de diseño y la configuración de Impeccable son de desarrollo y están excluidos en `.gitignore`.

## Actualizar contenido

Editar `README.md`. Las métricas de tesis corresponden al equipo y a datos sintéticos de desarrollo. Revisar el estado de la solicitud de Genie antes de cambiar “under review”.

No agregar fechas laborales, porcentajes de mejora ni cifras de adopción sin respaldo.

## Regenerar animación

```bash
python -m pip install -r scripts/requirements.txt
python scripts/generate_banner.py
```

El generador requiere las fuentes locales Noto Sans (`/usr/share/fonts/noto/`). Las rutas se definen al inicio del script. No depende de widgets ni servicios de estadísticas. El README también incluye la demo GIF original del repositorio de Genie como recurso remoto; puede requerir actualizarse si se mueve ese archivo.

## Accesibilidad

El elemento `picture` ofrece un PNG estático cuando el navegador indica `prefers-reduced-motion: reduce`. Los datos esenciales también están en texto Markdown; el banner incluye texto alternativo y hay un enlace a su versión estática.

## Comprobaciones realizadas

- README renderizado por la API Markdown de GitHub: conserva `picture`, `source`, `details` y la tabla.
- Banner GIF verificado: 84 fotogramas, 1280 × 400, bucle continuo, aproximadamente 92 KB (6,72 segundos por ciclo).
- Revisión visual de fotograma estático y central; sin JavaScript o CSS personalizado en el README.

La validación con la API comprueba el HTML generado. El renderizado visual dentro del perfil depende de GitHub; se debe verificar allí después de publicar.

## Revisión

Revisión independiente: **ship**, sin correcciones requeridas. Contraste del texto del banner: 8,59:1 o superior. En móviles, el Markdown nativo repite la información principal para evitar depender del texto pequeño de la imagen.
