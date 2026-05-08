# LangChain 学习计划

## 核心心法

LangChain 最适合用来学习和搭建 AI 应用的“组合方式”。不要一开始就追所有组件，先理解几条主链路：

- Prompt chain：把输入稳定变成输出。
- Chat chain：让多轮上下文可控地进入模型。
- RAG chain：让模型基于外部知识回答。
- Agent chain：让模型在有限工具中做决策。
- Eval chain：让每次修改都能被验证。

## 示例顺序

1. `01_prompt_chain.py`
   - 学 PromptTemplate、ChatOpenAI、StrOutputParser。
   - 重点看 LCEL 的组合方式。

2. `02_chat_memory.py`
   - 学如何保存消息历史。
   - 重点理解“记忆不是魔法，只是被重新放回 prompt 的上下文”。

3. `03_rag_faiss.py`
   - 学文档切分、embedding、向量库、retriever。
   - 重点观察 chunk 大小对答案的影响。

4. `04_agent_tools.py`
   - 学 tool calling 和 agent executor。
   - 重点理解工具描述越清楚，调用越稳定。

## 每个示例的练习方式

- 先不改代码跑一遍。
- 改 prompt，观察输出变化。
- 改模型参数，比如 `temperature`。
- 加一个失败输入，记录为什么失败。
- 抽出一个你熟悉的 Java 业务场景重写示例。

## 从 Java 迁移过来的类比

| Java 后端概念 | AI 应用概念 |
| --- | --- |
| Controller DTO | 用户输入 schema |
| Service | Chain / Runnable |
| Repository / Client | Tool / Retriever |
| JSON 序列化 | OutputParser |
| 单元测试 | Eval case |
| 分布式 tracing | LangSmith / tracing |
| 限流熔断 | LLM timeout / retry / fallback |

## 建议阅读顺序

- 官方 Introduction
- LCEL
- Chat models
- Prompt templates
- Retrieval
- Tool calling
- Agents
- Evaluation
