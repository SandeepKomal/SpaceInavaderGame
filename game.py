import pygame
import random
import math
from pygame import mixer
#import warnings
#from warnings  warnings("ignore")

# initaiaze pygame
pygame.init()

# create the screen
# width 800 and height 600
screen = pygame.display.set_mode((800, 600))

# background image

background = pygame.image.load('bg.jpg')

# background music

mixer.music.load('space_line.wav')
mixer.music.play(-1)

# title and icon

pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
PlayerImg = pygame.image.load('player 2.png')
PlayerX = 370
PlayerY = 500
PlayerX_change = 0
# PlayerY_change=0

# enemy 1
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
number_of_enemies = 6
for i in range(number_of_enemies):
    EnemyImg.append(pygame.image.load('alien.png'))
    EnemyX.append(random.randint(0, 735))
    EnemyY.append(random.randint(30, 170))
    EnemyX_change.append(0.5)
    EnemyY_change.append(20)
    #number_of_enemies += 1

# bullet
# ready - you cant see the bullet on the screen
# fire - the bullet is currently moving
bulletimg = pygame.image.load('bullets.png')
BulletX = 0
BulletY = 500
BulletY_change = 1
BulletX_change = 0
bullet_state = 'ready'
#score
score_value = 0
font = pygame.font.Font('Waffle Story.ttf', 30)
TextX = 10
TextY = 10

#game over text
game_over_font = pygame.font.Font('Waffle Story.ttf', 65)




def score(x, y):
    score = font.render("Score:" + str(score_value), True, ((250, 128, 114)))
    screen.blit(score, (x, y))

def game_over_text(x, y):
    game_over = game_over_font.render("GAME OVER" , True, ((250, 128, 114)))
    screen.blit(game_over, (200, 250))

def player(x, y):
    screen.blit(PlayerImg, (x, y))


def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


def is_Collision(EnemyX, EnemyY, BulletX, BulletY):
    distance = math.sqrt((math.pow(EnemyX - BulletX, 2)) + (math.pow(EnemyY - BulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop infinite loop which the game doesn't quit until unless we click on close or quit

running = True
while running:
    # red blue Green
    screen.fill((0, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # when keys are pressed and released
        if event.type == pygame.KEYDOWN:
            # print("pressed someother key")
            if event.key == pygame.K_LEFT:
                PlayerX_change = -2

            if event.key == pygame.K_RIGHT:
                PlayerX_change = 2

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('arcbsmm.wav')
                    bullet_sound.play()
                    BulletX = PlayerX
                    fire_bullet(BulletX, BulletY)

            # if event.key == pygame.K_UP:
            # PlayerY_change = -0.3

            # if event.key == pygame.K_DOWN:
            # PlayerY_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0
            # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            # PlayerY_change = 0

    PlayerX += PlayerX_change
    if PlayerX <= 0:
        PlayerX = 0
    if PlayerX >= 736:
        PlayerX = 736
    for i in range(number_of_enemies):

        #game over
        if EnemyY[i] >440:
            game_over_sound = mixer.Sound('govdsf.wav')
            game_over_sound.play()
            for j in range( number_of_enemies):
                EnemyY[j]= 2000

            game_over_text(200,250)
            break
        EnemyX[i] += EnemyX_change[i]
        if EnemyX[i] <= 0:
            EnemyX_change[i] = 0.8
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -0.8
            EnemyY[i] += EnemyY_change[i]

            # collision
        collision = is_Collision(EnemyX[i], EnemyY[i], BulletX, BulletY)
        if collision:
            collision_sound = mixer.Sound('coll.wav')
            collision_sound.play()
            BulletY = 480
            bullet_state = "ready"
            score_value += 1
            # print(score)
            EnemyX[i] = random.randint(0, 735)
            EnemyY[i] = random.randint(30, 170)
        enemy(EnemyX[i], EnemyY[i], i)

    # bullet movement

    if BulletY < 0:
        BulletY = 480
        bullet_state = "ready"  # multiple bullets

    if bullet_state is "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change

    # PlayerY += PlayerY_change
    player(PlayerX, PlayerY)
    score(TextX, TextY)

    pygame.display.update()
