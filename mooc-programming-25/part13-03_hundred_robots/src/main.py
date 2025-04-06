import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0,0,0))
h_num = 1
while h_num < 10:
    w_num = 1
    while w_num < 10:
        window.blit(robot, ((h_num-1) * 0.25 * width + width * w_num, (h_num-1) * height / 4 + height))
        w_num += 1
    h_num += 1
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()