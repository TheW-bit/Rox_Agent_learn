from tempfile import template

from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
"""
PromptTemplate->StringPromptTemplate->BasePromptTemplate
FewShotPromptTemplate->StringPromptTemplate->BasePromptTemplate
ChatPromptTemplate->BaseChatPromptTemplate->BasePromptTemplate
"""

template = PromptTemplate.from_template("我的邻居是{lastname}，爱好是{hobby}")
res = template.format(lastname="张大明",hobby = "钓鱼")
print(res,type(res))

res2 = template.invoke({"lastname":"周子昂","hobby":"唱歌"})
print(res2,type(res2))