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
   git clone https://github.com
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

## 📄️ ¿Cómo modificar el programa?
#1 Establecer la ruta de la musica.
- Dentro de la primera variable(musica), tienes que modificar la ruta dentro de los parentesis (home/carpeta/carpeta) con la ruta donde tienes tus canciones en .mp3 .wav, etc. 
<strong>Aviso: Las canciones deben estar sueltas y no metidas en carpetas, si no el programa no podrá leerlas</strong>

#2 Agregar tiempo de reproducción.
- Si sabes lo que hace el programa por dentro, debes saber que no posee alguna función que te deje reproducir musica sin importar el tiempo, como este es una version cruda, es lo basico y deberás cambiar el tiempo de time.sleep(aca el tiempo de tu musica) y que no se corte de inmediato.

## 🛠️ Próximas mejoras (Roadmap)
- [ ] Bucle continuo para cambiar de canción sin cerrar el programa.
- [ ] Controles interactivos en tiempo real (pausar, reanudar, detener y salir).
- [ ] Refactorización del código en funciones modulares.
- [ ] Soporte dinámico para la carpeta `~/Music` de cualquier usuario (`os.path.expanduser`).

## 📦 Tecnologías utilizadas
- **Python 3**
- **pygame-ce** (Motor de reproducción de audio)
- **uv** (Gestor de proyectos y paquetes)
