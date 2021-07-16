#I removed all the comments to clean up the code.
#I will be making a game that allows the user to control a player.
#The objective of the game is to collect the prize trophy.


#Phase 1: Importing.
#I import pygame and random for random number generation.
import pygame 
import random  



pygame.init() 



#Phase 2: Resolution.
#I select the size of the playing field for the game.
screen_width = 1280
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))


#Phase 3: Loading.
#I load in and declare the enemy, player and prize for the game.
#There will be 1 player, 1 prize and 9 enemies to make the game interesting.
#I made all three of them in paint and saved them as images.
player = pygame.image.load("Player.png")
enemy1 = pygame.image.load("Enemy.png")
enemy2 = pygame.image.load("Enemy.png")
enemy3 = pygame.image.load("Enemy.png")
enemy4 = pygame.image.load("Enemy.png")
enemy5 = pygame.image.load("Enemy.png")
enemy6 = pygame.image.load("Enemy.png")
enemy7 = pygame.image.load("Enemy.png")
enemy8 = pygame.image.load("Enemy.png")
enemy9 = pygame.image.load("Enemy.png")
prize = pygame.image.load("Prize.png")


#Phase 4: Height and Width.
#I get and declare the heights and widths of all of the objects.
image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
enemy4_height = enemy4.get_height()
enemy4_width = enemy4.get_width()
enemy5_height = enemy5.get_height()
enemy5_width = enemy5.get_width()
enemy6_height = enemy6.get_height()
enemy6_width = enemy6.get_width()
enemy7_height = enemy7.get_height()
enemy7_width = enemy7.get_width()
enemy8_height = enemy8.get_height()
enemy8_width = enemy8.get_width()
enemy9_height = enemy9.get_height()
enemy9_width = enemy9.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()


#Phase 5: Print.
#I print out the height and width of the Player the user will be playing as.
print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))


#Phase 6: Positioning.
#First i choose the position i want the player to start in.
#I chose a position in the top left hand corner.
playerXPosition = 100
playerYPosition = 50


#Secondly i randomly spawn in the enemies.
#I have three enemies coming from the right hand side and six enemies coming from the left hand side.
enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, 600)
enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, 400)
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, 200)
enemy4XPosition =  random.randint(0, 200)
enemy4YPosition =  screen_height
enemy5XPosition =  random.randint(0, 400)
enemy5YPosition =  screen_height
enemy6XPosition =  random.randint(0, 600)
enemy6YPosition =  screen_height
enemy7XPosition =  random.randint(0, 800)
enemy7YPosition =  screen_height
enemy8XPosition =  random.randint(0, 1000)
enemy8YPosition =  screen_height
enemy9XPosition =  random.randint(0, 1200)
enemy9YPosition =  screen_height


#Lastly i spawn the prize in my selected position.
#I chose right and side near the middle.
prizeXPosition = 1100
prizeYPosition = 380


#Phase 7: Declaration.
#I declare the three key variables as false to begin with and they will change later on depending on the users input.
keyUp= False
keyDown = False
keyLeft = False
keyRight = False


#Phase 8: Game Loop.
while 1:


    #I now spawn the objects on to the screen.
    screen.fill(0) 
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(enemy4, (enemy4XPosition, enemy4YPosition))
    screen.blit(enemy5, (enemy5XPosition, enemy5YPosition))
    screen.blit(enemy6, (enemy6XPosition, enemy6YPosition))
    screen.blit(enemy7, (enemy7XPosition, enemy7YPosition))
    screen.blit(enemy8, (enemy8XPosition, enemy8YPosition))
    screen.blit(enemy9, (enemy9XPosition, enemy9YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
    
       
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


        #When the user press' either of the arrow keys it will switch the variables to true effectively moving the player object.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
       
        #When the user is not pressing the arrow keys it will not move the object because the variables will remain false.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False


    #These if statements will be responsible for the movement of the objects.
    if keyUp == True:
        if playerYPosition > 0 : 
            playerYPosition -= 2 #This will move the player up.
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 2 #This will move the player down.
    if keyLeft == True:
        if playerXPosition > 0 :
            playerXPosition -= 2 #This will move the player left.
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 2 #This will move the players right.

    
    #Establishing the players box, enemies boxes and prize box for when they collide and decide the outcome of the game.
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
    enemy4Box = pygame.Rect(enemy4.get_rect())
    enemy4Box.top = enemy4YPosition
    enemy4Box.left = enemy4XPosition
    enemy5Box = pygame.Rect(enemy5.get_rect())
    enemy5Box.top = enemy5YPosition
    enemy5Box.left = enemy5XPosition
    enemy6Box = pygame.Rect(enemy6.get_rect())
    enemy6Box.top = enemy6YPosition
    enemy6Box.left = enemy6XPosition
    enemy7Box = pygame.Rect(enemy7.get_rect())
    enemy7Box.top = enemy7YPosition
    enemy7Box.left = enemy7XPosition
    enemy8Box = pygame.Rect(enemy8.get_rect())
    enemy8Box.top = enemy8YPosition
    enemy8Box.left = enemy8XPosition
    enemy9Box = pygame.Rect(enemy9.get_rect())
    enemy9Box.top = enemy9YPosition
    enemy9Box.left = enemy9XPosition


    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    

    #If the player collides with an enemy the game will end and the program will print 'you lose' telling the player they have lost the game.
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
    
        
        print("You lose!")
       
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy4Box) or playerBox.colliderect(enemy5Box) or playerBox.colliderect(enemy6Box):


        print("You lose!")


        pygame.quit()
        exit(0)


    if playerBox.colliderect(enemy7Box) or playerBox.colliderect(enemy8Box) or playerBox.colliderect(enemy9Box):


        print("You lose!")


        pygame.quit()
        exit(0)
    

    #If the player collides with the prize the game will end and the program will print 'you win' telling the player they have won the game. 
    if playerBox.colliderect(prizeBox):


        print("You Win!")


        pygame.quit()
        exit(0)
    

    #The following determines the speeds at which the enemies will move up and down the screen.
    #Some enemies move fast and some slow.
    enemy1XPosition -= 1.55
    enemy2XPosition -= 1.05
    enemy3XPosition -= 0.95
    enemy4YPosition -= 1.65
    enemy5YPosition -= 1.00
    enemy6YPosition -= 1.00
    enemy7YPosition -= 1.30
    enemy8YPosition -= 2.45
    enemy9YPosition -= 2.45


    #This is the end of the game logic.
