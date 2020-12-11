import pygame
import sys


def player_animation():
    new_player = player_frames[player_index]
    new_player_rect = new_player.get_rect(center=(250, player_rect.centery))
    return new_player, new_player_rect


# Bullet class
class bullets(object):
    def __init__(self, x, y, length, breadth, color):
        self.x = x
        self.y = y
        self.length = length
        self.breadth = breadth
        self.color = color
        self.velocity = 10

    def drawbullet(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.x, self.y, self.length, self.breadth))


def create_pipe():
    new_pipe = pipe_suface.get_rect(midtop=(1020, 452))
    return new_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 15
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_suface, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if player_rect.colliderect(pipe):
            hit_sound.play()
            return False
    return True


def drawfloor():

    screen.blit(landimg, (floor_x_pos, 550))
    screen.blit(landimg, (floor_x_pos+500, 550))
    screen.blit(landimg, (floor_x_pos+1000, 550))
    screen.blit(landimg, (floor_x_pos+1500, 550))
    screen.blit(landimg, (floor_x_pos+2000, 550))
    screen.blit(landimg, (floor_x_pos+2500, 550))


def updateFile():
    f = open('scores.txt', 'r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score

    return last


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(
            str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(512, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(str(score), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(512, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(
            str(bestscore), True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(512, 500))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()


player_movement = 0
gravity = 0.25
hertz = 100
game_active = True
score = 0


BLACK = (0, 0, 0)

# bkgimg = pygame.image.load('Assets/bkimg23.jpg').convert()  # Alternate Background
bkgimg = pygame.image.load('Assets/sky.png').convert()
bkgimg = pygame.transform.scale(bkgimg, (1024, 600))
# landimg = pygame.image.load('Assets/moon.jpeg').convert() #Alternate Surface
landimg = pygame.image.load('Assets/landing5.png').convert()
# landimg = pygame.image.load('Assets/landing2.png').convert()
landimg = pygame.transform.scale(landimg, (1024, 768))
player1 = pygame.image.load('Assets/Player/player1.png').convert()
player1.set_colorkey(BLACK)
player2 = pygame.image.load('Assets/Player/player2.png').convert()
player2.set_colorkey(BLACK)
player3 = pygame.image.load('Assets/Player/player3.png').convert()
player3.set_colorkey(BLACK)
player4 = pygame.image.load('Assets/Player/player4.png').convert()
player4.set_colorkey(BLACK)
player5 = pygame.image.load('Assets/Player/player5.png').convert()
player5.set_colorkey(BLACK)
player6 = pygame.image.load('Assets/Player/player6.png').convert()
player6.set_colorkey(BLACK)
player7 = pygame.image.load('Assets/Player/player7.png').convert()
player7.set_colorkey(BLACK)
player8 = pygame.image.load('Assets/Player/player8.png').convert()
player8.set_colorkey(BLACK)
player9 = pygame.image.load('Assets/Player/player9.png').convert()
player9.set_colorkey(BLACK)
player10 = pygame.image.load('Assets/Player/player10.png').convert()
player10.set_colorkey(BLACK)
deathstar = pygame.image.load('Assets/deathstar1.jpg').convert()


game_begin_surface = pygame.image.load('Retro.png')
game_begin_surface = pygame.transform.scale(game_begin_surface, (1024, 768))
game_begin_surface_rect = game_begin_surface.get_rect(center=(512, 384))

game_over_surface = pygame.image.load('Assets/gameover.jpg')
game_over_surface = pygame.transform.scale(game_over_surface, (1024, 768))
game_over_surface_rect = game_over_surface.get_rect(center=(512, 384))
game_font = pygame.font.Font(
    'assets/fonts/BigShouldersStencilText-Medium.ttf', 40)

# Pipes image.
pipe_surface = pygame.image.load('assets/Obstacles/pipe-green.png').convert()
pipe_suface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 2000)


player_frames = [player1, player2, player3, player4,
                 player5, player6, player7, player8, player9, player10]
player_index = 0
player_surface = player_frames[player_index]
player_rect = player_surface.get_rect(center=(250, 492))

PLAYERRUN = pygame.USEREVENT + 1
pygame.time.set_timer(PLAYERRUN, 100)

floor_x_pos = 0
pno = 1

# sound effects
hit_sound = pygame.mixer.Sound('assets/sounds/sound_effects/Hit.ogg')
point_sound = pygame.mixer.Sound('assets/sounds/sound_effects/Point.ogg')
point_sound_count = 100

bullet_list = []
obstacle_list = []
MainGame = False
BeginGame = True


while BeginGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                point_sound.play()
                BeginGame = False
                MainGame = True

    screen.blit(game_begin_surface, game_begin_surface_rect)

    pygame.display.update()
    clock.tick(hertz)
    hertz += 0.02


while MainGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                point_sound.play()
                if player_rect.centery == 492:
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
        if bullet.x < 1024 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullet_list.pop(bullet_list.index(bullet))

    screen.blit(bkgimg, (0, 0))

    if game_active == True:
        if player_rect.centery == 492:
            gravity = 0
        elif player_rect.centery < 492:
            gravity = 0.25

        else:
            gravity = 0
            player_rect.centery = 492
            player_movement = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_END]:
            if(len(bullet_list) < 1):
                bullet_list.append(
                    bullets(250, player_rect.centery, 15, 3, (255, 255, 153)))
        for bullet in bullet_list:
            bullet.drawbullet(screen)

        player_movement += gravity
        player_rect.centery += player_movement
        screen.blit(player_surface, player_rect)
        game_active = check_collision(pipe_list)
        score_display('main_game')
        floor_x_pos -= 5

        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        drawfloor()
        if floor_x_pos <= -2000:
            floor_x_pos = 0
        score = int(hertz//0.1-999)
        largeFont = pygame.font.SysFont('comicsans', 30)
        text = largeFont.render('Score: ' + str(score), 1, (255, 255, 255))
        largeFont = pygame.font.SysFont('comicsans', 80)
        bestscore = updateFile()
    else:
        pipe_list.clear()
        screen.blit(game_over_surface, game_over_surface_rect)
        score_display('game_over')

    pygame.display.update()
    clock.tick(hertz)
    hertz += 0.02