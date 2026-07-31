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

        game_instance.update()
        game_instance.render()

        pygame.display.flip()
        clock.tick(120)


if __name__ == "__main__":
    main()






# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
#     pygame.display.set_caption("Title")
#     clock = pygame.time.Clock()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         screen.fill(config.BLACK)
#         font = pygame.font.SysFont("SimHei", 48)
#         surface = font.render("卡牌战斗", True, config.WHITE)
#         screen.blit(surface,(100,100))
#         pygame.display.flip()

#         clock.tick(120)




# if __name__ == "__main__":
#     main()




    # def main():
    # pygame.init()
    # screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    # pygame.display.set_caption("Title")
    # # 实例化节拍器，就是default的时钟对象，用于控制游戏循环的频率，类似delay
    # clock = pygame.time.Clock()

    # x = 100
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #     screen.fill(config.BLACK)

    #     rect = pygame.draw.rect(screen, config.GOLD, (x, 100, 100, 100))
    #     # Font参数（字体类型的路径，字体大小）
    #     font = pygame.font.Font(None, 36)
    #     text = font.render("Hello, Pygame!", True, config.WHITE)
    #     screen.blit(text, (25, 25))
    #     x += 2
    #     if x > config.SCREEN_WIDTH:
    #         x = 0

    #     pygame.display.flip()
       
    #     clock.tick(120)

#     函数	参数1是什么	举例
# pygame.font.Font()	文件路径	Font("simhei.ttf", 48)
# pygame.font.SysFont()	字体名称	SysFont("SimHei", 48)