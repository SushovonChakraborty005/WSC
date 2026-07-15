from vector_store import search


def get_context(question):

    results, scores = search(question)

    print("\n===== SEARCH RESULTS =====")

    for i, result in enumerate(results):
        print(f"Result {i+1}:")
        print(result)
        print("--------------------------")

    context = "\n\n".join(results)

    # যদি কোনো result না থাকে
    if len(scores) == 0:
        return context, 999999

    # সবচেয়ে ভালো match
    best_score = min(scores)

    print(f"Best Score : {best_score}")

    return context, best_score