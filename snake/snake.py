import pygame as pg
import time
import random

pg.init()

green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

width, height = 800, 400
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Snake game")

icon = pg.image.load("image.png")
pg.display.set_icon(icon)

pg.font.init()

snake_block = 10
snake_speed = 15

clock = pg.time.Clock()

def snake(snake_block, snake_list):
    for i in snake_list:
        pg.draw.rect(screen, green, [i[0], i[1], snake_block, snake_block])

font_style = pg.font.Font(None, 25)

def display_score(score):
    score_surface = font_style.render(f"Score: {score}", False, white)
    screen.blit(score_surface, (0,0))

def display_game_lost():
    game_lost_surface = font_style.render("You lost!", False, white)
    screen.blit(game_lost_surface, (width/2, height/2))

def game_loop():
    snake_x, snake_y = width // 2, height // 2
    x, y = 0, 0
    snake_list = []
    snake_length = 1

    apple_x = round(random.randrange(0, width - snake_block) /10.0) * 10.0
    apple_y = round(random.randrange(0, height - snake_block) /10.0) * 10.0  

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x = -snake_block
                    y = 0
                elif event.key == pg.K_RIGHT:
                    x = snake_block
                    y = 0
                elif event.key == pg.K_UP:
                    x = 0
                    y = -snake_block
                elif event.key == pg.K_DOWN:
                    x = 0
                    y = snake_block 
                elif event.key == pg.K_ESCAPE:
                    pg.quit()

        if snake_y >= height or snake_y < 0 or  snake_x < 0 or snake_x >= width:
            display_game_lost()
            pg.display.update()
            time.sleep(1)
            pg.quit()
        
        snake_x += x
        snake_y += y
        #print(snake_x, x, snake_y, y)
        screen.fill(black)
        pg.draw.rect(screen, red, [apple_x, apple_y, 10, 10])
 
        snakeHead = []
        snakeHead.append(snake_x)
        snakeHead.append(snake_y)
        snake_list.append(snakeHead)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snakeHead:
                pg.quit()

        if apple_x == snake_x and apple_y == snake_y:
            apple_x = round(random.randrange(0, width - snake_block) /10.0) * 10.0
            apple_y = round(random.randrange(0, height - snake_block) /10.0) * 10.0
            snake_length += 1

        display_score(snake_length-1)
        snake(snake_block, snake_list)
        pg.display.update()

        clock.tick(snake_speed)

if __name__ == '__main__':
    game_loop()
