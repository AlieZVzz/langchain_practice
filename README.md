# LangChain AI Learning

这个仓库是一个面向 Java 开发工程师的 LangChain Python 学习框架。目标不是堆满示例，而是用一套清晰骨架把 AI 应用开发的关键路径串起来：Prompt、Chain、Memory、RAG、Agent、评测、工程化。

## 快速开始

```bash
uv sync --extra dev
cp .env.example .env
```

然后在 `.env` 里填入 `DEEPSEEK_API_KEY`。

运行第一个示例：

```bash
uv run python examples/01_prompt_chain.py
```

## 目录结构

```text
.
├── docs/
│   ├── roadmap-java-to-ai.md
│   └── langchain-study-plan.md
├── examples/
│   ├── 01_prompt_chain.py
│   ├── 02_chat_memory.py
│   ├── 03_rag_faiss.py
│   └── 04_agent_tools.py
├── src/lc_learning/
│   ├── config.py
│   └── llm.py
├── data/
│   ├── sample/
│   └── generated/
└── tests/
```

## 学习路线

建议按这个顺序推进：

1. `docs/roadmap-java-to-ai.md`: 先建立从 Java 后端到 AI 应用开发的能力地图。
2. `examples/01_prompt_chain.py`: 掌握 PromptTemplate、ChatModel、OutputParser 和 LCEL。
3. `examples/02_chat_memory.py`: 理解多轮对话状态如何进入 prompt。
4. `examples/03_rag_faiss.py`: 做一个最小可运行的本地 RAG。
5. `examples/04_agent_tools.py`: 理解 tool calling 和 agent 的边界。
6. 自己补一个小项目：知识库问答、代码解释助手、客服工单助手或简历优化助手。

## 参考资料

- LangChain Python 文档: https://python.langchain.com/docs/introduction/
- DeepSeek API 文档: https://api-docs.deepseek.com/
- LangChain ChatOpenAI 集成: https://python.langchain.com/docs/integrations/chat/openai/
- LangChain Expression Language: https://python.langchain.com/docs/concepts/lcel/
