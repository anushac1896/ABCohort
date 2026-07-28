# Vector Query Test

## Query

**Question:**

> Is physical therapy covered under the Silver plan?

---

## Retrieved Chunks Review

| Rank | Relevant? | Silver Plan Specific? | Notes |
|------|-----------|-----------------------|-------|
| 1 | Partially | No | Discusses excluded services but does not mention physical therapy or the Silver plan. |
| 2 | No | No | Discusses Minimum Value Standards and Marketplace information, unrelated to physical therapy. |
| 3 | Yes (Partially) | No | Mentions chiropractic care combined with physical and speech therapy limits, but does not answer whether physical therapy is covered under a Silver plan. |
| 4 | No | No | Discusses Minimum Essential Coverage, not physical therapy. |
| 5 | No | No | General summary of plan coverage and definitions, not related to physical therapy. |

---

## Retrieval Quality

The retriever returned documents that are generally related to health insurance coverage, but most of the retrieved chunks do **not directly answer** the user's question.

Only **Rank 3** is partially relevant because it mentions physical therapy, but it still does not state whether physical therapy is covered under the Silver plan.

---

## Silver Plan Verification

The retrieved documents are **not Silver-plan-specific**.

The knowledge base contains information from an HMO Summary of Benefits document rather than a Silver plan. Therefore, the retriever cannot return an exact answer for a Silver plan because that information is not present in the indexed documents.

---

## Retrieval Misses

The retrieval test revealed several limitations:

- The knowledge base does not contain a Silver plan document.
- The retrieved chunks are mostly general insurance information rather than answers about physical therapy.
- Metadata filtering by `plan_type` is not currently possible because all records have `"plan_type": "Unknown"`.
- More accurate results could be achieved by indexing multiple insurance plans and storing the correct `plan_type` metadata for each document.

---

## Overall Assessment

**Retrieval Quality: Fair**

The vector search successfully returned semantically related insurance content, demonstrating that the embeddings and ChromaDB retrieval are functioning correctly. However, it could not answer the question accurately because the requested information (Silver plan coverage for physical therapy) does not exist in the current knowledge base.

Future improvements include:
- Indexing multiple insurance plans (Silver, Gold, Bronze, etc.).
- Storing the correct `plan_type` metadata.
- Using metadata filters during retrieval to search only within the requested plan.
- Improving chunking and section detection for more precise retrieval.

---

## Metadata Filtering Test

A second retrieval test was performed using the metadata filter:

```python
where={"plan_type": "Silver"}
```

### Result

No documents were returned.

### Reason

All indexed records currently have:

```json
"plan_type": "Unknown"
```

Since there are no documents with `plan_type = "Silver"`, the metadata filter correctly excluded every record.

### Comparison

| Query Type | Results |
|------------|---------|
| Unfiltered | Returned 5 semantically similar insurance chunks |
| Filtered (`plan_type = Silver`) | Returned 0 documents |

### Conclusion

The metadata filtering functionality works correctly. However, the current knowledge base does not contain Silver plan documents. To support plan-specific retrieval, the ingestion pipeline should populate the `plan_type` field with the actual plan name (for example, Silver, Gold, Bronze, or Standard HMO).