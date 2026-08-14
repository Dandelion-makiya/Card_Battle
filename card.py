import buffs
import pygame
import config

class Card:
    """卡牌数据类"""
    def __init__(self, name, card_type, cost, value, target, description, buffs=None, buff_target=None):
        self.name = name
        self.card_type = card_type
        self.cost = cost
        self.value = value
        self.target = target
        self.description = description
        # self.buffs = buffs if buffs is not None else [] # AI别乱改我的代码，我不喜欢可读性差的代码
        if buffs is None:
            self.buffs = []
        else:
            self.buffs = buffs
        self.buff_target = buff_target if buff_target is not None else None



    def __str__(self):
        base = (f"Card(name={self.name}, type={self.card_type}, "
                f"cost={self.cost}, value={self.value}, "
                f"target={self.target}, description={self.description})")
        if self.buffs:
            base += f" [buffs={self.buffs}]"
        if self.buff_target:
            base += f" [buff_target={self.buff_target}]"
        return base

    def draw(self, screen, x, y, is_hovered=False):
        pygame.draw.rect(screen, config.BLACK, (x, y, 150, 200))
        border_color = config.GOLD if is_hovered else config.WHITE
        pygame.draw.rect(screen, border_color, (x, y, 150, 200), 3)
        font = pygame.font.SysFont("SimHei", 20)
        name_surface = font.render(self.name, True, config.WHITE)
        screen.blit(name_surface, (x + 10, y + 10))
        cost_text = font.render(str(self.cost), True, config.GOLD)
        screen.blit(cost_text, (x + 130, y + 10))


    def play(self, game):
        if self.card_type == "attack":
            game.enemy.take_damage(self.value)
        elif self.card_type == "defense":
            game.player.block += self.value

        if self.buffs:
            for buff in self.buffs:
                if self.buff_target == "player":
                    game.player.status_effects.append(buff)
                elif self.buff_target == "enemy":
                    game.enemy.status_effects.append(buff)




# 卡牌模板，后面可以放另外的文件里保管
uppercut = Card("上勾拳", "attack", 2, 12, "enemy1", 
                "造成 12 点伤害，施加 1 层虚弱 + 1 层易伤",
                 buffs=[buffs.WEAK, buffs.VULNERABLE], 
                 buff_target="enemy1")
slash = Card("斩击", "attack", 1, 6, "enemy", "造成 6 点伤害")
defend = Card("防御", "defense", 1, 5, "player", "获得 5 点护盾")
bash = Card("痛击", "attack", 2, 8, "enemy", "造成 8 点伤害，施加易伤",
             buffs=[buffs.VULNERABLE], 
             buff_target="enemy")
poison = Card("毒击", "attack", 2, 4, "enemy", "造成 4 点伤害，施加中毒")
smash = Card("重击", "attack", 3, 15, "enemy", "造成 15 点伤害")









# if __name__ == "__main__":
#     print(uppercut)


# if __name__ == "__main__":
#     strike = Card("斩击", "attack", 1, 6, "enemy1", "造成 6 点伤害")
#     defend = Card("防御", "defense", 1, 5, "player", "获得 5 点护盾")
#     bash = Card("痛击", "attack", 2, 8, "enemy2", "造成 8 点伤害，施加 2 层易伤", buffs=[buffs.VULNERABLE], buff_target="enemy2")

#     for card in [strike, defend, bash]:
#         print(card)
