import random
import pygame

class Enemy:
    def __init__(self, name, hp, intent_pool):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.intent_pool = intent_pool
        self.block = 0 # 当前护盾值
        self.status_effects = [] # 存储状态效果
        self.intent = None

    def decide_intent(self):
        """AI 选择本回合行动（简单版：随机挑一个）"""
        self.intent = random.choice(self.intent_pool)
    
    def take_damage(self, amount):
        """受到伤害，先扣护盾"""
        if self.block > 0:
            blocked = min(self.block, amount)
            self.block -= blocked
            amount -= blocked
        self.hp -= amount 
    def draw(self, screen, x, y):
        font = pygame.font.SysFont("SimHei", 20)
        # 名字
        name_text = font.render(self.name, True, config.WHITE)
        screen.blit(name_text, (x, y))
        # HP
        hp_text = font.render(f"HP: {self.hp}/{self.max_hp}", True, config.RED)
        screen.blit(hp_text, (x, y + 30))
        # 护盾
        if self.block > 0:
            block_text = font.render(f"护盾: {self.block}", True, config.BLUE)
            screen.blit(block_text, (x, y + 55))
        # 意图
        if self.intent:
            action, value = self.intent
            intent_text = font.render(f"意图: {action} {value}", True, config.GOLD)
            screen.blit(intent_text, (x, y + 80))

