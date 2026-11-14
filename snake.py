import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((601, 601))
pygame.display.set_caption("Ran San Moi")
clock = pygame.time.Clock()
running = True
GREEN = (0, 255, 0)
RED = (255, 0, 0)
font_big = pygame.font.SysFont("Arial", 50)
font_small = pygame.font.SysFont("Arial", 25)

snakes = [[3,10],[4,10]]
direction = "Right"

x_apple = randint(1,19)
y_apple = randint(1,19)

score = 0
pausing = False

while running:
    clock.tick(10)
    screen.fill((0, 0, 0))

    tail_x = snakes[0][0]
    tail_y = snakes[0][1]

    #draw snake
    for snake in snakes:
        pygame.draw.rect(screen, GREEN, pygame.Rect(snake[0]*30,snake[1]*30,30,30))

    #draw apple
    pygame.draw.rect(screen, RED, pygame.Rect(x_apple*30,y_apple*30,30,30))

    #ran an tao
    if(snakes[-1][0] == x_apple and snakes[-1][1] == y_apple):
        snakes.insert(0, [tail_x, tail_y])
        score += 1
        while True:
            x_apple = randint(1, 19)
            y_apple = randint(1, 19)
            if [x_apple, y_apple] not in snakes:
                break

    #score
    diem = font_small.render("Scores: " + str(score), True, (255,255,255))
    screen.blit(diem, (10,10))

    #crash egde
    if snakes[-1][0] > 19 or snakes[-1][1] > 19 or snakes[-1][0] < 0 or snakes[-1][1] < 0:
        pausing = True

    #crash snake
    for i in range(len(snakes)-1):
        if(snakes[i][0] == snakes[-1][0] and snakes[i][1] == snakes[-1][1]):
            pausing = True

    #snake move
    if pausing == False:
        if direction == "Right":
            snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
            snakes.pop(0)
        elif direction == "Left":
            snakes.append([snakes[-1][0] - 1, snakes[-1][1]])
            snakes.pop(0)
        elif direction == "Down":
            snakes.append([snakes[-1][0], snakes[-1][1]+1])
            snakes.pop(0)
        elif direction == "Up":
            snakes.append([snakes[-1][0], snakes[-1][1]-1])
            snakes.pop(0)

    if pausing:
        game_over = font_big.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over, (180, 250))
        space = font_big.render("Press SPACE to continue", True, (255, 255, 255))
        screen.blit(space, (70, 330))
        final_score = font_big.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(final_score, (220, 170))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "Down":
                direction = "Up"
            elif event.key == pygame.K_DOWN and direction != "Up":
                direction = "Down"
            elif event.key == pygame.K_LEFT and direction != "Right":
                direction = "Left"
            elif event.key == pygame.K_RIGHT and direction != "Left":
                direction = "Right"
            elif event.key == pygame.K_SPACE:
                pausing = False
                score = 0
                snakes.clear()
                snakes.append([3,10])
                snakes.append([4,10])
                x_apple = randint(1,19)
                y_apple = randint(1,19)
                direction = "Right"

    pygame.display.flip()
pygame.quit()
