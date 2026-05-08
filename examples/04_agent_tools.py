from langchain.agents import create_agent
from langchain.tools import tool

from lc_learning.llm import build_chat_model


@tool
def calculate_monthly_llm_cost(requests_per_day: int, input_tokens: int, output_tokens: int) -> str:
    """Estimate monthly LLM cost with a simple fixed sample price."""
    input_price_per_1m = 0.15
    output_price_per_1m = 0.60
    days = 30
    input_cost = requests_per_day * input_tokens * days / 1_000_000 * input_price_per_1m
    output_cost = requests_per_day * output_tokens * days / 1_000_000 * output_price_per_1m
    total = input_cost + output_cost
    return f"Estimated monthly cost: ${total:.2f}"


@tool
def recommend_langchain_topic(level: str) -> str:
    """Recommend the next LangChain topic for a learner."""
    topics = {
        "beginner": "PromptTemplate + LCEL",
        "intermediate": "RAG with retriever and vector store",
        "advanced": "Agent tools, evaluation, and tracing",
    }
    return topics.get(level.lower(), "Start with PromptTemplate + LCEL")


def main() -> None:
    tools = [calculate_monthly_llm_cost, recommend_langchain_topic]
    agent = create_agent(
        model=build_chat_model(temperature=0),
        tools=tools,
        system_prompt="你是 AI 应用开发学习助手。需要计算或查询时，优先使用工具。",
    )

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "我是 intermediate 水平，每天 2000 次请求，"
                        "每次约 1200 input tokens 和 400 output tokens。"
                        "请推荐学习主题并估算月成本。"
                    ),
                }
            ]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
