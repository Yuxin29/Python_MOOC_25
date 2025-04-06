import pygame
import random

pygame.init()
window = pygame.display.set_mode((640,480))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0,0,0))
number = 0
while number < 1000:
    h = random.randint(0, 480 - height)
    w = random.randint(0, 640 - width)
    window.blit(robot, (w, h))
    number += 1
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()