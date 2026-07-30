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


if __name__ == "__main__":
    strike = Card("斩击", "attack", 1, 6, "enemy1", "造成 6 点伤害")
    defend = Card("防御", "defense", 1, 5, "player", "获得 5 点护盾")
    bash = Card("痛击", "attack", 2, 8, "enemy2", "造成 8 点伤害，施加 2 层易伤","易伤", "enemy2")

    for card in [strike, defend, bash]:
        print(card)
