import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0,0,0))
num = 1
while num < 10:
    window.blit(robot, (width * num, height))
    num += 1
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()