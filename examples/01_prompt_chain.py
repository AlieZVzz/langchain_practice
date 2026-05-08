from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from lc_learning.llm import build_chat_model


def main() -> None:
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "你是一名资深 AI 应用架构师，擅长把 Java 后端经验迁移到 AI 应用开发。",
            ),
            (
                "human",
                "请用 5 个要点解释：{topic}。每个要点都给一个 Java 后端类比。",
            ),
        ]
    )
    model = build_chat_model(temperature=0.2)
    chain = prompt | model | StrOutputParser()

    result = chain.invoke({"topic": "LangChain 中的 LCEL"})
    print(result)


if __name__ == "__main__":
    main()
