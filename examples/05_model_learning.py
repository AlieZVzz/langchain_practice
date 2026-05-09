from langchain_openai import ChatOpenAI
from lc_learning.llm import build_chat_model

result = build_chat_model(temperature=0.2).invoke("Hello, world!")
print(result)
