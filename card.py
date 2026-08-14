import pygame
import config
import buffs
import battle


class Card:
    """卡牌数据类。

    buff_specs：打出后要施加的状态效果规格列表，
                每个元素是 (buff类型, 层数, 持续回合)，
                例如 ("vulnerable", 1, 2) 表示施加 2 回合易伤。
    """
    def __init__(self, name, card_type, cost, value, target, description,
                 buff_specs=None, buff_target=None):
        self.name = name
        self.card_type = card_type
        self.cost = cost
        self.value = value
        self.target = target
        self.description = description
        if buff_specs is None:
            self.buff_specs = []
        else:
            self.buff_specs = buff_specs
        if buff_target is None:
            self.buff_target = None
        else:
            self.buff_target = buff_target

    def __str__(self):
        base = (f"Card(name={self.name}, type={self.card_type}, "
                f"cost={self.cost}, value={self.value}, "
                f"target={self.target}, description={self.description})")
        if self.buff_specs:
            base += f" [buffs={self.buff_specs}]"
        if self.buff_target:
            base += f" [buff_target={self.buff_target}]"
        return base

    def draw(self, screen, x, y, is_hovered=False):
        pygame.draw.rect(screen, config.BLACK, (x, y, 150, 200))
        border_color = config.GOLD if is_hovered else config.WHITE
        pygame.draw.rect(screen, border_color, (x, y, 150, 200), 3)
        font = pygame.font.SysFont("SimHei", 20)
        small_font = pygame.font.SysFont("SimHei", 16)
        # 名字
        name_surface = font.render(self.name, True, config.WHITE)
        screen.blit(name_surface, (x + 10, y + 10))
        # 费用
        cost_text = font.render(str(self.cost), True, config.GOLD)
        screen.blit(cost_text, (x + 130, y + 10))
        # 数值
        if self.card_type == "attack":
            value_text = f"伤害 {self.value}"
        elif self.card_type == "defense":
            value_text = f"护盾 {self.value}"
        else:
            value_text = str(self.value)
        value_surface = font.render(value_text, True, config.RED)
        screen.blit(value_surface, (x + 10, y + 50))
        # 描述（按逗号拆成多行）
        lines = self.description.split("，")
        for j, line in enumerate(lines):
            line_surface = small_font.render(line, True, config.WHITE)
            screen.blit(line_surface, (x + 10, y + 100 + j * 22))

    def play(self, game):
        """打出卡牌：结算数值效果，并给目标施加附带的状态效果"""
        if self.card_type == "attack":
            battle.deal_damage(game.player, game.enemy, self.value)
        elif self.card_type == "defense":
            battle.gain_block(game.player, self.value)

        if self.buff_specs:
            if self.buff_target == "player":
                target = game.player
            else:
                target = game.enemy
            for spec in self.buff_specs:
                target.status_effects.append(buffs.create_buff(spec))


def create_starting_deck():
    """GDD 2.2 初始牌组：斩击×5、防御×4、痛击×1，共 10 张"""
    deck = []
    for _ in range(5):
        deck.append(Card("斩击", "attack", 1, 6, "enemy", "造成 6 点伤害"))
    for _ in range(4):
        deck.append(Card("防御", "defense", 1, 5, "player", "获得 5 点护盾"))
    deck.append(Card("痛击", "attack", 2, 8, "enemy",
                     "造成 8 点伤害，施加 2 回合易伤",
                     buff_specs=[("vulnerable", 1, 2)],
                     buff_target="enemy"))
    return deck




# 卡牌模板与正式卡池后续按 GDD 2.5 逐项讨论设计
