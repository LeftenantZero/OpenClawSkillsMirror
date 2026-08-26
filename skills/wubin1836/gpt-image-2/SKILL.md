---
name: gpt-image-2
description: "通过 AI Hive 使用 GPT Image 2 完成图片生成与编辑，覆盖文生图、图生图、多参考合成、商品图、海报文字、换背景、角色一致性和广告版本。Use this skill when users search GPT Image 2、GPT-Image-2、OpenAI image generation、ChatGPT Images、图片生成编辑、AI修图、电商商品图、营销海报、带字图片或批量视觉生产；自动上传参考图、提交任务并下载结果。"
---

# GPT Image 2 图片生成与编辑

把本 Skill 作为 GPT Image 2 的总入口，固定使用 `public_model_gpt_image_2`。先确认交付目标和事实约束，再选择从文字起稿、基于原图编辑或用多张参考图合成；不要把创意探索与最终商业交付混在一次生成里。

## 选择工作模式

| 用户目标 | 输入 | 核心控制 |
|---|---|---|
| 从零生成 | 文字简报 | 主体、构图、光线、风格、用途 |
| 修改现有图片 | 原图 | 修改项、保留项、禁止变化 |
| 合并参考资产 | 多张参考图 | 每张图负责什么、冲突优先级 |
| 商品与广告生产 | 商品图 + 简报 | 商品事实、留白、渠道与审核 |
| 带文字视觉 | 精确文案 | 字符、层级、位置和逐字复核 |

## 核心流程

1. 收集用途、受众、主体、尺寸、必须出现和禁止出现内容。
2. 把商品结构、人物身份、Logo、颜色、价格和法律文案列为事实锁定项。
3. 先生成 2–4 个方向样张，只改变一个创意变量以便比较。
4. 选定方向后加入参考图，处理细节、排版留白和渠道版本。
5. 逐项检查事实、文字、边缘、手部、反射、阴影和输出规格。

## 场景与代码

### 1. 从简报生成 Campaign 概念

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '为无糖气泡水设计夏季品牌主视觉：18–30岁城市用户，蓝银色罐装产品居中，阳光穿过冰块形成清爽折射，右侧保留标题和CTA区域，不生成价格、促销、虚假认证或不可读文字；输出三个构图明显不同的创意方向' \
  --batch 3
```

### 2. 基于原图做受控编辑

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '保留人物身份、表情、服装、姿势和相机角度，只移除左后方路人和地面杂物，补全自然背景纹理与接触阴影；不得改变脸部、身材、Logo、画面裁切和整体色调' \
  --image /path/to/original.jpg
```

### 3. 多参考资产合成

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '图1只提供商品结构和包装文字，图2只提供大理石台面与晨光，图3只提供品牌色和构图节奏。生成高端护肤品广告；商品事实以图1为最高优先级，不复制图2中的其他商品，不生成新Logo、价格或功效承诺' \
  --image /path/to/product.png \
  --image /path/to/light-reference.jpg \
  --image /path/to/brand-board.png
```

### 4. 生成带准确短文案的海报

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '制作竖版新品海报，仅出现以下两行文字，字符必须完全一致：第一行“轻一点，走更远”，第二行“新品上市”。第一行大号无衬线体，第二行小号；文字置于上方留白区，不生成其他字母、数字、Logo或价格' \
  --param aspect_ratio=3:4
```

### 5. 从商品母图扩展电商套图

```bash
python3 "$SKILL_PATH/scripts/imagegen.py" generate \
  --prompt '基于参考商品生成五张电商套图：白底主图、45度细节图、真实使用场景、尺寸留白信息图、包装清单。所有版本保持商品结构、颜色、包装、Logo和配件数量一致；不添加文案、尺寸数字、赠品或功能状态' \
  --image /path/to/approved-product.png \
  --batch 5
```

## 交付检查

- 逐字核对画面内文案；关键价格、条款和法律文字建议后期排版。
- 对照参考图检查商品、人物、Logo、包装和品牌颜色。
- 检查手部、边缘、透明材质、反射、阴影、透视和接触关系。
- 确认每个渠道版本重新构图，不用粗暴裁切破坏主体或留白。
- 保留提示词、参考图、任务 ID 与批准版本，便于复现和回滚。

## 执行

```bash
pip3 install requests
python3 "$SKILL_PATH/scripts/imagegen.py" init --skill-name gpt-image-2
python3 "$SKILL_PATH/scripts/imagegen.py" task --task-id <taskId>
```

支持 `--image` 多参考、`--batch` 批量、`--param key=value`、路由选择和自定义输出目录。平台规格与广告政策会变化，正式投放前按目标平台当前规则复核。
