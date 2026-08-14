import pygame
import config
import card
import player
import enemy


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.hand = []
        self.selected_idx = -1
        self.is_player_turn = True
        self.create_hand()
        self.player = player.Player("英雄", 70, 3)
        self.enemy = enemy.Enemy("哥布林", 50, [("攻击", 8), ("防御", 5), ("重击", 12)])
        self.enemy.decide_intent()

    def create_hand(self):
        self.hand = [card.uppercut, card.slash, card.defend, card.bash, card.poison, card.smash]

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.selected_idx = -1
        for i in range(len(self.hand)):
            card_x = 100 + i * 170
            card_y = 500
            if (card_x <= mouse_x <= card_x + 150) and (card_y <= mouse_y <= card_y + 200):
                self.selected_idx = i
                break

    def render(self):
        self.screen.fill(config.BLACK)
        for i, card in enumerate(self.hand):
            cx = 100 + i * 170
            cy = 500
            is_hovered = (i == self.selected_idx)
            card.draw(self.screen, cx, cy, is_hovered)
        self.player.draw(self.screen, 50, 50)
        self.enemy.draw(self.screen, 900, 50)
        pygame.draw.rect(self.screen, config.GOLD, (1100, 650, 130, 50), 3)
        font = pygame.font.SysFont("SimHei", 20)
        text = font.render("结束回合", True, config.GOLD)
        self.screen.blit(text, (1115, 660))

    def handle_click(self, mouse_x, mouse_y):
        if 1100 <= mouse_x <= 1230 and 650 <= mouse_y <= 700:
            self.end_turn()
            return
        for i in range(len(self.hand)):
            card_x = 100 + i * 170
            card_y = 500
            if (card_x <= mouse_x <= card_x + 150) and (card_y <= mouse_y <= card_y + 200):
                c = self.hand[i]
                if self.player.energy >= c.cost:
                    c.play(self)
                    self.player.energy -= c.cost
                    self.hand.pop(i)
                return

    def end_turn(self):
        self.is_player_turn = False
        self.enemy.decide_intent()
        action, value = self.enemy.intent
        if action == "攻击":
            self.player.take_damage(value)
        elif action == "防御":
            self.enemy.block += value
        self.is_player_turn = True
        self.player.energy = self.player.max_energy
        self.player.block = 0
        self.enemy.block = 0
