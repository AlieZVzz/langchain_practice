# Java 工程师转型 AI 应用开发 Roadmap

这条路线默认你已经具备 Java 后端基础：HTTP、数据库、缓存、消息队列、微服务、部署和排障。AI 应用开发不是放弃这些能力，而是把它们升级成“围绕模型构建可靠产品”的工程能力。

## 阶段 1: AI 应用基础

目标：知道大模型能做什么、不能做什么，以及为什么不能只靠 prompt 硬扛。

- LLM 基本概念：token、context window、temperature、top_p、system/user/assistant message。
- Prompt 基础：角色、任务、上下文、约束、输出格式、few-shot 示例。
- 常见能力边界：幻觉、时效性、数学与精确检索、长文本遗忘、工具调用失败。
- API 调用方式：OpenAI-compatible API、流式输出、超时、重试、限流。
- Java 类比：把模型看成一个不确定的远程服务，prompt 是请求协议，output parser 是响应 DTO 校验。

交付物：

- 写 5 个 prompt，并记录输入、输出、失败样例和改进方式。
- 跑通 `examples/01_prompt_chain.py`。

## 阶段 2: Python 与 LangChain 基础

目标：能用 Python 写出可维护的 AI 应用原型。

- Python 工程：虚拟环境、依赖管理、包结构、pytest。
- LangChain 核心对象：ChatModel、PromptTemplate、OutputParser、Runnable。
- LCEL：用 `prompt | model | parser` 组合链路。
- 结构化输出：JSON、Pydantic schema、错误修复。
- Java 类比：Runnable 类似可组合的 service pipeline，parser 类似反序列化和校验层。

交付物：

- 为一个业务场景做“输入 -> prompt -> 模型 -> 结构化输出”的链。
- 跑通 `examples/02_chat_memory.py`。

## 阶段 3: RAG 知识库问答

目标：能把企业文档、代码库、FAQ 接入模型，减少幻觉。

- 文档加载：txt、markdown、pdf、网页。
- 文本切分：chunk size、overlap、metadata。
- Embedding：向量化、相似度、召回质量。
- Vector Store：FAISS、Chroma、Milvus、pgvector。
- Retrieval：top_k、过滤、rerank、引用来源。
- Java 类比：RAG 像“搜索服务 + LLM 生成层”，不是简单把全文塞进 prompt。

交付物：

- 用本地 markdown/txt 做一个问答 demo。
- 跑通 `examples/03_rag_faiss.py`。

## 阶段 4: Agent 与工具调用

目标：理解什么时候该用 agent，什么时候普通 chain 更稳。

- Tool calling：定义工具名、描述、参数 schema。
- Agent loop：计划、调用工具、观察结果、继续推理。
- 风险控制：工具白名单、参数校验、权限边界、最大步数。
- 常见场景：查数据库、调用内部 API、创建工单、执行代码分析。
- Java 类比：tool 是后端 service adapter，agent 是带决策能力的 orchestration layer。

交付物：

- 做一个“查询订单状态/计算价格/生成回复”的模拟 agent。
- 跑通 `examples/04_agent_tools.py`。

## 阶段 5: 评测、监控与生产化

目标：从 demo 走向可以上线的 AI 应用。

- 评测集：正常样例、边界样例、攻击样例、回归样例。
- 指标：准确率、引用命中率、拒答率、延迟、成本。
- 可观测性：trace、prompt version、输入输出采样、失败聚类。
- 安全：PII 脱敏、prompt injection 防护、越权工具调用防护。
- 架构：异步任务、缓存、队列、fallback、灰度发布。
- Java 类比：把 AI 链路纳入已有 SRE、测试、CI/CD 和安全治理体系。

交付物：

- 为 RAG demo 建 20 条评测问题。
- 给一个 chain 加日志、耗时统计和失败重试。

## 12 周学习节奏

| 周期 | 重点 | 输出 |
| --- | --- | --- |
| 第 1-2 周 | LLM API、Prompt、Python 基础 | 10 个 prompt 实验 |
| 第 3-4 周 | LangChain LCEL、结构化输出 | 一个业务抽取 chain |
| 第 5-6 周 | RAG 文档问答 | 本地知识库 QA |
| 第 7-8 周 | Agent、工具调用 | 模拟业务助手 |
| 第 9-10 周 | 评测、日志、成本 | 小型 eval 套件 |
| 第 11-12 周 | 项目整合与部署 | 一个完整 AI 应用 demo |

## 推荐项目题目

- 公司内部制度问答助手：RAG + 引用来源 + 不知道就拒答。
- Java 代码解释助手：读取代码片段，解释职责、依赖和潜在风险。
- 客服回复助手：根据工单内容、知识库和语气要求生成回复。
- 面试题训练助手：围绕 Java、系统设计、AI 应用开发生成追问和评分。
