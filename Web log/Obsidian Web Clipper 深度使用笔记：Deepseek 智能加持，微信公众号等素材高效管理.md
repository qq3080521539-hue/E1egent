---
title: "Obsidian Web Clipper 深度使用笔记：Deepseek 智能加持，微信公众号等素材高效管理"
source: "https://zhuanlan.zhihu.com/p/27980381867"
author:
  - "[[田公子电子工程师]]"
published:
created: 2026-04-16
description: "Obsidian Web Clipper 深度使用笔记：Deepseek 智能加持，微信公众号等素材高效管理前言在信息爆炸的时代，我们每天都需要从海量的网页中筛选和收集素材。今天，我将为大家带来 Obsidian Web Clipper 的深度使用笔…"
tags:
  - "clippings"
---
## 前言

在信息爆炸的时代，我们每天都需要从海量的网页中筛选和收集素材。今天，我将为大家带来 Obsidian Web Clipper 的深度使用笔记，重点介绍如何结合 **[Deepseek 大模型](https://zhida.zhihu.com/search?content_id=254618686&content_type=Article&match_order=1&q=Deepseek+%E5%A4%A7%E6%A8%A1%E5%9E%8B&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0NTA5ODMsInEiOiJEZWVwc2VlayDlpKfmqKHlnosiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ2MTg2ODYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.ZfPYM_RpRff88tO9jXhsd_phDLoZG0oLWKumTCYV2pY&zhida_source=entity)** ，实现网页内容 **快速剪藏、智能总结和高效管理** ，让你的素材收集工作流焕然一新。

## 什么是 Obsidian Web Clipper (Deepseek 智能版)？

Obsidian Web Clipper 是一款强大的浏览器扩展，它可以将网页内容快速保存到你的 Obsidian 知识库中。而我们今天要深入探讨的，是如何通过配置 **Deepseek API** ，让 Obsidian Web Clipper 拥有 **AI 智能摘要** 的能力。这意味着，在剪藏网页内容的同时，Deepseek 大模型可以自动为你 **总结文章要点、提取关键信息** ，并将其一并保存到 Obsidian 笔记中，极大地提升了素材处理效率。

**核心优势：**

- **Deepseek 智能摘要：** 利用 Deepseek 大模型自动总结网页内容，快速获取文章核心信息。
- **高效网页剪藏：** 一键保存网页文章、图片、文字等，告别手动复制粘贴。
- **[Markdown](https://zhida.zhihu.com/search?content_id=254618686&content_type=Article&match_order=1&q=Markdown&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0NTA5ODMsInEiOiJNYXJrZG93biIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI1NDYxODY4NiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.oqcW-B-umTww4Y70awHpuzLesPorA6FFI7Bn7hqgVZw&zhida_source=entity) 深度集成：** 完美保存为 Markdown 格式，无缝衔接 Obsidian 编辑和链接功能。
- **灵活配置 API：** 支持 Deepseek 等多种 API，可根据需求选择合适的模型。
- **自定义模板：** 高度可定制的模板，满足个性化剪藏需求。

## 安装与配置 Obsidian Web Clipper (Deepseek 版)

### 1\. 安装浏览器扩展

- **Chrome:** 在 Chrome 网上应用店搜索 "Obsidian Web Clipper" 并安装。
- **Firefox:** 在 Firefox 附加组件商店搜索 "Obsidian Web Clipper" 并安装。
- **Edge:** 在 edge的扩展-获取扩展中，搜索 "Obsidian Web Clipper" 并安装。

### 2\. 注册并获取 Deepseek API 密钥

要使用 Deepseek 的智能摘要功能，你需要先注册 Deepseek 账号并获取 API 密钥：

1. 访问 **[Deepseek 官网](https://link.zhihu.com/?target=https%3A//www.deepseek.com/)** 并注册账号。
2. 登录后，进入 **[API 页面](https://link.zhihu.com/?target=https%3A//platform.deepseek.com/api_keys)** 创建新的 API 密钥，并妥善保存。
3. 根据需要，前往 **[充值页面](https://link.zhihu.com/?target=https%3A//platform.deepseek.com/top_up)** 充值，Deepseek 提供了非常实惠的模型 v3 版本。

### 3\. 配置 Obsidian Web Clipper 插件

1. 点击浏览器工具栏中的 Obsidian Web Clipper 图标，进入设置页面。
2. **General 设置：** 可以在general-language中设置语言为简体中文。配置你的 Obsidian Vault 名称，确保 Web Clipper 可以正确连接到你的知识库，默认情况是保存到你打开的vault中。
3. **Template 设置：** 模板决定了剪藏内容的格式和结构。你可以使用默认模板，也可以自定义模板以添加摘要等功能。 （ *后文将提供示例模板配置* ）
4. **Interpreter（解释器） 设置 (关键步骤)：** 这是配置 并使用大模型如Deepseek 的核心部分。
- **Behavior:** 根据个人习惯设置 "Automatically run"，开启后每次剪藏会自动调用 API 进行总结，也可选择手动触发以节省 API 调用次数。
- **Providers:** \*\*重点！ Provider 务必先选择 `OpenAI` \*\*。 然后将provider改为custom（自定义），已获取URL格式。
- **Base URL:** 把url前半部分替换为想要的比如硅基流动或者无问芯穹等的base url，最后效果是 [api.siliconflow.cn/v1/c](https://link.zhihu.com/?target=https%3A//api.siliconflow.cn/v1/chat/completions) 。
- **API Key:** 填写 从硅基流动 官网获取的 API 密钥。
- **Models:** 模型ID一定是要从硅基流动复制过来的完整名称
![](https://pica.zhimg.com/v2-5ee5c936d52445c58036136374de96c8_1440w.jpg)

![](https://pic4.zhimg.com/v2-09502616ffebea7aa0db7ecff5d58cd1_1440w.jpg)

**大家也可以使用其他模型或者本地ollama模型，不同模型处理效果和处理速度会有差异。**

### 4\. Template 模板配置 (示例)

为了实现 AI 摘要功能，你需要修改 Obsidian Web Clipper 的模板。以下是一个示例模板配置，你可以在 "Template" 设置中点击 "New template" -> "Import" 导入 JSON 文件，或者手动修改现有模板： **官方的template地址如下** **[obsidian-community/web-clipper-templates: Community collection of templates for the official Obsidian web clipper.](https://link.zhihu.com/?target=https%3A//github.com/obsidian-community/web-clipper-templates)**

***warning！！！***

**在 "Interpreter Context" 中，你必须、必须、必须添加和在note content中同样的内容，以指示 Deepseek 模型进行摘要和关键要素提取，并利用变量将提取后的信息由大模型传递到笔记内容 note content里去** 目前市面上好多博主的笔记说明里都没有说到这一点。

![](https://pica.zhimg.com/v2-f8aabf9a962d1646fa4b6355bcc954f4_1440w.jpg)

![](https://pica.zhimg.com/v2-618a0766eb60520bd2c197f80206e0bc_1440w.jpg)

**只有note content添加的效果**

![](https://pica.zhimg.com/v2-1b24987ba4148ee5ea7a7939fe174122_1440w.jpg)

**note content和Interpreter Context都添加的效果**

![](https://pic4.zhimg.com/v2-d2c02fb387a155d25c3c3168cb061b57_1440w.jpg)

## 使用 Obsidian Web Clipper 收集素材

1. **浏览网页，发现素材：** 在 Chrome 或 Edge 浏览器中打开你感兴趣的网页文章，例如微信公众号文章、行业资讯、案例分析等。
2. **点击 Web Clipper 图标：** 点击浏览器工具栏中的 Obsidian Web Clipper 图标。
3. **预览和确认：** 在弹出的界面中，你可以预览剪藏效果，并选择保存位置（例如，你可以创建一个名为 "Clippings" 的文件夹作为默认剪藏目录，可以在设置里修改默认位置，也可以在剪藏时修改为比如inbox或者inbox/AAA）。
4. **智能摘要 (Deepseek 自动运行或手动触发)：为了省钱还是手动吧**
- 如果 "Automatically run" 已开启，Web Clipper 会自动调用 Deepseek API 进行摘要。稍等片刻，你就可以在预览界面看到 AI 总结的摘要和关键要素。
- 如果 "Automatically run" 关闭，你需要手动点击 "Run Interpreter" 按钮来触发 Deepseek API 调用。
1. **添加到 Obsidian：** 点击 "Add to Obsidian" 按钮，剪藏内容（包括智能摘要）将保存到你的 Obsidian Vault 中。

## 优化技巧与建议

- **创建专属素材库：** 在 Obsidian 中建立专门的文件夹，例如 "微信公众号素材库" 或 "文章剪藏"，用于存放剪藏的网页内容，方便分类管理。
- **善用标签分类：** 在模板中预设或手动添加标签，例如 `#灵感`, `#案例分析`, `#行业报告` 等，方便后续通过obsidian利用标签进行检索和回顾。
- **自定义模板字段：** 根据你的需求，在模板中添加更多属性字段，例如 "作者"、"来源平台"、"阅读状态" 等，更精细化地管理素材。
- **定期回顾与整理：** 定期回顾剪藏的素材，结合 Deepseek 等大模型提供的摘要和关键要素，快速筛选有价值的信息，并将其融入到你的微信公众号文章创作中。
- **配合 Local image plus 插件：** 配合 Local image plus 插件使用效果更佳，可以更好地管理剪藏图片。

## 总结

Obsidian Web Clipper 结合 大模型，为写作者和喜欢整理笔记的人打造了一个 **高效、智能的素材收集和管理工作流** 。它不仅能快速剪藏网页内容，更能利用 AI 智能提取文章核心信息，大大节省了素材处理时间，让你更专注于内容创作本身。掌握这款利器，相信你输出的文章质量和创作效率都将得到显著提升！

---

**互动话题：** 你还希望 Obsidian Web Clipper 增加哪些智能功能来辅助写作和整理笔记？欢迎在评论区分享你的想法！

发布于 2025-03-04 22:38・北京[Obsidian](https://www.zhihu.com/topic/21349840)[DeepSeek](https://www.zhihu.com/topic/28820212)