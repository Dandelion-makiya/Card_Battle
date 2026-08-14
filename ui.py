"""UI 辅助函数：文字绘制、结束画面"""
import pygame
import config


def draw_text(screen, text, x, y, size=20, color=config.WHITE):
    font = pygame.font.SysFont("SimHei", size)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def draw_end_screen(screen, state):
    """战斗结束画面"""
    if state == "victory":
        title = "胜利！"
        color = config.GOLD
    else:
        title = "失败……"
        color = config.RED
    draw_text(screen, title, 700, 350, size=72, color=color)

    # 重新开始按钮
    pygame.draw.rect(screen, config.WHITE, (700, 520, 200, 50), 3)
    draw_text(screen, "重新开始", 755, 532, size=24)
