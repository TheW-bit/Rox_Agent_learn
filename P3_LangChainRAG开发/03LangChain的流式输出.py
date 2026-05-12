from langchain_community.llms.tongyi import Tongyi
import os

model = Tongyi(model = 'qwen-max')
# 通过stream方法获得流式输出
res = model.stream(input = '请写一个关于机器学习的段落')
for chunk in res:
    print(chunk,end="",flush=True)