from langchain_community.llms.tongyi import Tongyi
import os


llm = Tongyi(model = 'qwen-max')

res = llm.invoke(input = '请写一个关于机器学习的段落')
print(res)