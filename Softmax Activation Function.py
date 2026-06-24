import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    pass
    max_score = max(scores)
    result = []
    for i in scores:
        result.append(math.exp(i - max_score))  
    
    sum_all = sum(result)

    final = []
    for j in result:
        probability_dist = round( j / sum_all, 4)
        final.append(probability_dist)

    return final
