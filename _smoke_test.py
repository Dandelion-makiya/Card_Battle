"""临时冒烟测试：无界面验证战斗循环与 buff 结算（跑完即删）"""
import game
import battle
import buffs


def test_buffs():
    import player as player_mod
    import enemy as enemy_mod

    def fresh():
        return player_mod.Player("测试", 70, 3), enemy_mod.Enemy("木桩", 100, [("攻击", 0)])

    print("=== buff 结算验证 ===")

    p, e = fresh()
    e.status_effects.append(buffs.create_vulnerable(2))
    battle.deal_damage(p, e, 6)
    assert e.hp == 91, f"易伤: 期望 9 伤害, 实际 {100 - e.hp}"
    print("易伤: 6 伤害 -> 9 ✓")

    p, e = fresh()
    p.status_effects.append(buffs.create_weak(2))
    battle.deal_damage(p, e, 6)
    assert e.hp == 96, f"虚弱: 期望 4 伤害, 实际 {100 - e.hp}"
    print("虚弱: 6 伤害 -> 4 ✓")

    p, e = fresh()
    e.block = 3
    battle.deal_damage(p, e, 6)
    assert e.hp == 97 and e.block == 0, "护盾吸收异常"
    print("护盾: 6 伤害 - 3 护盾 = 3 掉血 ✓")

    p, e = fresh()
    e.status_effects.append(buffs.create_poison(3))
    battle.tick_turn_start(e)
    assert e.hp == 97, "中毒结算异常"
    print("中毒: 3 层 -> 扣 3 血 ✓")

    p, e = fresh()
    p.status_effects.append(buffs.create_strength(2))
    battle.deal_damage(p, e, 6)
    assert e.hp == 92, f"力量: 期望 8 伤害, 实际 {100 - e.hp}"
    print("力量: 6 + 2 = 8 伤害 ✓")


def main():
    g = game.Game(None)

    print("\n=== 初始状态 ===")
    print(f"手牌: {len(g.hand)}  抽牌堆: {len(g.draw_pile)}  弃牌堆: {len(g.discard_pile)}")
    assert len(g.hand) == 5 and len(g.draw_pile) == 5, "初始抽牌异常"

    print("\n=== 玩家回合打牌 ===")
    for c in list(g.hand):
        if c.card_type == "attack" and g.player.energy >= c.cost:
            before = g.enemy.hp
            c.play(g)
            g.player.energy -= c.cost
            g.discard_pile.append(c)
            g.hand.remove(c)
            print(f"打出 {c.name}，敌人HP {before} -> {g.enemy.hp}")

    print("\n=== 结束回合（敌人回合）===")
    before_hp = g.player.hp
    g.end_turn()
    print(f"玩家HP {before_hp} -> {g.player.hp}，state={g.state}")
    print(f"新回合 手牌: {len(g.hand)}  抽牌堆: {len(g.draw_pile)}  弃牌堆: {len(g.discard_pile)}")
    print(f"玩家能量: {g.player.energy}")

    print("\n=== 自动战斗到结束 ===")
    rounds = 0
    while g.state == "PLAYER_TURN" and rounds < 100:
        rounds += 1
        for c in list(g.hand):
            if g.state != "PLAYER_TURN":
                break
            if c.card_type == "attack" and g.player.energy >= c.cost:
                c.play(g)
                g.player.energy -= c.cost
                g.discard_pile.append(c)
                g.hand.remove(c)
        if g.state == "PLAYER_TURN":
            g.end_turn()
        print(f"回合{rounds}: 玩家HP={g.player.hp} 敌人HP={g.enemy.hp} state={g.state}")

    assert g.state in ("victory", "defeat"), "战斗应能分出胜负"
    print(f"\n最终结果: {g.state}（玩家HP={g.player.hp} 敌人HP={g.enemy.hp}）")


if __name__ == "__main__":
    test_buffs()
    main()
    print("\n冒烟测试通过 ✓")
