"""战斗逻辑：伤害结算、状态效果结算、胜负判定。

这里只做「机制」，buff 的具体数值和种类后续再逐项讨论设计。
"""


def get_stacks(entity, buff_type):
    """返回实体身上某种 buff 的总层数"""
    total = 0
    for buff in entity.status_effects:
        if buff.buff_type == buff_type:
            total += buff.stacks
    return total


def has_buff(entity, buff_type):
    return get_stacks(entity, buff_type) > 0


def deal_damage(attacker, defender, amount):
    """一次攻击结算。

    顺序：力量加成 → 虚弱减免 → 易伤增伤 → 护盾吸收 → 荆棘反弹
    返回实际造成的 HP 伤害。
    """
    amount += get_stacks(attacker, "strength")
    if has_buff(attacker, "weak"):
        amount = int(amount * 0.75)
    if has_buff(defender, "vulnerable"):
        amount = int(amount * 1.5)

    hp_before = defender.hp
    defender.take_damage(amount)
    dealt = hp_before - defender.hp

    # 荆棘反弹（受击方有荆棘时，反弹伤害给攻击方）
    thorns = get_stacks(defender, "thorns")
    if thorns > 0 and dealt > 0:
        attacker.take_damage(thorns)
    return dealt


def gain_block(target, amount):
    """获得护盾，受敏捷加成"""
    amount += get_stacks(target, "dexterity")
    target.block += amount


def tick_turn_start(entity):
    """回合开始结算：中毒扣血，随后层数 -1，归零的中毒移除"""
    poison = get_stacks(entity, "poison")
    if poison > 0:
        entity.hp -= poison
        for buff in entity.status_effects:
            if buff.buff_type == "poison":
                buff.stacks -= 1
        entity.status_effects = [
            buff for buff in entity.status_effects
            if not (buff.buff_type == "poison" and buff.stacks <= 0)
        ]


def tick_turn_end(entity):
    """回合结束结算：再生回血，并扣减限时 buff 的剩余回合"""
    regen = get_stacks(entity, "regen")
    if regen > 0:
        entity.hp = min(entity.max_hp, entity.hp + regen)

    for buff in entity.status_effects[:]:
        if buff.duration is not None:
            buff.duration -= 1
            if buff.duration <= 0:
                entity.status_effects.remove(buff)


def check_battle_over(player, enemy):
    """返回 "victory" / "defeat" / None"""
    if enemy.hp <= 0:
        return "victory"
    if player.hp <= 0:
        return "defeat"
    return None
