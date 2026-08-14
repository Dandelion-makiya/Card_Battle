class Buff:
    """状态效果。

    stacks：层数（中毒=每回合伤害值，力量/敏捷=加成值，其余默认为 1）
    duration：剩余回合数；None 表示持续到战斗结束（或靠层数自然归零）
    """
    def __init__(self, name, buff_type, stacks=1, duration=None, description=""):
        self.name = name
        self.buff_type = buff_type
        self.stacks = stacks
        self.duration = duration
        self.description = description

    def __str__(self):
        return (f"Buff(name={self.name}, type={self.buff_type}, "
                f"stacks={self.stacks}, duration={self.duration})")

    def __repr__(self):
        return self.__str__()


# ---------- 工厂函数：每次调用都返回全新实例，避免多个目标共享同一个 buff ----------

def create_poison(stacks):
    return Buff("中毒", "poison", stacks=stacks, duration=None,
                description="每回合开始受到 X 点伤害，随后层数 -1")


def create_weak(duration=2):
    return Buff("虚弱", "weak", stacks=1, duration=duration,
                description="造成的伤害 × 0.75（向下取整）")


def create_vulnerable(duration=2):
    return Buff("易伤", "vulnerable", stacks=1, duration=duration,
                description="受到的伤害 × 1.5（向下取整）")


def create_strength(stacks):
    return Buff("力量", "strength", stacks=stacks, duration=None,
                description=f"攻击伤害 +{stacks}")


def create_dexterity(stacks):
    return Buff("敏捷", "dexterity", stacks=stacks, duration=None,
                description=f"获得护盾 +{stacks}")


def create_thorns(stacks, duration=2):
    return Buff("荆棘", "thorns", stacks=stacks, duration=duration,
                description=f"受到攻击时反弹 {stacks} 点伤害")


def create_regen(stacks):
    return Buff("再生", "regen", stacks=stacks, duration=stacks,
                description=f"每回合结束回复 {stacks} 点 HP")


def create_buff(spec):
    """根据规格 (类型, 层数, 持续回合) 创建对应的 buff 实例"""
    buff_type, stacks, duration = spec
    if buff_type == "poison":
        return create_poison(stacks)
    if buff_type == "weak":
        return create_weak(duration)
    if buff_type == "vulnerable":
        return create_vulnerable(duration)
    if buff_type == "strength":
        return create_strength(stacks)
    if buff_type == "dexterity":
        return create_dexterity(stacks)
    if buff_type == "thorns":
        return create_thorns(stacks, duration)
    if buff_type == "regen":
        return create_regen(stacks)
    raise ValueError(f"未知的 buff 类型: {buff_type}")
