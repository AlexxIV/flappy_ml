import pygame
from helpers.constants import BG_IMG, STAT_FONT, WIN_WIDTH


def draw_window(win, birds, pipes, base, score, gen, vel):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    text = STAT_FONT.render("Gen: " + str(gen), 1, (255, 255, 255))
    win.blit(text, (10, 10))

    text = STAT_FONT.render("Velocity: " + str(vel), 1, (255, 255, 255))
    win.blit(text, (10, 50))

    base.draw(win)
    for bird in birds:
        bird.draw(win)
    pygame.display.update()
