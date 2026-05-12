from langchain_classic.chains.summarize.map_reduce_prompt import prompt_template
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我起个名字，简单回答"
)
# 调用.format方法注入信息即可
# prompt_text = prompt_template.format(lastname="张", gender="女儿")
# print(prompt_text)
#
# model = Tongyi(model = 'qwen-max')
# res = model.invoke(input = prompt_text)
# print(res)
model = Tongyi(model = 'qwen-max')

chain = prompt_template | model # | summarize_prompt
res = chain.invoke(input = {"lastname": "张", "gender": "女儿"})
print( res)