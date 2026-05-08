from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from lc_learning.llm import build_chat_model


def main() -> None:
    history = [
        HumanMessage(content="我是 Java 开发工程师，正在学习 LangChain。"),
        AIMessage(content="很好，我们可以用后端工程类比来理解 AI 应用。"),
    ]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个耐心的 AI 应用开发教练。"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    chain = prompt | build_chat_model(temperature=0.3) | StrOutputParser()
    result = chain.invoke(
        {
            "history": history,
            "question": "请结合我的背景，解释 RAG 为什么不是简单的全文搜索。",
        }
    )
    print(result)


if __name__ == "__main__":
    main()
