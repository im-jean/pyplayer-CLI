# 🎵 pyplayer-CLI

Reproductor de música local minimalista para terminal, desarrollado en Python y pensado para entornos Linux.

## ✨ Características actuales
- Escaneo automático de archivos de audio en el directorio local.
- Lista numerada interactiva en consola.
- Selección y reproducción directa mediante número de pista usando `pygame-ce`.

## 🚀 Requisitos e instalación

Este proyecto utiliza **[uv](https://astral.sh)** para la gestión rápida de dependencias y entornos virtuales.

1. Clona el repositorio:
   ```bash
   git clone https://github.com/im-jean/pyplayer-CLI
   cd pyplayer-CLI
   ```

2. Sincroniza las dependencias:
   ```bash
   uv sync
   ```

3. Ejecuta el reproductor:
   ```bash
   uv run pyplayer
   ```

## 📄 ¿Cómo configurar y modificar el programa?

### 1. Establecer la ruta de tu música
Dentro del archivo `src/pyplayer/__init__.py`, busca la variable `musica` y reemplaza la ruta dentro de `os.listdir("/home/tu_usuario/Music/")` por la carpeta donde guardas tus canciones (`.mp3`, `.wav`, `.ogg`, etc.).
> **Nota:** Por el momento, los archivos de audio deben estar directamente dentro de esa carpeta y no en subcarpetas.

### 2. Ajustar el tiempo de reproducción
Esta versión inicial aún no cuenta con un bucle continuo, por lo que utiliza una pausa temporal (`time.sleep(60)`) para mantener el audio sonando antes de cerrar el programa. Puedes modificar ese número en segundos según la duración de tus pistas para evitar que se corten antes de tiempo.

## 🛠️ Próximas mejoras (Roadmap)
- [ ] Bucle continuo para cambiar de canción sin cerrar el programa.
- [ ] Controles interactivos en tiempo real (pausar, reanudar, detener y salir).
- [ ] Refactorización del código en funciones modulares.
- [ ] Soporte dinámico para la carpeta `~/Music` de cualquier usuario (`os.path.expanduser`).

## 📦 Tecnologías utilizadas
- **Python 3**
- **pygame-ce** (Motor de reproducción de audio)
- **uv** (Gestor de proyectos y paquetes)
