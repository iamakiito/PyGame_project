#  Игра "Саймон говорит"
#  Проект на PyGame для Яндекс.Лицея
#  От Владыкина И.С.

import pygame, random, time, sys


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# ЦВЕТА
red = pygame.Color('red')
light_red = pygame.Color('firebrick')
green = pygame.Color('green')
light_green = pygame.Color('lightgreen')
yellow = pygame.Color('yellow')
light_yellow = pygame.Color('lightyellow')
blue = pygame.Color('blue')
light_blue = pygame.Color('lightblue')
white = pygame.Color('white')
black = pygame.Color('black')

# КНОПКИ
green_button = green
blue_button = blue
yellow_button = yellow
red_button = red

# ШРИФТ
font_path = './data/font.ttf'
font = pygame.font.Font(font_path, 20)
title_font = pygame.font.Font(font_path, 50)

# КАРТИНКИ
logo = pygame.image.load('./data/img/simon_logo.png')
big_logo = pygame.transform.scale(logo, (300, 300))
start_button = pygame.transform.scale(pygame.image.load('./data/img/start_button.png'), (240, 90))
again_button = pygame.transform.scale(pygame.image.load('./data/img/again_button.png'), (240, 90))
exit_button = pygame.transform.scale(pygame.image.load('./data/img/exit_button.png'), (240, 90))

# ЗВУКИ
main_theme = pygame.mixer.Sound('./data/audio/main_theme.ogg')
lose_sound = pygame.mixer.Sound('./data/audio/lose.wav')
red_sound = pygame.mixer.Sound('./data/audio/red.wav')
yellow_sound = pygame.mixer.Sound('./data/audio/yellow.wav')
blue_sound = pygame.mixer.Sound('./data/audio/blue.wav')
green_sound = pygame.mixer.Sound('./data/audio/green.wav')

screen = pygame.display.set_mode((600,700))
pygame.display.set_icon(logo)
pygame.display.set_caption('Саймон говорит')

score = 0
pattern = []
time_delay = 500
running = True


def render_screen(g=green, r=red, y=yellow, b=blue):
    screen.fill(black)
    score_txt = font.render('Счёт: ' + str(score), True, white)
    screen.blit(score_txt, (450, 50))

    pygame.draw.rect(screen, g, pygame.Rect(50, 150, 250, 250))
    pygame.draw.rect(screen, r, pygame.Rect(300, 150, 250, 250))
    pygame.draw.rect(screen, y, pygame.Rect(50, 400, 250, 250))
    pygame.draw.rect(screen, b, pygame.Rect(300, 400, 250, 250))

    pygame.display.update()


def show_pattern():
    time_delay = 500 - 100 * int(len(pattern) / 5)
    if time_delay <= 100:
        time_delay = 100

    render_screen()
    pygame.time.delay(1000)

    for x in pattern:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        if x == 1:
            # ЗЕЛЁНЫЙ
            render_screen(g=light_green)
            green_sound.play()
            pygame.time.delay(time_delay)
            render_screen()
            green_sound.stop()
        elif x == 2:
            # КРАСНЫЙ
            render_screen(r=light_red)
            red_sound.play()
            pygame.time.delay(time_delay)
            render_screen()
            red_sound.stop()
        elif x == 3:
            # ЖЁЛТЫЙ
            render_screen(y=light_yellow)
            yellow_sound.play()
            pygame.time.delay(time_delay)
            render_screen()
            yellow_sound.stop()
        elif x == 4:
            # СИНИЙ
            render_screen(b=light_blue)
            blue_sound.play()
            pygame.time.delay(time_delay)
            render_screen()
            blue_sound.stop()

        pygame.time.delay(time_delay)


def new_pattern():
    global score
    score = len(pattern)
    pattern.append(random.randint(1, 4))


def check_pattern(player_pattern):
    if player_pattern != pattern[:len(player_pattern)]:
        lose_screen()


def click_listen():
    turn_time = time.time()
    player_pattern = []

    while time.time() <= turn_time + 3 and len(player_pattern) < len(pattern):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 50 < x < 300 and 150 < y < 400:
                    render_screen(g=light_green)
                    green_sound.play()
                    pygame.time.delay(time_delay)
                    green_sound.stop()
                    render_screen()
                    player_pattern.append(1)
                    check_pattern(player_pattern)
                    turn_time = time.time()
                elif 300 < x < 550 and 150 < y < 400:
                    render_screen(r=light_red)
                    red_sound.play()
                    pygame.time.delay(time_delay)
                    red_sound.stop()
                    render_screen()
                    player_pattern.append(2)
                    check_pattern(player_pattern)
                    turn_time = time.time()
                elif 50 < x < 300 and 400 < y < 650:
                    render_screen(y=light_yellow)
                    yellow_sound.play()
                    pygame.time.delay(time_delay)
                    yellow_sound.stop()
                    render_screen()
                    player_pattern.append(3)
                    check_pattern(player_pattern)
                    turn_time = time.time()
                elif 300 < x < 550 and 400 < y < 650:
                    render_screen(b=light_blue)
                    blue_sound.play()
                    pygame.time.delay(time_delay)
                    blue_sound.stop()
                    render_screen()
                    player_pattern.append(4)
                    check_pattern(player_pattern)
                    turn_time = time.time()

    if not time.time() <= turn_time + 3:
        lose_screen()


def quit_game():
    running = False
    pygame.display.quit()
    pygame.quit()
    sys.exit()


def lose_screen():
    lose_sound.play()
    global  score

    screen.fill(black)
    lose_txt = title_font.render('Вы проиграли', True, white)
    score_txt = title_font.render('Счёт: ' + str(score), True, white)
    screen.blit(lose_txt, (150, 50))
    screen.blit(score_txt, (((600 - title_font.size('Счёт: ' + str(score))[0]) / 2), 120))
    screen.blit(again_button, (180, 300))
    screen.blit(exit_button, (180, 450))

    pygame.display.update()

    #ОБНУЛЕНИЕ
    score = 0
    global pattern
    pattern = []
    global time_delay
    time_delay = 500
    global running
    running = True

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 180 <= x <= 420 and 300 <= y <= 390:
                    start_menu()
                elif 180 <= x <= 420 and 450 <= y <= 540:
                    quit_game()


def start_menu():
    waiting = True
    main_theme.play(-1)
    logo_movement = 150
    title_txt = title_font.render('Саймон говорит', True, white)

    logo_movement_direction = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 180 <= x <= 420 and 530 <= y <= 620:
                    main_theme.stop()
                    waiting = False

        screen.fill(black)

        screen.blit(title_txt, (135, 50))
        screen.blit(big_logo, (150, logo_movement))
        screen.blit(start_button, (180, 530))
        pygame.display.update()

        if logo_movement == 150:
            pygame.time.delay(300)
            logo_movement_direction = True
        elif logo_movement == 190:
            pygame.time.delay(300)
            logo_movement_direction = False

        if logo_movement_direction:
            logo_movement += 0.5
        else:
            logo_movement -= 0.5

        clock.tick(60)

    while running:
        new_pattern()
        show_pattern()
        click_listen()


start_menu()