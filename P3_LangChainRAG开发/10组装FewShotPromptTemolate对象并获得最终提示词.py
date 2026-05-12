
from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
example_template = PromptTemplate.from_template("单词:{word}, 反义词：{antonym}")
example_data = [
    {"word": "good", "antonym": "bad"},
    {"word": "tall", "antonym": "short"},
    {"word": "big", "antonym": "small"},
    {"word": "high", "antonym": "low"},
    {"word": "far", "antonym": "close"},
    {"word": "young", "antonym": "old"},
    {"word": "happy", "antonym": "sad"},
    {"word": "fast", "antonym": "slow"},
    {"word": "cold", "antonym": "warm"},
    {"word": "大", "antonym": "小"},
]
few_shot_prompt = FewShotPromptTemplate(
    examples=example_data,
    example_prompt=example_template,
    prefix="请给出单词的反义词,我·提供如下的示例",
    suffix="基于前面的示例告诉我，单词:{input}, 的反义词是：",
    input_variables=["input"],
    example_separator="\n",
)
# 获得最终提示词
prompt_text = few_shot_prompt.invoke(input= {"input": "左"}).to_string()
print(prompt_text)



model = Tongyi(model = 'qwen-max')
print(model.invoke(input = prompt_text))