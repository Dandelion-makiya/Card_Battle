# 🎴 卡牌战斗游戏 — 学习进度

> **项目路径**：`e:\card battle`
> **教学规则**：见 `.clinerules`

---

## 课程总览（10 课）

| 课次 | 课程主题 | 状态 |
|------|---------|------|
| 第1课 | 🏗️ 项目架构设计 | ✅ 完成 |
| 第2课 | 🪟 Pygame 窗口 | ✅ 完成 |
| 第3课 | 🎨 绘制基础 | ✅ 完成 |
| 第4课 | 🃏 卡牌数据结构 | ✅ 完成 |
| 第5课 | ✨ Buff 系统设计 | ✅ 完成 |
| 第6课 | 🖱️ 手牌渲染与交互 | ✅ 完成 |
| 第7课 | 👥 实体类（Player + Enemy） | ✅ 完成 |
| 第8课 | ⚔️ 战斗逻辑 | ✅ 完成 |
| 第9课 | 🔄 回合制系统 | ✅ 完成 |
| 第10课 | 🏁 完整游戏整合 | ⬜ 待开始 |

---

## 已完成课程详情

### 第1课：项目架构设计 ✅
- 掌握模块拆分原则（单一职责）
- 理解各模块职责：`main.py` / `config.py` / `game.py` / `card.py` / `enemy.py` / `battle.py` / `ui.py`
- 新增 `player.py`，与 `enemy.py` 对称设计
- 「卡牌能否打出」的判断逻辑放在 `game.py`

### 第2课：Pygame 窗口 ✅
- `pygame.init()` → `set_mode()` → 主循环
- 事件处理：`pygame.event.get()` / `pygame.QUIT`
- 渲染流程：`screen.fill()` 清屏 → `pygame.display.flip()` 显示 → `clock.tick(60)` 锁帧
- 理解 `sys.exit()` 与 `__name__ == "__main__"`

### 第3课：绘制基础 ✅
- pygame 坐标系（左上角原点，Y 轴向下）
- 画矩形：`pygame.draw.rect(screen, color, (x, y, w, h))`
- 画文字三步：`SysFont` → `render` → `blit`
- 中文显示用 `pygame.font.SysFont("SimHei", 48)`
- 绘制顺序：先画底层再画上层（后画覆盖先画）
- fill/flip 顺序的实验验证

### 第4课：卡牌数据结构 ✅
- 采用**单一 `Card` 类**，不拆分子类（放弃继承方案）
- Card 的属性：`name`, `card_type`, `cost`, `value`, `target`, `description`, `buff_specs`, `buff_target`
- `buff_specs` 用规格 `(类型, 层数, 回合)` 描述状态效果，打出时才创建 buff 实例，避免共享污染
- 所有卡牌类型（attack/defense/skill）统一用 `card_type` 字段区分

### 第5课：Buff 系统设计 ✅
- `Buff` 类字段：`name`, `buff_type`, `stacks`（层数）, `duration`（剩余回合，None=本场战斗）
- 工厂函数 `create_xxx()` / `create_buff(spec)`，每次返回全新实例
- 已定义 7 种 buff 模板：中毒/虚弱/易伤/力量/敏捷/荆棘/再生（数值细节后续讨论）

### 第6课：手牌渲染与交互 ✅
- 卡牌 `draw()` 渲染名字、费用、数值、描述
- 鼠标悬停高亮（金色边框）
- 点击打牌：能量足够才可打出，打出后卡进弃牌堆

### 第7课：实体类（Player + Enemy） ✅
- `Player`：`hp` / `max_hp` / `block` / `energy` / `status_effects`
- `Enemy`：`hp` / `intent_pool` / `intent_index` / `intent` / `status_effects`
- 敌人意图按意图池**顺序循环**（`decide_intent`）

### 第8课：战斗逻辑 ✅
- `battle.deal_damage`：力量加成 → 虚弱减免 → 易伤增伤 → 护盾吸收 → 荆棘反弹
- `battle.gain_block`：护盾受敏捷加成
- `battle.tick_turn_start/end`：中毒扣血、再生回血、限时 buff 回合递减
- `battle.check_battle_over`：胜负判定

### 第9课：回合制系统 ✅
- 抽牌堆 / 弃牌堆 / 洗牌（初始牌组 斩击×5 防御×4 痛击×1）
- 完整回合流程：玩家回合 → 结束回合 → 敌人回合 → 新玩家回合（抽 5 张）
- 状态机：`PLAYER_TURN` / `VICTORY` / `DEFEAT`
- 胜负判定与结束画面（可重新开始）

---

## 当前进度：第9课 — 回合制系统 ✅

**已完成**：战斗核心循环已跑通（牌堆 → 打牌 → 敌人回合 → 胜负判定 → 重新开始）。

**后续待讨论设计**（按你要求先不写死）：
- Buff 的具体种类与数值（GDD 2.4）
- 正式卡池 18 张（GDD 2.5）
- 13 场敌人的意图模式（GDD 2.6）

---

## 项目文件结构

```
e:\card battle\
├── main.py            # 程序入口（pygame窗口 + 主循环）
├── config.py          # 常量配置（窗口尺寸、颜色）
├── game.py            # 游戏主控（状态管理、回合）
├── card.py            # 卡牌类 + 初始牌组
├── player.py          # 玩家类（HP、护盾、能量）
├── enemy.py           # 敌人类（HP、意图、AI）
├── battle.py          # 战斗逻辑（伤害/buff 结算、胜负判定）
├── buffs.py           # Buff 类定义 + 工厂函数
├── ui.py              # UI辅助函数
├── assets/            # 资源文件夹
├── .clinerules        # 教学对话规则
└── PROGRESS.md        # 本文件
```

---

## 教学规则摘要（来自 .clinerules）

1. 任一课程未明确「本课已掌握」前，不得推进到下一课
2. 不得揣测用户心理，有疑问必须先提问
3. 掌握确认方式：提问让用户回答，或让用户手写代码验证