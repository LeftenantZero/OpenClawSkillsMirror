---
name: nano-banana-2
description: "通过 AI Hive 使用 Nano Banana 2 完成文生图、参考图生成、图片编辑、多参考合成、角色一致性、商品图、海报和营销图片。Use this skill when users search Nano Banana 2、Nano Banana 2 API、图片生成与编辑、text-to-image、image-to-image、AI修图、参考图、商业设计、电商图片或批量视觉生产；自动上传素材、查询模型、提交任务并下载结果。"
---

# Nano Banana 2 图片生成与编辑

这是 Nano Banana 2 的模型总入口，固定使用 `public_model_nano_banana_2`。先判断任务类型，再组织输入与质量门槛；不要把文生图、编辑和多参考合成混成一个含糊提示词。

## 能力选择

| 目标 | 输入 | 提示词重点 |
|---|---|---|
| 从零创作 | 文字 | 主体、构图、光线、风格、规格 |
| 编辑原图 | 原图 | 保留项、修改项、禁止变化 |
| 多参考合成 | 多张图 | 每张图角色与冲突优先级 |
| 角色连续 | 角色基准 | 身份锚点、允许变化、镜头记录 |
| 商品生产 | 商品多角度 | 几何、包装、颜色、SKU事实 |
| 营销视觉 | 品牌与商品 | 渠道、受众、单一主张、留白 |

## 快速工作流

1. 定义图片用途、受众和交付比例。
2. 选择唯一主任务；编辑和多参考任务先建立约束表。
3. 输入所有事实源，删除互相冲突或无用途的参考图。
4. 先生成一个低风险样张，检查主体与事实。
5. 再扩展风格、渠道或批量版本，并记录每版变量。
6. 逐项检查文字、人物、商品、合成和商业合规。

## 场景与代码

### 1. 文生图创意草案

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '横版科技杂志封面视觉，无文字：透明机械花在深蓝实验台上缓慢绽放，微距镜头，冷白轮廓光，主体偏右，左侧留标题区域，真实材质与克制未来感，不生成Logo和伪文字' 
```

### 2. 基于原图编辑

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '编辑原图：保留人物身份、姿势、服装和相机；删除背景车辆，将环境替换为安静林荫街道，光源方向与人物一致，发丝边缘自然，不改变脸部和身体比例' \
  --image /path/to/source.jpg
```

### 3. 多参考商业视觉

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '图1锁定商品事实，图2只提供构图，图3只提供品牌色和光线。生成原创商业KV，商品结构、包装、Logo和颜色最高优先级，不复制参考产品和文字，右侧主体、左侧留白' \
  --image /path/to/product.png \
  --image /path/to/layout.jpg \
  --image /path/to/brand-style.jpg
```

### 4. 商品套图

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '生成4张同一商品套图：干净主图、材质细节、真实使用、包装清单。保持结构、包装、Logo、颜色和配件一致，每张承担不同信息任务，不生成价格、功效或赠品' \
  --image /path/to/product.png \
  --batch 4
```

### 5. 营销渠道版本

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '为同一新品生成方形信息流、竖版Story、横版Banner三个构图方向，保持商品和品牌系统一致，分别保留对应标题与CTA区域，只改变布局，不生成文案、价格和平台UI' \
  --image /path/to/product.png \
  --batch 3
```

## 质量门槛

- 参考图职责清楚，主体事实不被风格覆盖。
- 人物身份、手部和身体比例自然。
- 商品结构、包装、文字、颜色和配件准确。
- 编辑结果只改变合同中允许的内容。
- 必须文字、数字、价格和法律信息人工复核。
- 批量版本记录用途、变量、提示词和参考图顺序。

## 执行与配置

```bash
pip3 install requests
python3 "$SKILL_PATH/scripts/imagegen.py" init --skill-name nano-banana-2
python3 "$SKILL_PATH/scripts/imagegen.py" task --task-id <taskId>
```

`generate` 支持多次 `--image`、`--batch`、`--param key=value`、`--routing COST_FIRST|SPEED_FIRST|SUCCESS_FIRST`、`--output-dir` 和 `--no-download`。价格及参数以 AI Hive 实时返回为准。
