from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from lc_learning.embeddings import HashEmbeddings
from lc_learning.llm import build_chat_model


DOCUMENTS = [
    """
    LangChain 的核心价值是把 Prompt、模型、工具、检索器和输出解析器组合成可维护的 AI 应用链路。
    对 Java 工程师来说，可以把 LCEL 理解成一种声明式 pipeline。
    """,
    """
    RAG 是 Retrieval-Augmented Generation。它先从外部知识库检索相关片段，再把片段作为上下文交给模型回答。
    RAG 的质量取决于文档切分、embedding、召回、重排、prompt 和答案约束。
    """,
    """
    Agent 适合需要模型根据目标选择工具的场景。对于固定流程，普通 chain 通常更稳定、更容易评测。
    工具调用必须控制权限、参数和最大执行步数。
    """,
]


def format_docs(docs) -> str:
    return "\n\n".join(doc.page_content for doc in docs)


def main() -> None:
    splitter = RecursiveCharacterTextSplitter(chunk_size=180, chunk_overlap=30)
    splits = splitter.create_documents(DOCUMENTS)

    embeddings = HashEmbeddings()
    vector_store = FAISS.from_documents(splits, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})

    prompt = ChatPromptTemplate.from_template(
        """请只根据下面的上下文回答问题。
如果上下文没有答案，就说“我不知道”。

上下文:
{context}

问题:
{question}
"""
    )

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | build_chat_model(temperature=0)
        | StrOutputParser()
    )

    print(chain.invoke("Java 工程师应该如何理解 RAG？"))


if __name__ == "__main__":
    main()
