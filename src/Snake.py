# Imports all required Libraries
import pygame
import random
import sys

# Global variables ar creatd 
pygame.init()
font = pygame.font.SysFont(None, 25)
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

#Class for the snake
class Snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"

    def changedirectionto(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"
    
    def move(self, foodpos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10
        self.body.insert(0, list(self.position))
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
            if self.position == bodypart:
                 return 1
        return 0
    
    def headpos(self):
        return self.position
    
    def getbody(self):
        return self.body

#class for the foodspawner
class Foodspawner():
    def __init__(self):
        self.position = [random.randrange(1,50)*10, random.randrange(1,5) * 10]
        self.isfoodonscreen = True
    
    def spawnfood(self):
        if self.isfoodonscreen == False:
            self.position = [random.randrange(1,50)*10, random.randrange(1,5) * 10]
            self.isfoodonscreen = True
        return self.position

    def setfood(self, b):
        self.isfoodonscreen = b

# Function to print text on the screen with required parameters
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])

#Function to display the game over screen 
def gameover_screen():
    #Establishes internal variables
    ending_rect = pygame.Rect((50, 100), (400, 200))
    replay_game = False

    #Main while loop
    while replay_game == False:
        #Prints screen, rectangle, and text
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), ending_rect)
        text_screen("You Lost", pygame.Color(54, 255, 51), 70, 110)
        text_screen("Press Spacebar to Play Again", pygame.Color(54, 255, 51), 70, 160)
        
        #Awaits response
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
        
        #Updates screen
        pygame.display.update()
        clock.tick(24)

#function to end the program
def gameover():
    pygame.quit()
    sys.exit()





#function to run the welcom screen
def welcomescreen():
    #Establishes some internal variables
    exit_game = False
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Welcome to Snek Game')
    welcome_rect = pygame.Rect((50, 100), (400, 200))

    #main while loop
    while exit_game == False:
        #Draws rectangles and prints text
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), welcome_rect)
        text_screen("Welcome to The Snek Game", pygame.Color(54, 255, 51), 70, 110)
        text_screen("Press Spacebar to Play", pygame.Color(54, 255, 51), 70, 160)
        
        #Awaits Response
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
        
        #Updates the screen
        pygame.display.update()
        clock.tick(24)
        




# main gameloop
def main():
    # creates some internal variables
    score = 0
    snake = Snake()
    foodspawner = Foodspawner()
    
    #main game while loop
    while True:

        #Establishes key stroke inputs
        pygame.display.set_caption('Snek Game')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.changedirectionto('UP')
                if event.key == pygame.K_DOWN:
                    snake.changedirectionto('DOWN')
                if event.key == pygame.K_RIGHT:
                    snake.changedirectionto('RIGHT')
                if event.key == pygame.K_LEFT:
                    snake.changedirectionto('LEFT')
        
        #spawns food
        foodpos = foodspawner.spawnfood()

        #Check if food is collected
        if(snake.move(foodpos) == 1):
            score +=1 
            foodspawner.setfood(False)
        
        #Prints the snake
        screen.fill(pygame.Color(0, 0, 0))
        for pos in snake.getbody():
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(foodpos[0], foodpos[1], 10, 10))

        #Check for collision and update the screen     
        if (snake.collision() == 1):
            gameover_screen()
        pygame.display.set_caption('Snake score:' + str(score))
        pygame.display.flip()
        clock.tick(24)


welcomescreen()










