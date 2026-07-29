# Retrieval Test Results

## Test 1

**Question**

> What is my deductible?

**Classification**

Structured (SQL)

**Retrieved Context**

- Retrieved deductible value `(2000)` from the SQL `plans` table.

**Manual Score**

✅ Good

---

## Test 2

**Question**

> What's my copay?

**Classification**

Structured (SQL)

**Retrieved Context**

- Retrieved copay value `(10)` from the SQL `plans` table.

**Manual Score**

✅ Good

---

## Test 3

**Question**

> What is my premium?

**Classification**

Structured (SQL)

**Retrieved Context**

- Retrieved premium value `(500)` from the SQL `plans` table.

**Manual Score**

✅ Good

---

## Test 4

**Question**

> Show my claim status.

**Classification**

Structured (SQL)

**Retrieved Context**

- Retrieved claim IDs and their statuses:
  - C1001 – Pending
  - C1002 – Approved
  - C1003 – Denied
  - C1004 – Approved
  - C1005 – Pending

**Manual Score**

✅ Good

---

## Test 5

**Question**

> Is physical therapy covered?

**Classification**

Unstructured (Vector)

**Retrieved Context**

- Retrieved sections discussing rehabilitation services and physical therapy.
- Also returned some unrelated exclusion and preventive care sections.

**Manual Score**

🟡 Partial

**Notes**

Relevant information was retrieved, but several returned chunks were only loosely related to physical therapy.

---

## Test 6

**Question**

> What services are excluded?

**Classification**

Unstructured (Vector)

**Retrieved Context**

- Retrieved the "Excluded Services & Other Covered Services" section.
- Included examples such as cosmetic surgery, hearing aids, dental care, long-term care, and weight loss programs.

**Manual Score**

✅ Good

---

## Test 7

**Question**

> Explain prior authorization.

**Classification**

Unstructured (Vector)

**Retrieved Context**

- Retrieved multiple policy sections mentioning prior authorization requirements.
- Retrieved examples from hospital stays, outpatient services, maternity care, and rehabilitation.

**Manual Score**

🟡 Partial

**Notes**

The retrieved context references prior authorization but does not provide a clear definition or explanation.

---

## Test 8

**Question**

> Does the plan cover emergency room visits?

**Classification**

Unstructured (Vector)

**Retrieved Context**

- Retrieved emergency room care copay information.
- Also returned outpatient surgery and excluded services sections.

**Manual Score**

🟡 Partial

**Notes**

Emergency room information was found, but additional unrelated chunks reduced retrieval precision.

---

## Test 9

**Question**

> Is my knee surgery covered after I meet my deductible?

**Classification**

Both (SQL + Vector)

**Retrieved Context**

- SQL returned deductible value `(2000)`.
- Vector search returned deductible policy information and covered services.

**Manual Score**

🟡 Partial

**Notes**

The system successfully merged SQL and vector results, but it did not retrieve information specifically about knee surgery.

---

## Test 10

**Question**

> Can I receive physical therapy after paying my deductible?

**Classification**

Both (SQL + Vector)

**Retrieved Context**

- SQL returned deductible information.
- Vector search retrieved rehabilitation and physical therapy related sections.

**Manual Score**

🟡 Partial

**Notes**

The retrieved context discusses rehabilitation and deductible information, but it does not explicitly answer whether physical therapy is covered after the deductible is met.

---

# Overall Summary

| Metric | Result |
|---------|--------|
| Total Questions | 10 |
| Structured | 4 |
| Unstructured | 4 |
| Both | 2 |
| Good | 5 |
| Partial | 5 |
| Poor | 0 |

## Observations

- The question classifier correctly routed all ten questions.
- SQL retrieval returned accurate structured information for deductible, copay, premium, and claim status.
- Vector retrieval successfully found semantically related policy sections.
- Hybrid retrieval correctly merged SQL and vector results.
- Some vector queries returned extra policy chunks that were only loosely related to the question, reducing precision.

## Improvements

- Add a reranking stage (e.g., Cohere Rerank or BGE Reranker) to improve the ordering of retrieved chunks.
- Improve chunking so that sections remain more focused.
- Add richer metadata (plan type, benefit category, coverage area) and use metadata filtering.
- Increase retrieval precision by combining semantic search with keyword (hybrid) search.
- Expand the knowledge base with additional plan documents to better answer plan-specific questions.