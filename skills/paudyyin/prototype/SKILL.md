---
name: prototype
version: 2.1.0
description: "Build one-shot prototypes to validate design decisions �� logic prototypes (state machines/algori..."
tags: [coding, frontend, visual, template-based, multi-agent]
metadata:
  author: yindb2 (adapted from community skill)
  category: coding
  triggers:
    - 原型
    - prototype
    - demo
    - 验证想法
    - 快速原�?    - UI探索
    - 状态机验证
    - 设计选项
  dependencies:
    - coding-framework (>=10.0.0) �?决策阶梯、安全守�?  integration:
    - daily-agent 调度入口，匹�?原型/demo/验证"类任�?    - coding-framework 模式1（快速编码）配合使用，先原型后正式实�?    - code-review-visualizer (>=1.0.0) �?UI 原型进行可视化审�?---

# Prototype �?快速原型验�?
原型�?*回答问题的可丢弃代码**。问题决定形态�?
---

## 核心定义

原型不是MVP、不是PoC、不是sprint deliverable。原型只有一个目的：**回答一个具体的设计问题**，回答完就可以丢弃�?
---

## 第一步：识别问题类型

从用户的描述、周围代码、或直接询问来确定：

### 逻辑分支
**问题**�?这个逻辑/状态模型感觉对吗？"
**形�?*：小型交互式终端应用，推动状态机走过难以在纸上推理的情况�?**特征**�?- 关注状态转换、边界条件、异常路�?- 输出是终端打印的状态变�?- 不需要视觉呈�?
### UI分支
**问题**�?这应该长什么样�?
**形�?*：生成几个截然不同的UI变体，通过URL参数+浮动底栏切换�?**特征**�?- 关注布局、交互、视觉层�?- 输出是浏览器中可操作的界�?- 需要视觉对�?
### 如何判断
- 周围是后端模�?�?逻辑分支
- 周围是页�?组件 �?UI分支
-  genuinely模糊且用户联系不�?�?根据上下文选更匹配的，在原型顶部声明假�?
**两个分支产出完全不同的artifact——搞错了浪费整个原型�?*

---

## 通用规则

### 规则1：从第一天起就是可丢弃的，且明确标记

- 原型代码放在它要验证的模�?页面附近（上下文清晰�?- 但命名让随意读者能看出这是原型，不是生产代�?- 命名约定：`prototype-XX`、`spike-XX`、`explore-XX`

### 规则2：一条命令运�?
- 用项目已有的task runner：`pnpm <name>`、`python <path>`、`bun <path>`
- 用户必须能不经思考就启动�?- 如果有依赖安装，写在README或注释里

### 规则3：默认无持久�?
- 状态存在内存中
- 持久化是原型�?*检查的东西**，不是它应该依赖的东�?- 如果问题明确涉及数据库，用scratch DB或本地文件，命名清楚"PROTOTYPE �?可删�?

### 规则4：跳过打�?
- 不写测试
- 不写错误处理（除了让原型能运行的最小量�?- 不做抽象
- 目标是快速学到东西然后删�?
### 规则5：暴露状�?
- **逻辑原型**：每次操作后，打�?渲染所有相关状�?- **UI原型**：每次变体切换时，显示完整状�?- 让用户看到什么变�?
### 规则6：完成后删除或吸�?
- 原型回答了问题后：删除它，或将验证过的决策合并到真实代码
- 不要让它烂在仓库�?
---

## 逻辑原型指南

### 适用场景
- 状态机设计验证
- 算法行为探索
- 并发/竞态条件演�?- 数据�?管道验证

### 构建模板
```python
# prototype-state-machine.py
"""
原型：验证XX状态机设计
问题：在A/B/C情况下状态转换是否正确？
运行：python prototype-state-machine.py
"""

class StateMachine:
    def __init__(self):
        self.state = "initial"
    
    def handle(self, event):
        old_state = self.state
        # ... 状态转换逻辑 ...
        print(f"  {old_state} --[{event}]--> {self.state}")

def run_scenario(name, events):
    print(f"\n=== 场景: {name} ===")
    sm = StateMachine()
    for event in events:
        sm.handle(event)
    print(f"  最终状�? {sm.state}")

# 测试难以推理的场�?run_scenario("正常流程", ["start", "process", "complete"])
run_scenario("中途取�?, ["start", "process", "cancel"])
run_scenario("异常恢复", ["start", "error", "retry", "complete"])
```

### 验证要点
- [ ] 覆盖了所有状态转换路�?- [ ] 测试了边界条件（空输入、重复事件、非法转换）
- [ ] 状态变化清晰可�?- [ ] 能回�?这个逻辑对吗�?

---

## UI原型指南

### 适用场景
- 布局方案对比
- 交互模式探索
- 组件设计验证
- 响应式方案对�?
### 构建模板
```html
<!-- prototype-ui-variants.html -->
<!--
  原型：验证XX页面的UI方案
  问题：方案A/B/C哪个更好�?  运行：浏览器直接打开
  切换：URL�??variant=a / ?variant=b / ?variant=c
-->
<!DOCTYPE html>
<html>
<head>
  <style>
    /* 每个variant独立的样�?*/
  </style>
</head>
<body>
  <div id="variant-switcher">
    <!-- 浮动底栏切换变体 -->
  </div>
  <div id="variant-a"><!-- 方案A --></div>
  <div id="variant-b" style="display:none"><!-- 方案B --></div>
  <div id="variant-c" style="display:none"><!-- 方案C --></div>
</body>
</html>
```

### 验证要点
- [ ] 至少2-3个截然不同的方案
- [ ] 方案间可快速切换对�?- [ ] 使用真实数据（非lorem ipsum�?- [ ] 能回�?这应该长什么样�?

---

## 完成后：捕获答案

**答案**是原型唯一值得保留的东西�?
### 捕获方式
1. **Commit message** �?如果决策直接合并到代�?2. **ADR（Architecture Decision Record�?* �?如果是有意义的架构决�?3. **Issue** �?如果需要后续跟�?4. **NOTES.md** �?放在原型旁边，记录问题和结论

### 捕获内容
```markdown
# 原型结论

**问题**：XX状态机在并发事件下是否安全�?**答案**：不安全。发现race condition：事件A和B同时到达时，状态可能跳到非法值�?**决策**：引入事件队列，串行化处理�?**日期**�?026-06-20
**原型文件**：prototype-state-machine.py（可删除�?```

---

## 快速验证流�?
### 验证决策�?
```
用户提出设计问题
    �?    ├─ 问题明确 + 可回�?�?选择原型类型
    �?  ├─ 逻辑问题 �?逻辑原型（终端应用）
    �?  └─ 视觉问题 �?UI原型（HTML页面�?    �?    ├─ 问题模糊 �?先澄�?    �?  └─ 问用户："你想验证的是什么？"
    �?      ├─ "逻辑对不�? �?逻辑原型
    �?      └─ "长什么样�? �?UI原型
    �?    └─ 问题不需要原�?�?跳过
        ├─ 已有明确答案 �?直接说明
        └─ 可通过阅读代码回答 �?直接读代�?```

### 时间盒约�?
| 原型类型 | 最大时�?| 说明 |
|----------|----------|------|
| 逻辑原型 | 30 分钟 | 超过说明问题太大，需要拆�?|
| UI原型�?-3变体�?| 45 分钟 | 超过说明变体太多，缩减到2�?|
| 集成验证原型 | 60 分钟 | 涉及外部服务集成的复杂原�?|

### 原型质量检�?
完成原型后，回答以下问题�?- [ ] 原型回答了最初的问题吗？
- [ ] 结论有明确证据支撑吗�?- [ ] 答案可以转化为生产代码决策吗�?- [ ] 原型可以安全删除吗？

---

## 错误处理与降级策�?
### 原型构建失败

| 场景 | 降级方案 |
|------|----------|
| 逻辑原型依赖外部服务 | �?mock 数据替代真实服务 |
| UI原型无法在终端呈�?| 生成静�?HTML 文件，用浏览器打开 |
| 原型代码无法运行 | 降级为伪代码 + 状态表，手动推�?|
| 时间盒用�?| 停止构建，记录已有发现，标注未验证部�?|

### 原型结论不明�?
| 场景 | 降级方案 |
|------|----------|
| 多个变体难以区分 | 列出各变体优劣，让用户做最终选择 |
| 原型暴露新问�?| 记录新问题，评估是否需要第二轮原型 |
| 结论与预期矛�?| 信任原型结果，调整设计方�?|

---

## �?coding-framework 集成

### 调度入口

prototype 作为 daily-agent 的独立子技能，当任务分类为"原型/demo/验证想法"时自动加载�?
### 与决策阶梯配�?
原型构建前，先过 coding-framework �?Ponytail 决策阶梯�?1. 这个问题需要原型来回答吗？（L1: 需要存在吗？）
2. 代码库已有类似原型？（L2: 代码库已有？�?3. 能否用更简单方式回答？（L3-L5�?4. 确认需要原型后，快速构�?
### 原型到生产的过渡

```
原型验证通过
  �?coding-framework 模式1（快速编码）�?正式实现
  �?coding-framework 模式2（代理审查）�?代码审查
```

### �?code-review-visualizer 配合

UI原型完成后，使用 code-review-visualizer 生成可视化对比页面，方便团队评审�?
---

## 相关参�?
- `references/prototype-patterns.md` �?原型设计模式
- `references/rapid-validation.md` �?快速验证方�?
---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.1.0 | 2026-06-29 | 增加快速验证流程、错误处理与降级策略、coding-framework 集成 |
| v2.0.0 | 2026-06-20 | 从mp-prototype重组织，补充references和模板，适配daily-agent v2.0 |
| v1.0.0 | 社区版本 | 原型构建原始规则 |
