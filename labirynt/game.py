import pygame
import sys


text1 = "Twoim zadaniem jest wydostanie się z labiryntu."
text2 = "Gratuluje! Naciśnij Enter aby przejść dalej albo ESC aby opuścić grę."
text4 = "Wpadłeś w dziurę!!! Ale jeszcze jesteś żywy (ENTER)"
text5 = "Nie uważałeś wystarczająco i jesteś martwy!"

pygame.init()

screen = pygame.display.set_mode((800, 660))
pygame.display.set_caption('LABIRYNT')
font = pygame.font.Font(None, 20)
clock = pygame.time.Clock()


# objekty
player = pygame.Rect(20, 20, 20, 20)
walls = []
holes = []
door_cords = (0, 0)
lives = 4


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (player.x, player.y) in holes:
            (player.x, player.y) = (20, 20)
            if lives > 1:
                lives -= 1
            else:
                sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (player.x, player.y) == door_cords:
            sys.exit(0)

    # background
    bg = pygame.image.load("sand.jpg")
    screen.blit(bg, (0, 0))

    # setting up levels
    try:
        with open('level.txt', 'r') as file:
            level = file.readlines()
            for y in range(len(level)):
                for x in range(len(level[0])-1):
                    character = level[y][x]
                    cord_x = x * 20
                    cord_y = y * 20
                    if character == '#':
                        block_surf = pygame.image.load("grass1.jpg").convert()
                        screen.blit(block_surf, (cord_x, cord_y))
                        walls.append((cord_x, cord_y))
                    elif character == 'O':
                        whole_surf = pygame.image.load("whole.jpg").convert()
                        screen.blit(whole_surf, (cord_x, cord_y))
                        holes.append((cord_x, cord_y))
                    elif character == 'H':
                        door_surf = pygame.image.load("download.jpeg").convert()
                        screen.blit(door_surf, (cord_x, cord_y))
                        door_cords = (cord_x, cord_y)

    except FileNotFoundError:
        print("No file!")

    # control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and (player.x + 20, player.y) not in walls and (player.x, player.y) not in holes:
        player.x += 20
    if keys[pygame.K_LEFT] and (player.x - 20, player.y) not in walls and (player.x, player.y) not in holes:
        player.x -= 20
    if keys[pygame.K_UP] and (player.x, player.y - 20) not in walls and (player.x, player.y) not in holes:
        player.y -= 20
    if keys[pygame.K_DOWN] and (player.x, player.y + 20) not in walls and (player.x, player.y) not in holes:
        player.y += 20

    # player
    pygame.draw.rect(screen, (10, 230, 235), player)

    screen.fill((0, 0, 0), pygame.Rect(0, 600, 800, 60))
    label = font.render(text1, 1, (0, 255, 0))
    status_label = font.render("próby: {}".format(lives), 1, (0, 255, 0))
    screen.blit(label, (10, 605))
    screen.blit(status_label, (10, 625))

    if (player.x, player.y) in holes:
        if lives > 1:
            screen.fill((0, 0, 0), pygame.Rect(0, 600, 800, 60))
            label = font.render(text4, 1, (0, 255, 0))
            screen.blit(label, (10, 605))
        else:
            screen.fill((0, 0, 0), pygame.Rect(0, 600, 800, 60))
            label = font.render(text5, 1, (0, 255, 0))
            screen.blit(label, (10, 605))

    if (player.x, player.y) == door_cords:
            screen.fill((0, 0, 0), pygame.Rect(0, 600, 800, 60))
            label = font.render(text2, 1, (0, 255, 0))
            screen.blit(label, (10, 605))

    pygame.display.update()
    clock.tick(8)
