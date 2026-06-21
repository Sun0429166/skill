"""
公关文案修辞打分工具 score_statement.py
功能：输入公关声明文本，自动检测Ethos可信度、Pathos共情、Logos逻辑三类要素完整度打分
满分100，Ethos(40分)、Pathos(30分)、Logos(30分)
适配：企业致歉、明星回应、政府发布会口径三类文案
"""

def score_pr_text(text: str):
    # 定义三类修辞关键词库
    ethos_words = ["致歉", "整改", "停业", "排查", "监督", "处罚", "负责", "承担责任", "监管", "回访", "赔付"]
    pathos_words = ["愧疚", "痛心", "抱歉", "理解", "担忧", "沉痛", "共情", "难过", "感谢监督"]
    logos_words = ["时间线", "第一步", "第二步", "措施", "方案", "期限", "流程", "核查", "数据"]

    # 匹配计数
    ethos_count = sum(1 for word in ethos_words if word in text)
    pathos_count = sum(1 for word in pathos_words if word in text)
    logos_count = sum(1 for word in logos_words if word in text)

    # 分项打分（封顶）
    ethos_score = min(ethos_count * 5, 40)
    pathos_score = min(pathos_count * 5, 30)
    logos_score = min(logos_count * 5, 30)
    total = ethos_score + pathos_score + logos_score

    # 评级判定
    if total >= 80:
        level = "优秀：三要素完整，符合标准公关文案"
    elif total >= 60:
        level = "合格：基础要素齐全，少量优化空间"
    else:
        level = "不合格：缺少共情/责任/逻辑，需大幅修改"

    # 输出打分报告
    print("===== 公关文案修辞打分报告 =====")
    print(f"Ethos可信度得分：{ethos_score}/40  匹配关键词数量：{ethos_count}")
    print(f"Pathos情感共情得分：{pathos_score}/30  匹配关键词数量：{pathos_count}")
    print(f"Logos事实逻辑得分：{logos_score}/30  匹配关键词数量：{logos_count}")
    print(f"总分：{total}/100")
    print(f"综合评价：{level}")
    return total

# 测试示例（直接运行可测试杨国福致歉文案）
if __name__ == "__main__":
    test_text = """
    针对苏州门店卫生问题我们深表愧疚，食品安全是我们的底线。
    涉事门店立刻停业全面消杀，全国所有门店开展为期一周安全排查，
    开通24小时投诉专线接受消费者监督，对涉事顾客全额赔付。
    后续每月联合市场监管局突击检查，建立长效监管机制。
    """
    score_pr_text(test_text)
