from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model = "qwen3-max")

# prompt = PromptTemplate.from_template(
#        "你需要根据会话历史回应用户问题，对话历史:{chat_history},用户提问:{input},请回答"
#     )

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","你需要根据会话历史回应用户问题，对话历史:"),
        MessagesPlaceholder("chat_history"),
        ("human","请回答如下问题：{input}")
    ]
)

str_parser = StrOutputParser()

base_chian = prompt | model | str_parser

store = {} # 存储会话 key就是会话id，value就是InMemoryChatMessageHistory类对象

# 通过会话id获取InMemoryChatMessageHistoryl类对象

def get_history(session_id):
    """获取历史消息
        这样就很方便了，我们取session_id的时候只需要从store字典当中取就行了
    """
    if session_id not in store:

        store[session_id] = InMemoryChatMessageHistory() #InMemoryChatMessageHistory() 是 LangChain 提供的内存聊天历史管理器,功能：在内存中存储和管理对话消息历史记录：
    return store[session_id] #


# 创建一个新的链，对原有链增强功能：自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chian, # 基础链 被增强的原有chain
    get_history, # 获取历史消息的函数，通过会话id获取InMemoryChatMessageHistoryl类对象
    input_messages_key="input",# 历史消息的key
    history_messages_key="chat_history" # 添加历史消息的key

)


if __name__ == "__main__":
    # 固定格式。添加Langchian的配置，为当前程序配置所属的session——id
    session_config = {
        "configurable":{
            "session_id":"user_001"
        }
    }
res =conversation_chain.invoke({"input":"小王有3只钢笔"},session_config)
print("第一次执行",res)

res =conversation_chain.invoke({"input":"小雪有5个橡皮"},session_config)
print("第二次执行",res)

res =conversation_chain.invoke({"input":"总共有多少个文具"},session_config)
print("第三次执行",res)