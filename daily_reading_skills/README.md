# Daily Reading Skills

一套面向 `论文检索 -> 推荐 -> 点评 -> 笔记 -> 作者机构图谱 -> 共读精读` 的 Codex skills 仓库。

这份仓库整理自当前本机可用的技能集，目标是把它们沉淀成一个可版本化、可迁移、可复用的 repo，
同时保留现有的相对路径结构，方便直接同步到 `~/.codex/skills/`。

## 包含内容

### 论文流水线

- `daily-papers`
  - 每日论文推荐的一句话入口
- `daily-papers-fetch`
  - 抓取、打分和富化论文
- `daily-papers-review`
  - 生成推荐点评
- `daily-papers-notes`
  - 批量生成正式论文笔记并回填链接

### 单篇与图谱

- `paper-reader`
  - 一次性高质量读论文 / 写正式笔记
- `paper-author-landscape`
  - 单篇或多篇汇总的作者 / 实验室 / 机构图谱
- `generate-mocs`
  - 刷新 Obsidian 目录页

### 共读与精读

- `guided-reading`
  - 书籍 / 论文分次共读
  - 学习地图
  - session 记录
  - 小测
  - 笔记纠错
  - 概念回填

### 共享依赖

- `_shared`
  - 配置读取
  - MOC 生成脚本
  - 通用配置文件

## 仓库结构

```text
daily_reading_skills/
├── README.md
├── .gitignore
├── _shared/
├── daily-papers/
├── daily-papers-fetch/
├── daily-papers-review/
├── daily-papers-notes/
├── paper-reader/
├── paper-author-landscape/
├── generate-mocs/
└── guided-reading/
```

这个结构刻意对齐 `~/.codex/skills/`，这样技能中的相对路径引用例如 `../_shared/...` 不需要重写。

## 当前配置取向

这份 repo 当前默认偏向：

- `trajectory inference`
- `single-cell`
- `spatial omics`
- `optimal transport`
- `Schrodinger bridge / flow matching`
- `virtual cell / perturbation prediction`

如果要迁移到其他方向，只需要改 `_shared/user-config.json` 或本地覆盖配置。

## 安装方式

### 直接同步到 Codex skills 目录

```bash
rsync -a daily_reading_skills/ ~/.codex/skills/
```

### 或只同步其中一部分

```bash
rsync -a daily_reading_skills/guided-reading/ ~/.codex/skills/guided-reading/
rsync -a daily_reading_skills/_shared/ ~/.codex/skills/_shared/
```

## 配置方式

仓库中提供：

- `_shared/user-config.json`
  - 仓库级默认配置
- `_shared/user-config.local.example.json`
  - 本地覆盖示例

建议做法：

1. 复制示例文件：

```bash
cp _shared/user-config.local.example.json _shared/user-config.local.json
```

2. 修改本机路径：

- `obsidian_vault`
- `zotero_db`
- `zotero_storage`

3. 如有需要，再调整：

- `keywords`
- `negative_keywords`
- `domain_boost_keywords`
- `pubmed_journals`

## 依赖

基础依赖：

- `python3`
- `pdfinfo`
- `pdftotext`

推荐依赖：

- `PyYAML`
- Zotero
- Obsidian

## 典型用法

### 每日论文

- `今日论文推荐`
- `过去3天论文推荐`
- `跑一下论文点评`
- `跑一下论文笔记`

### 正式读论文

- `读一下这篇论文 ...`
- `读一下 Zotero 里的 ...`
- `这篇论文背后有哪些组在做`

### 作者机构图谱

- `分析一下现在有的论文的作者与机构图谱`
- `帮我摸一下这个方向的人和机构`

### 共读精读

- `我们一起读这本书 ...`
- `继续上次共读`
- `检查我的笔记`
- `给我出个小测`

## 不包含的内容

这个仓库没有整理 Codex 的系统技能，例如：

- `.system/skill-creator`
- `.system/skill-installer`

这些更适合作为本机工具，而不是当前 repo 的业务技能主体。

## 建议版本控制策略

建议提交：

- `SKILL.md`
- `agents/`
- `references/`
- `scripts/`
- `_shared/user-config.json`

建议不要提交：

- `_shared/user-config.local.json`
- `.DS_Store`
- `__pycache__/`

仓库里已经通过 `.gitignore` 处理了这些项。
