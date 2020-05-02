#Action1：设计你自己的句子生成器
import random

# 语法
host = """
host = 寒暄 报数 询问 具体业务 结尾
报数 = 我是工号 数字 号 ,
数字 = 单个数字 | 数字 单个数字
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好
询问 = 请问你要 | 您需要
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？"""
# 语法字典
def getGrammarDict(host, linesplit = "\n", hostsplit ="="):
    result = {}
    for line in host.split(linesplit):
        if not line.strip():
            continue
        expr, statement = line.split(hostsplit)
        result[expr.strip()] = [i.split() for i in statement.split("|")]
    return result
host_dict = getGrammarDict(host)
print(host_dict)
# 生成句子
def generate(host_dict, target, isEng = False):
    if target not in host_dict:
        return target
    find = random.choice(host_dict[target])
    blank = ''
    if isEng:
        blank = ' '
    return blank.join(generate(host_dict, t, isEng) for t in find)
print(generate(host_dict,"host"))
print(generate(host_dict,"host", True))

