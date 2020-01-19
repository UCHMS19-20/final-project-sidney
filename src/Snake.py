import pygame
import random
import sys

pygame.init()

class Snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50]]
        self.direction = "RIGHT"

    def changedirectionto(self, dir):
        if dir = "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir = "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir = "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir = "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"
    
    def move(self, foodpos):
        if self.direction = "RIGHT":
            self.position[0] += 10
        if self.direction = "LEFT":
            self.position[0] -= 10
        if self.direction = "UP":
            self.position[1] += 10
        if self.direction = "DOWN":
            self.position[1] -= 10
        self.body.insert(0, self.position)
        if self.position == foodpos:
            return 1
        else: 
            self.body.pop()
            return 0
    
    def collision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1
        for bodypart in self.body[1:]:
            if self.position = bodypart:
                 return 1
        return 0
    
    def headpos(self):
        return self.position
    
    def getbody(self):
        return self.position


class Foodspawner(self):
    def __init__(self):
        self.position = [random.randrange(1.50)*10, random.randrange(1.5) * 10]
        self.isfoodonscreen = True
    
    def spawnfood(self):
        if self.isfoodonscreen == False:
            self.position = [random.randrange(1.50)*10, random.randrange(1.5) * 10]
            self.isfoodonscreen = True
        return self.position

    def setfood(self, b):
        self.isfoodonscreen = b


def gameover():
    pygame.quit()
    sys.exit()

screen = pygame.display.set((500, 500))
pygame.display.set_caption('snake game')
clock = pygame.time.Clock()

score = 0
snake = Snake()
foodspawner = Foodspawner()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            gameover()
        elif event == pygame.KEYDOWN:
            if event == pygame.K_UP
                snake.changedirectionto('UP')
            if event == pygame.K_DOWN:
                snake.changedirectionto('DOWN')
            if event == pygame.K_RIGHT:
                snake.changedirectionto('RIGHT')
            if event == pygame.K_LEFT:
                snake.changedirectionto('LEFT')
    
    foodpos = foodspawner.spawnfood()
    if(snake.move(foodpos) == 1):
        score +=1 
        foodspawner.setfood(False)
    
    screen.fill(pygame.Color(0, 0, 0))
    for pos in snake.getbody():
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(foodpos[0], foodpos[1], 10, 10))
    if (snake.collision() == 1):
        gameover()
    pygame.display.set_caption('Snake score:' + str(score))
    pygame.display.flip()
    clock.tick(24)







