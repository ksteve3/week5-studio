"""Working but repetitive FAQ search. Refactor this file only.
The vectors are word counts, NOT learned semantic embeddings.
"""
import math

FAQS = [
    {"id": "password", "text": "Reset your password using the account portal."},
    {"id": "expenses", "text": "Submit travel expenses with a receipt."},
    {"id": "leave", "text": "Request vacation leave through your manager."},
]
VOCAB = ["password", "account", "travel", "expenses", "receipt", "vacation", "leave", "manager"]


def text_to_vector(text):
    """Return word counts for text in the original VOCAB order."""
    cleaned = text.strip().lower().replace("?", "").replace(".", "")
    return [cleaned.split().count(word) for word in VOCAB]


def cosine_similarity(first_vector, second_vector):
    """Return the cosine similarity of two word-count vectors.

    Returns 0.0 if either vector is all zeros.
    """
    dot = 0.0
    first_norm = 0.0
    second_norm = 0.0
    for i in range(len(first_vector)):
        dot += first_vector[i] * second_vector[i]
        first_norm += first_vector[i] ** 2
        second_norm += second_vector[i] ** 2
    if first_norm == 0 or second_norm == 0:
        return 0.0
    return dot / (math.sqrt(first_norm) * math.sqrt(second_norm))


def search(query):
    qv = text_to_vector(query)
    results = []
    for item in FAQS:
        v = text_to_vector(item["text"])
        score = cosine_similarity(qv, v)
        results.append({"id": item["id"], "score": score})
    best = results[0]
    for row in results:
        if row["score"] > best["score"]:
            best = row
    return {"id": best["id"], "score": best["score"], "scores": results}


def compare_texts(first, second):
    av = text_to_vector(first)
    bv = text_to_vector(second)
    return cosine_similarity(av, bv)


if __name__ == "__main__":
    result = search("How do I reset my password?")
    for row in result["scores"]:
        print(row["id"], round(row["score"], 4))
    print("Selected FAQ:", result["id"])
