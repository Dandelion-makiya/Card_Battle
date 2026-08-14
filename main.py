import pygame
import sys
import config
import game


def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Card Battle")
    clock = pygame.time.Clock()

    game_instance = game.Game(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_instance.handle_click(event.pos[0], event.pos[1])

        game_instance.update()
        game_instance.render()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
