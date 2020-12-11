import sys
import pygame


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

player_frames = [player1, player2, player3, player4,
                 player5, player6, player7, player8, player9, player10]
player_index = 0
player_surface = player_frames[player_index]
player_rect = player_surface.get_rect(center=(375, 417))

PLAYERRUN = pygame.USEREVENT + 1
pygame.time.set_timer(PLAYERRUN, 100)

floor_x_pos = 0
pno = 1

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
                    while player_movement != -10:
                        player_movement -= gravity

        if event.type == PLAYERRUN:
            if player_index < 9:
                player_index += 1
            else:
                player_index = 0
            player_surface, player_rect = player_animation()

    screen.blit(bkgimg, (0, 0))

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
        player_movement += gravity
        player_rect.centery += player_movement
        screen.blit(player_surface, player_rect)

    floor_x_pos -= 1

    drawfloor()
    if floor_x_pos <= -2000:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(500)
