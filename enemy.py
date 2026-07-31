import random
import pygame
import config

class Enemy:
    def __init__(self, name, hp, intent_pool):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.intent_pool = intent_pool
        self.block = 0
        self.status_effects = []
        self.intent = None

    def decide_intent(self):
        self.intent = random.choice(self.intent_pool)

    def take_damage(self, amount):
        if self.block > 0:
            blocked = min(self.block, amount)
            self.block -= blocked
            amount -= blocked
        self.hp -= amount

    def draw(self, screen, x, y):
        font = pygame.font.SysFont('SimHei', 20)
        name_text = font.render(self.name, True, config.WHITE)
        screen.blit(name_text, (x, y))
        hp_text = font.render(f'HP: {self.hp}/{self.max_hp}', True, config.RED)
        screen.blit(hp_text, (x, y + 30))
        if self.block > 0:
            block_text = font.render(f'\u62a4\u76fe: {self.block}', True, config.BLUE)
            screen.blit(block_text, (x, y + 55))
        if self.intent:
            action, value = self.intent
            intent_text = font.render(f'\u610f\u56fe: {action} {value}', True, config.GOLD)
            screen.blit(intent_text, (x, y + 80))
