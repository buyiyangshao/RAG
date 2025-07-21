# DeepSleep AI 助手

![Logo](static/images/deepsleep_logo1.png)

一款基于大模型的智能对话系统，集成 RAG 知识库、语音合成等能力，提供高效的人机交互体验。

## 🌟 核心功能

### 1. 智能对话

- 支持多轮上下文对话 ([RAGChatter.py](file://d:\Multimodal_tasks_AI\RAG\RAGChatter.py))
- 提供文生图开关 ([chat.html](file://d:\Multimodal_tasks_AI\templates\chat.html))
- 支持图片/音频文件上传 ([chat.js](file://d:\Multimodal_tasks_AI\static\js\chat.js))

### 2. 知识库管理

- 多文档 RAG 检索 ([RAGBuild.py](file://d:\Multimodal_tasks_AI\RAG\RAGBuild.py))
- 支持 PDF/TXT 文件上传 (`templates/chat_rag.html`)
- 相似问题缓存优化 ([get_similar_cached_answer](file://d:\Multimodal_tasks_AI\RAG\RAGBuild.py#L134-L201))

### 3. 用户系统

- 注册/登录/密码重置 ([forget-password.css](file://d:\Multimodal_tasks_AI\static\css\forget-password.css))
- 图形验证码防护 ([login.html](file://d:\Multimodal_tasks_AI\templates\login.html))
- 管理员后台 ([admin.html](file://d:\Multimodal_tasks_AI\templates\admin.html))

### 4. 语音合成

- 预设 6 种音色 ([voice_synthesize.py](file://d:\Multimodal_tasks_AI\multi_modal\voice_synthesize.py))
- 支持自定义声音克隆
- 腾讯云 COS 存储集成

## 🛠️ 技术栈

### 后端

- **核心框架**: Flask (Python)
- **向量数据库**: Redis (`langchain_redis`)
- **嵌入模型**: DashScope (`DashScopeEmbeddings`)
- **大模型**: 通义千问 (`qwen-plus`)

### 前端

- **UI 框架**: 纯 HTML/CSS + FontAwesome
- **Markdown 渲染**: marked.js + highlight.js
- **交互设计**: 响应式布局 ([home.css](file://d:\Multimodal_tasks_AI\static\css\home.css))

### 基础设施

- **会话存储**: Redis (`RedisChatMessageHistory`)
- **文件存储**: 腾讯云 COS (`cos-python-sdk-v5`)
- **API 网关**: 阿里云 DashScope

## 🚀 快速开始

1. 安装依赖：

```bash
pip install -r requirements.txt
```



2. 配置环境变量：
```bash
# api_url_messages.json

{
  "tongyi_api_key": "your_api_key",
  "redis_url": "redis://localhost:6379/0",
  "api_base": "<https://dashscope.aliyuncs.com/compatible-mode/v1>"
}
```



1. 启动服务：

```bash
flask run --host=0.0.0.0 --port=5000
```

## 📂 项目结构

```
Multimodal_tasks_AI/
├── RAG/                     # 知识库核心模块
├── multi_modal/             # 语音合成模块
├── static/                  # 静态资源
├── templates/               # 前端页面
├── requirements.txt         # 依赖清单
└── README.md                # 项目文档
```
