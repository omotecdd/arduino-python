import pygame
import serial

pygame.init()
X = 600
Y = 600

scrn = pygame.display.set_mode((X, Y))

pygame.display.set_caption('image')

sun = pygame.image.load("sun.jpg").convert()
moon = pygame.image.load("moon.jpg").convert()

ser = serial.Serial('COM3', 9600)

while True:
    x = str(ser.readline())
    y = x.strip("b'rn\\")
    print(y)
    if y=='1':
        scrn.blit(sun, (0, 0))
        pygame.display.flip()
    if y=='0':
        scrn.blit(moon, (0, 0))
        pygame.display.flip()