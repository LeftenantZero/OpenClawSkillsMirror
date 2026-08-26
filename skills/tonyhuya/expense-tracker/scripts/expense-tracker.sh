#!/usr/bin/env bash
# expense-tracker: 本地记账助手（数据存在 ~/.expense-tracker/ledger.tsv）
# 用法:
#   expense-tracker add 25.5 午饭
#   expense-tracker add -30 退押金        # 负数=收入
#   expense-tracker list                  # 查看最近20条
#   expense-tracker list 2026-08          # 查看某月
#   expense-tracker today                # 今日汇总
#   expense-tracker month                # 本月汇总
#   expense-tracker summary              # 本月分类统计
#   expense-tracker delete 3             # 删除第3条
set -euo pipefail

DATA_DIR="${EXPENSE_DATA_DIR:-$HOME/.expense-tracker}"
LEDGER="$DATA_DIR/ledger.tsv"
mkdir -p "$DATA_DIR"
[ -f "$LEDGER" ] || touch "$LEDGER"

show_help() { sed -n '2,12p' "$0" | sed 's/^# \{0,1\}//'; }

case "${1:-}" in
  add)
    [ $# -lt 3 ] && { echo "用法: expense-tracker add <金额> <备注>" >&2; exit 1; }
    AMT="$2"; shift 2
    NOTE="$*"
    [[ "$AMT" =~ ^-?[0-9]+(\.[0-9]+)?$ ]] || { echo "金额格式不对: $AMT" >&2; exit 1; }
    DATE=$(date +%Y-%m-%d)
    TIME=$(date +%H:%M)
    echo -e "$DATE\t$TIME\t$AMT\t$NOTE" >> "$LEDGER"
    if [[ "$AMT" =~ ^- ]]; then
      echo "💰 已记录收入: ${AMT#-} 元（$NOTE）"
    else
      echo "💸 已记录支出: $AMT 元（$NOTE）"
    fi
    ;;
  list)
    LIMIT=20
    if [ $# -ge 2 ]; then
      case "$2" in
        *-*) grep "^$2" "$LEDGER" | tail -n 50 ;;
        *) LIMIT="$2"; tail -n "$LIMIT" "$LEDGER" ;;
      esac
    else
      tail -n "$LIMIT" "$LEDGER"
    fi | python3 -c "
import sys
rows=[]
for line in sys.stdin:
    p=line.rstrip('\n').split('\t')
    if len(p)>=4: rows.append(p)
if not rows:
    print('📭 暂无记录，试试: expense-tracker add 25.5 午饭')
else:
    print(f'📒 最近 {len(rows)} 条记录：')
    for i,(d,t,a,n) in enumerate(rows):
        sign='+' if a.startswith('-') else '-'
        amt=abs(float(a))
        print(f'  {d} {t}  {sign}{amt:.2f}  {n}')
" ;;
  today)
    TODAY=$(date +%Y-%m-%d)
    grep "^$TODAY" "$LEDGER" | python3 -c "
import sys
rows=[l.rstrip().split('\t') for l in sys.stdin if l.strip()]
inc=sum(float(r[2]) for r in rows if r[2].startswith('-'))
exp=sum(float(r[2]) for r in rows if not r[2].startswith('-'))
net = abs(inc) - exp
sign = '+' if net >= 0 else '-'
print(f'📅 今日（{len(rows)}笔）：支出 {exp:.2f} 元，收入 {abs(inc):.2f} 元，净 {sign}{abs(net):.2f} 元')
" ;;
  month)
    MONTH=$(date +%Y-%m)
    grep "^$MONTH" "$LEDGER" | python3 -c "
import sys
rows=[l.rstrip().split('\t') for l in sys.stdin if l.strip()]
inc=sum(float(r[2]) for r in rows if r[2].startswith('-'))
exp=sum(float(r[2]) for r in rows if not r[2].startswith('-'))
net = abs(inc) - exp
sign = '+' if net >= 0 else '-'
print(f'📊 本月（$MONTH，{len(rows)}笔）：支出 {exp:.2f} 元，收入 {abs(inc):.2f} 元，净 {sign}{abs(net):.2f} 元')
" ;;
  summary)
    MONTH=$(date +%Y-%m)
    grep "^$MONTH" "$LEDGER" | python3 -c "
import sys
from collections import defaultdict
cats=defaultdict(float)
for l in sys.stdin:
    p=l.rstrip().split('\t')
    if len(p)<4 or p[2].startswith('-'): continue
    cats[p[3]] += float(p[2])
if not cats:
    print('📭 本月暂无支出记录')
else:
    print(f'📊 $MONTH 支出分类统计：')
    for k,v in sorted(cats.items(), key=lambda x:-x[1]):
        print(f'  {k}: {v:.2f} 元')
    print(f'  合计: {sum(cats.values()):.2f} 元')
" ;;
  delete)
    [ $# -lt 2 ] && { echo "用法: expense-tracker delete <行号>" >&2; exit 1; }
    N="$2"
    TOTAL=$(wc -l < "$LEDGER")
    [ "$N" -le "$TOTAL" ] || { echo "没有第 $N 条（共 $TOTAL 条）" >&2; exit 1; }
    sed -i "${N}d" "$LEDGER"
    echo "🗑️ 已删除第 $N 条记录"
    ;;
  --help|-h|"")
    show_help
    ;;
  *)
    echo "未知命令: $1（试试 add / list / today / month / summary / delete）" >&2
    exit 1
    ;;
esac
