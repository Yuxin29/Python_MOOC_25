import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
clock = pygame.time.Clock()

def create_random_robot():
    return {
        'x': random.randint(robot.get_width(),640) - robot.get_width(),
        'y': -robot.get_height(),
    }
robots = []

while True:
    if random.randint(1,1000) % 78 == 0:
        robots.append(create_random_robot())
    window.fill((0, 0, 0))
    for obj in robots:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        if obj['y'] < 480 - robot.get_height():
            obj['y'] += 2
        if obj['y'] == 480 - robot.get_height() and obj['x'] <= 640:
            if obj['x'] >= 320 - robot.get_width():
                obj['x'] += 2
            else: 
                obj['x'] -= 2
        window.blit(robot, (obj['x'], obj['y']))
    clock.tick(60)
    pygame.display.flip()