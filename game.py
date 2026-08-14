import random
import pygame
import config
import card
import battle
import player
import enemy
import ui


class Game:
    HAND_LIMIT = 10  # 手牌上限

    def __init__(self, screen):
        self.screen = screen
        self.player = player.Player("英雄", 70, 3)
        self.enemy = enemy.Enemy("哥布林", 50, [("攻击", 8), ("防御", 5), ("重击", 12)])
        self.draw_pile = card.create_starting_deck()
        random.shuffle(self.draw_pile)
        self.discard_pile = []
        self.hand = []
        self.selected_idx = -1
        self.state = "PLAYER_TURN"
        self.enemy.decide_intent()   # 战斗开始先展示敌人第一个意图
        self.start_player_turn()

    # ---------- 牌堆 ----------
    def draw_cards(self, n):
        for _ in range(n):
            if len(self.hand) >= self.HAND_LIMIT:
                return
            if not self.draw_pile:
                self.reshuffle_discard()
            if not self.draw_pile:
                return
            self.hand.append(self.draw_pile.pop())

    def reshuffle_discard(self):
        random.shuffle(self.discard_pile)
        self.draw_pile = self.discard_pile
        self.discard_pile = []

    # ---------- 回合流程 ----------
    def start_player_turn(self):
        """玩家回合开始：中毒结算 → 护盾清零 → 能量回满 → 抽 5 张"""
        battle.tick_turn_start(self.player)
        result = battle.check_battle_over(self.player, self.enemy)
        if result:
            self.state = result
            return
        self.player.block = 0
        self.player.energy = self.player.max_energy
        self.draw_cards(5)
        self.state = "PLAYER_TURN"

    def end_turn(self):
        """玩家主动结束回合：手牌进弃牌堆 → 能量清零 → 进入敌人回合"""
        if self.state != "PLAYER_TURN":
            return
        self.discard_pile.extend(self.hand)
        self.hand = []
        self.player.energy = 0
        battle.tick_turn_end(self.player)
        self.run_enemy_turn()

    def run_enemy_turn(self):
        """敌人回合：中毒结算 → 护盾清零 → 执行意图 → 结束结算 → 判定胜负 → 回到玩家回合"""
        battle.tick_turn_start(self.enemy)
        result = battle.check_battle_over(self.player, self.enemy)
        if result:
            self.state = result
            return
        self.enemy.block = 0
        action, value = self.enemy.intent
        if action in ("攻击", "重击"):
            battle.deal_damage(self.enemy, self.player, value)
        elif action == "防御":
            battle.gain_block(self.enemy, value)
        battle.tick_turn_end(self.enemy)

        result = battle.check_battle_over(self.player, self.enemy)
        if result:
            self.state = result
            return
        self.enemy.decide_intent()
        self.start_player_turn()

    def restart(self):
        self.__init__(self.screen)

    # ---------- 输入 ----------
    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.selected_idx = -1
        if self.state != "PLAYER_TURN":
            return
        for i in range(len(self.hand)):
            card_x = 100 + i * 170
            card_y = 500
            if card_x <= mouse_x <= card_x + 150 and card_y <= mouse_y <= card_y + 200:
                self.selected_idx = i
                break

    def handle_click(self, mouse_x, mouse_y):
        if self.state in ("victory", "defeat"):
            # 点击"重新开始"按钮
            if 700 <= mouse_x <= 900 and 520 <= mouse_y <= 570:
                self.restart()
            return
        if self.state != "PLAYER_TURN":
            return
        # 结束回合按钮
        if 1100 <= mouse_x <= 1230 and 650 <= mouse_y <= 700:
            self.end_turn()
            return
        # 打牌
        for i in range(len(self.hand)):
            card_x = 100 + i * 170
            card_y = 500
            if card_x <= mouse_x <= card_x + 150 and card_y <= mouse_y <= card_y + 200:
                c = self.hand[i]
                if self.player.energy >= c.cost:
                    c.play(self)
                    self.player.energy -= c.cost
                    self.discard_pile.append(c)
                    self.hand.pop(i)
                return

    # ---------- 渲染 ----------
    def render(self):
        self.screen.fill(config.BLACK)
        if self.state in ("victory", "defeat"):
            ui.draw_end_screen(self.screen, self.state)
            return
        for i, c in enumerate(self.hand):
            cx = 100 + i * 170
            cy = 500
            c.draw(self.screen, cx, cy, i == self.selected_idx)
        self.player.draw(self.screen, 50, 50)
        self.enemy.draw(self.screen, 900, 50)
        # 牌堆信息
        ui.draw_text(self.screen, f"抽牌堆: {len(self.draw_pile)}", 50, 200)
        ui.draw_text(self.screen, f"弃牌堆: {len(self.discard_pile)}", 50, 230)
        # 结束回合按钮
        pygame.draw.rect(self.screen, config.GOLD, (1100, 650, 130, 50), 3)
        ui.draw_text(self.screen, "结束回合", 1115, 662, color=config.GOLD)
