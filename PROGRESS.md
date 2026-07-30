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
| 第4课 | 🃏 卡牌数据结构 | 🔄 进行中 |
| 第5课 | ✨ Buff 系统设计 | ⬜ 待开始 |
| 第6课 | 🖱️ 手牌渲染与交互 | ⬜ 待开始 |
| 第7课 | 👥 实体类（Player + Enemy） | ⬜ 待开始 |
| 第8课 | ⚔️ 战斗逻辑 | ⬜ 待开始 |
| 第9课 | 🔄 回合制系统 | ⬜ 待开始 |
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

---

## 当前进度：第4课 — 卡牌数据结构 🔄

**设计决策**：
- 采用**单一 `Card` 类**，不拆分子类（放弃继承方案）
- Card 的属性：`name`, `card_type`, `cost`, `value`, `target`, `description`, `buff`, `buff_target`
- `buff` 存储 buff 对象引用，`buff_target` 指定 buff 作用目标
- 所有卡牌类型（attack/defense/skill）统一用 `card_type` 字段区分

**当前状态**：Card 类基础版已跑通，buff 字段待添加。

---

## 项目文件结构

```
e:\card battle\
├── main.py            # 程序入口（pygame窗口 + 主循环）
├── config.py          # 常量配置（窗口尺寸、颜色）
├── game.py            # 游戏主控（状态管理、回合）
├── card.py            # 卡牌类体系（Card + 子类）
├── player.py          # 玩家类（HP、护盾、能量）
├── enemy.py           # 敌人类（HP、意图、AI）
├── battle.py          # 战斗逻辑（伤害结算）
├── buff.py            # Buff 类定义 + 标准 Buff 模板
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