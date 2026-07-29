from question_classifier import classify_question
from sql_lookup import sql_lookup
from vector_lookup import vector_lookup


def retrieve(question):
    """
    Route the question to SQL, Vector DB, or both.
    Merge and de-duplicate the retrieved context.
    """

    route = classify_question(question)

    context = []

    print(f"Route selected: {route}")

    # ----------------------------------
    # Structured (SQL)
    # ----------------------------------
    if route == "structured":

        sql_results = sql_lookup(question)

        if sql_results:
            context.append("=== SQL RESULTS ===")

            for row in sql_results:
                context.append(str(row))

    # ----------------------------------
    # Unstructured (Vector)
    # ----------------------------------
    elif route == "unstructured":

        vector_results = vector_lookup(question)

        docs = vector_results["documents"][0]

        context.append("=== POLICY DOCUMENTS ===")

        for doc in docs:
            context.append(doc)

    # ----------------------------------
    # Both
    # ----------------------------------
    elif route == "both":

        sql_results = sql_lookup(question)

        vector_results = vector_lookup(question)

        if sql_results:

            context.append("=== SQL RESULTS ===")

            for row in sql_results:
                context.append(str(row))

        docs = vector_results["documents"][0]

        context.append("=== POLICY DOCUMENTS ===")

        for doc in docs:
            context.append(doc)

    # ----------------------------------
    # Remove duplicates
    # ----------------------------------
    unique_context = []

    seen = set()

    for item in context:

        if item not in seen:
            unique_context.append(item)
            seen.add(item)

    return "\n\n".join(unique_context)


# ----------------------------------
# Test
# ----------------------------------
if __name__ == "__main__":

    question = "Is my knee surgery covered after I meet my deductible?"

    context = retrieve(question)

    print("\n")
    print("=" * 80)
    print("FINAL CONTEXT")
    print("=" * 80)
    print(context)