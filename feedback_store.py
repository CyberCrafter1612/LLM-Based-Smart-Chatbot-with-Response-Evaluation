import json
import os

FILE_PATH = "data/feedback.json"

def save_feedback(query, response, scores):
    data = {
        "query": query,
        "response": response,
        "scores": scores
    }

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

    with open(FILE_PATH, "r+") as f:
        content = json.load(f)
        content.append(data)
        f.seek(0)
        json.dump(content, f, indent=4)
