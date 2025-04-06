import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x1 = 320+math.cos(angle)*140-robot.get_width()/2
    y1 = 240+math.sin(angle)*140-robot.get_height()/2
    x2 = 320+math.cos(angle + 40)*140-robot.get_width()/2
    y2 = 240+math.sin(angle + 40)*140-robot.get_height()/2
    x3 = 320+math.cos(angle + 80)*140-robot.get_width()/2
    y3 = 240+math.sin(angle + 80)*140-robot.get_height()/2
    x4 = 320+math.cos(angle + 120)*140-robot.get_width()/2
    y4 = 240+math.sin(angle + 120)*140-robot.get_height()/2
    x5 = 320+math.cos(angle + 160)*140-robot.get_width()/2
    y5 = 240+math.sin(angle + 160)*140-robot.get_height()/2
    x6 = 320+math.cos(angle + 200)*140-robot.get_width()/2
    y6 = 240+math.sin(angle + 200)*140-robot.get_height()/2
    x7 = 320+math.cos(angle + 240)*140-robot.get_width()/2
    y7 = 240+math.sin(angle + 240)*140-robot.get_height()/2
    x8 = 320+math.cos(angle + 280)*140-robot.get_width()/2
    y8 = 240+math.sin(angle + 280)*140-robot.get_height()/2
    x9 = 320+math.cos(angle + 320)*140-robot.get_width()/2
    y9 = 240+math.sin(angle + 320)*140-robot.get_height()/2
    x10 = 320+math.cos(angle + 360)*140-robot.get_width()/2
    y10 = 240+math.sin(angle + 360)*140-robot.get_height()/2

    window.fill((0, 0, 0))
    xy = {(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9), (x10, y10)}
    for item in xy:
        window.blit(robot, item)
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)