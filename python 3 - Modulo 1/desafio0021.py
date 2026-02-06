import pygame

pygame.init()
pygame.mixer.init()

from tkinter import filedialog

arquivo = filedialog.askopenfilename()

pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()

rodando = True

while rodando:
    input("A música está tocando. Aperte ENTER para parar.")
    pygame.mixer.music.stop()
    rodando = False