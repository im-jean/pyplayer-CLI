import os
import pygame
import time

musica = os.listdir("/home/jean/Music/")
pygame.mixer.init()

def lista_canciones():
  for numero, canciones in enumerate(musica, start=1):
    print(f"[{numero}] - {canciones}")


def unir_pistas():
  cancion_seleccionada = int(input("~# ")) - 1
  eleccion = os.path.join("/home/jean/Music/", musica[cancion_seleccionada])
  return eleccion

def reproducir(eleccion):
  pygame.mixer.music.load(eleccion)
  pygame.mixer.music.play()
  time.sleep(60)


def main() -> None:
  lista_canciones()
  eleccion = unir_pistas()
  reproducir(eleccion)

if __name__ == "__main__":
  main()