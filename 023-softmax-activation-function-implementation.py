import math

def softmax(scores: list[float]) -> list[float]:
    exp_scores = [math.exp(x) for x in scores]
    exp_sum = sum(exp_scores)
    probabilities = [exp_score / exp_sum for exp_score in exp_scores]
    return probabilities
