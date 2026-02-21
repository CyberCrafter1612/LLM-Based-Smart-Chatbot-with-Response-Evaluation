def evaluate_response(query, response):
    score = {
        "accuracy": score_accuracy(query, response),
        "relevance": score_relevance(query, response),
        "clarity": score_clarity(response)
    }

    score["overall"] = round(
        (score["accuracy"] + score["relevance"] + score["clarity"]) / 3, 2
    )

    return score


def score_accuracy(query, response):
    # simple heuristic (can be replaced with LLM judge later)
    return min(len(response) / 50, 10)


def score_relevance(query, response):
    common_words = set(query.lower().split()) & set(response.lower().split())
    return min(len(common_words) * 2, 10)


def score_clarity(response):
    sentences = response.split(".")
    return min(len(sentences) * 2, 10)
