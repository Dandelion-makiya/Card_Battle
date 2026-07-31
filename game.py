import pygame
import config
import card
import player
import enemy


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.hand = []
        self.selected_idx = -1 # 选中的卡牌索引 
        # -1 == 没选中任何卡牌
        self.selected_card = -1 
        self.create_hand()
        # 初始化敌方和玩家 ，测试代码，后面还是用模块化
        self.player = player.Player("英雄", 70, 3)              # ← 加这行
        self.enemy = enemy.Enemy("哥布林", 50,                   # ← 加这行
                       [("攻击", 8), ("防御", 5), ("重击", 12)])

    def create_hand(self):
        self.hand = [card.uppercut, card.slash, 
                     card.defend, card.bash, 
                     card.poison, card.smash]

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.selected_idx = -1 # 索引

        for i in range(len(self.hand)):
            card_x = 100 + i * 170
            card_y = 500
            if (card_x <= mouse_x <= card_x + 150) and (card_y <= mouse_y <= card_y + 200):
                self.selected_idx = i  # 记录：鼠标悬停在第 i 张卡上
                break

    def render(self):
        self.screen.fill(config.BLACK)
        for i, card in enumerate(self.hand):
            cx = 100 + i * 170 
            cy = 500
            is_hovered = (i == self.selected_idx)
            card.draw(self.screen, cx, cy, is_hovered)
        self.player.draw(self.screen, 50, 50)      # ← 加这行（左上角）
        self.enemy.draw(self.screen, 900, 50)      # ← 加这行（右上角）
        