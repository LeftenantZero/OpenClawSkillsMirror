---
name: expense-tracker
description: "本地记账助手，纯命令行无外部依赖。记录收支、按日/月汇总、分类统计，数据存在本地 TSV 文件，完全隐私。"
homepage: ""
metadata:
  {
    "openclaw":
      {
        "emoji": "💰",
        "install":
          [
            {
              "id": "python3",
              "kind": "apt",
              "formula": "python3",
              "bins": ["python3"],
              "label": "Install python3",
            },
          ],
      },
  }
---

# expense-tracker.sh 本地记账助手

极简本地记账工具，**零外部依赖、零网络请求**，数据存在本地
`~/.expense-tracker.sh/ledger.tsv`，完全隐私可控。

## 用法

```bash
expense-tracker.sh add 25.5 午饭      # 记一笔支出
expense-tracker.sh add -5000 发工资   # 负数 = 收入
expense-tracker.sh list               # 最近20条
expense-tracker.sh list 2026-08       # 某月记录
expense-tracker.sh today              # 今日汇总
expense-tracker.sh month              # 本月汇总
expense-tracker.sh summary            # 本月支出分类统计
expense-tracker.sh delete 3           # 删除第3条
```

## 特点

- 💸 支出记正数，💰 收入记负数（如 `add -5000 工资`）
- 📊 `summary` 按备注自动分类统计本月支出
- 🔒 数据纯本地存储（TSV），不联网、不上传
- ⚙️ 可用环境变量 `EXPENSE_DATA_DIR` 自定义数据目录（默认 `~/.expense-tracker.sh`）

## 适用场景

- 个人日常记账
- 家庭月度开销统计
- 预算管理（配合提醒技能使用）
