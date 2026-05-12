from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

# 创建模型实例
llm = ChatTongyi(model = 'qwen-max')
# 创建消息实例
messages = [
    SystemMessage(content="你是一名诗人"),
    HumanMessage(content="你是谁"),
    AIMessage(content="我是一个诗人"),
    HumanMessage(content="请写一个关于机器学习的段落"),
]
# 流式输出
for chunk in llm.stream(messages):
    print(chunk.content, end="",flush= True)