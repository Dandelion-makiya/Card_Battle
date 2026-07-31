import pygame
import config


class Player:
    def __init__(self, name, hp, max_energy):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.block = 0 # 当前护盾值
        self.max_energy = max_energy
        self.energy = max_energy
        self.status_effects = [] # 存储状态效果

    def take_damage(self, amount):
        if self.block > 0:
            blocked = min(self.block, amount)  #blocked 返回小的那个，不会让block变成负数
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
        # 能量
        energy_text = font.render(f"能量: {self.energy}/{self.max_energy}", True, config.GOLD)
        screen.blit(energy_text, (x, y + 80))
    