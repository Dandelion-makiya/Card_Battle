import pygame
import config
import card


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.hand = []
        # -1 == 没选中任何卡牌
        self.selected_card = -1 
        self.create_hand()

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