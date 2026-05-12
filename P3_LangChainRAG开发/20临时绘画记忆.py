from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model = "qwen3-max")
#prompt = PromptTemplate.from_template(
#    "你需要根据会话历史回应用户问题，对话历史:{chat_history},用户提问
#    :{input},请回答"
#)
prompt= ChatPromptTemplate.from_messages(
    [
        ("system","你需要根据会话历史回应用户问题，对话历史:"),
        MessagesPlaceholder("chat_history"),
        ("human","请回答如下问题：{input}")
    ]
)