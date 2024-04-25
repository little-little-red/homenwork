def calculate_usual_score_before_weighting(final_score, paper_score):
    paper_ratio = 0.7
    paper_part = paper_score * paper_ratio
    if paper_part > final_score:
        return "总成绩设定太高，无法达到."
    usual_score = (final_score - paper_part) / (1 - paper_ratio)
    return usual_score


print(calculate_usual_score_before_weighting(60, 50))
