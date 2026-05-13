import os,json
from typing import Sequence
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
# message_to_dict 将message对象转换成字典

class FileChatMessageHistory(BaseChatMessageHistory):
    """
    保存会话历史记录到文件
    """
    def __init__(self,session_id,storage_path):
        self.session_id = session_id
        self.storage_path = storage_path

        self.file_path = os.path.join(self.storage_path, f"{self.session_id}.json")
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)


    def add_message(self, message: BaseMessage) -> None:
        all_messages = self.messages
        all_messages.append(message)

        new_messages = [message_to_dict(msg) for msg in all_messages]

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f, ensure_ascii=False, indent=2)


    @property # 装饰器
    def messages(self) -> list[BaseMessage]:
        # 当前文件内：list[BaseMessage]
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                messages_data = json.load(f) # 读取文件内容
                return messages_from_dict(messages_data) # 将数据转换成BaseMessage类实例


        except FileNotFoundError:
            return []


    def clear(self) -> None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)




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

def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt


base_chian = prompt | model | str_parser



# 通过会话id获取InMemoryChatMessageHistoryl类对象

def get_history(session_id):
    """获取历史消息
        这样就很方便了，我们取session_id的时候只需要从store字典当中取就行了
    """
    return FileChatMessageHistory(session_id,storage_path="./chat_history")



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
    # res =conversation_chain.invoke({"input":"小王有3只钢笔"},session_config)
    # print("第一次执行",res)
    #
    # res =conversation_chain.invoke({"input":"小雪有5个橡皮"},session_config)
    # print("第二次执行",res)

    res =conversation_chain.invoke({"input":"总共有多少个文具"},session_config)
    print("第三次执行",res)