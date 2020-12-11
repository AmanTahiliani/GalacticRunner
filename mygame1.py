import sys
import pygame
import random


def player_animation():
    new_player = player_frames[player_index]
    new_player_rect = new_player.get_rect(center=(375, player_rect.centery))
    return new_player, new_player_rect


def drawfloor():

    screen.blit(landimg, (floor_x_pos, 475))
    screen.blit(landimg, (floor_x_pos + 500, 475))
    screen.blit(landimg, (floor_x_pos + 1000, 475))
    screen.blit(landimg, (floor_x_pos + 1500, 475))
    screen.blit(landimg, (floor_x_pos + 2000, 475))
    screen.blit(landimg, (floor_x_pos + 2500, 475))

    # if pno==1:
    #     screen.blit(player1,(200,237))
    # elif pno==2:
    #     screen.blit(player2,(200,237))
    # elif pno==3:
    #     screen.blit(player3,(200,237))
    # elif pno==4:
    #     screen.blit(player4,(200,237))
    # elif pno==5:
    #     screen.blit(player5,(200,237))
    # elif pno==6:
    #     screen.blit(player6,(200,237))
    # elif pno==7:
    #     screen.blit(player7,(200,237))
    # elif pno==8:
    #     screen.blit(player8,(200,237))
    # elif pno==9:
    #     screen.blit(player9,(200,237))
    # elif pno==10:
    #     screen.blit(player10,(200,237))


class bullets(object):
    # Bullet class
    def __init__(self, x, y, length, breadth, color):
        self.x = x
        self.y = y
        self.length = length
        self.breadth = breadth
        self.color = color
        self.velocity = 7

    def drawbullet(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.x, self.y, self.length, self.breadth))


# class obstacles(object):
#     # Obstacle class
#     def __init__(self, obstacle, x, y, height, width):
#         self.image = obstacle
#         self.x = x
#         self.y = y
#         self.height = height
#         self.width = width
#         self.box = (x, y, width, height)
#         self.velocity = 1

#     def drawobstacle(self, screen):
#         self.box = (self.x, self.y, self.width-10, self.height)
#         screen.blit(pygame.transform.scale(
#             self.image, (64, 64)), (self.x, self.y))
#         pygame.draw.rect(screen, (255, 0, 0), self.box, 2)


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    new_pipe = pipe_suface.get_rect(midtop=(1500, random_pipe_pos))
    return new_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_suface, pipe)

# def check_collision(pipes):
    # for pipe in pipes:
        # for bullet in bullet_list:
        # if bullet.colliderect(pipe):
        # point_sound.play()


pygame.init()
screen = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()

player_movement = 0
gravity = 0.25
game_active = True

bkgimg = pygame.image.load('Assets/Hyades.jpg').convert()
bkgimg = pygame.transform.scale2x(bkgimg)
landimg = pygame.image.load('Assets/moon.jpeg').convert()
player1 = pygame.image.load('Assets/Player/player1.png').convert()
player2 = pygame.image.load('Assets/Player/player2.png').convert()
player3 = pygame.image.load('Assets/Player/player3.png').convert()
player4 = pygame.image.load('Assets/Player/player4.png').convert()
player5 = pygame.image.load('Assets/Player/player5.png').convert()
player6 = pygame.image.load('Assets/Player/player6.png').convert()
player7 = pygame.image.load('Assets/Player/player7.png').convert()
player8 = pygame.image.load('Assets/Player/player8.png').convert()
player9 = pygame.image.load('Assets/Player/player9.png').convert()
player10 = pygame.image.load('Assets/Player/player10.png').convert()
deathstar = pygame.image.load('Assets/deathstar1.jpg').convert()
# obstacle = pygame.image.load('Assets/Obstacles/1.jpg').convert()

# Pipes image.
pipe_surface = pygame.image.load('assets/Obstacles/1.jpg').convert()
pipe_suface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

bullet_list = []
obstacle_list = []
# obstacle_list.append(obstacles(obstacle, 1000, 200, 64, 64))

player_frames = [player1, player2, player3, player4,
                 player5, player6, player7, player8, player9, player10]
for i in range(len(player_frames)):
    player_frames[i] = pygame.transform.scale(player_frames[i], (100, 113))

player_index = 0
player_surface = player_frames[player_index]
player_rect = player_surface.get_rect(center=(375, 417))

PLAYERRUN = pygame.USEREVENT + 1
pygame.time.set_timer(PLAYERRUN, 100)

floor_x_pos = 0
pno = 1

# point_sound = pygame.mixer.Sound('assets/sounds/sound_effects/Point.ogg')
# point_sound_count = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                if player_rect.centery == 417:
                    player_movement = 0
                    gravity = 0.25
                    while player_movement != -12:
                        player_movement -= gravity

        if event.type == PLAYERRUN:
            if player_index < 9:
                player_index += 1
            else:
                player_index = 0
            player_surface, player_rect = player_animation()
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

    for bullet in bullet_list:
        if bullet.x < 1366 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullet_list.pop(bullet_list.index(bullet))

    screen.blit(bkgimg, (0, 0))

    if game_active == True:
        if player_rect.centery == 417:
            gravity = 0
        elif player_rect.centery < 417:
            gravity = 0.25
        else:
            gravity = 0
            player_rect.centery = 417
            player_movement = 0
        pipe_list = move_pipes(pipe_list)
        pipe_height = [300, 350, 400, 450, 500, 550]
        draw_pipes(pipe_list)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_END]:
            if(len(bullet_list) < 1):
                bullet_list.append(
                    bullets(375, player_rect.centery, 15, 3, (255, 255, 153)))
        for bullet in bullet_list:
            bullet.drawbullet(screen)
        player_movement += gravity
        player_rect.centery += player_movement
        screen.blit(player_surface, player_rect)

    floor_x_pos -= 1

    drawfloor()
    if floor_x_pos <= -2000:
        floor_x_pos = 0

    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)
    pygame.display.update()
    clock.tick(500)
