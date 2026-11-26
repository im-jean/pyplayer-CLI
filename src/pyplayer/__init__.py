import os
import pygame
import time

def main() -> None:
  #1 Buscar las canciones.
  musica = os.listdir("/home/jean/Music/")

  #2 Mostrar la lista de canciones.
  for numero, canciones in enumerate(musica, start=1):
    print(f"[{numero}] - {canciones}")

  #3 Iniciar el motor de audio
  pygame.mixer.init()

  #4 Pedir numero de la cancion al usuario
  cancion_seleccionada = int(input("Cancion: ")) - 1

  #4 Unir rutas
  eleccion = os.path.join("/home/jean/Music/", musica[cancion_seleccionada])

  #5 Cargar la musica
  pygame.mixer.music.load(eleccion)
  pygame.mixer.music.play()
  time.sleep(60)

if __name__ == "__main__":
  main()
