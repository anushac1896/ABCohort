# Fine-Tuning Preparation Notes

## 1. Missing required disclaimers

**Classification:** Fine-tuning candidate.  
**Why:** This is a response-consistency problem. Training examples can reinforce a short reminder that exact coverage and costs depend on the member's plan.

## 2. Inconsistent tone for sensitive questions

**Classification:** Fine-tuning candidate.  
**Why:** Responses to denials, bills, and care concerns should be empathetic, plain-language, and action-oriented. Ideal examples teach that communication pattern.

## 3. Wrong or unavailable plan-specific details

**Classification:** Retrieval problem.  
**Why:** Deductibles, copays, network participation, coverage rules, and claim status are current, member- and plan-specific facts. Fine-tuning cannot reliably supply them; the chatbot must retrieve them from an approved, current source.

## FT vs Retrieval

**Fine-tuning (FT)** improves how the chatbot responds. It can help with consistent empathetic tone, plain-language explanations, correct insurance terminology, and required disclaimer use.

**Retrieval** provides current, plan-specific facts. It is needed for deductibles, copays, coinsurance, provider network status, prior-authorization rules, claim status, and coverage details.

Fine-tuning cannot fix retrieval problems. If the chatbot gives an incorrect plan-specific answer, the fix is to improve the benefits data source, retrieval accuracy, or data freshness—not to add that fact to the fine-tuning dataset.
## Conclusion

Fine-tuning improves how the chatbot communicates: tone, terminology, explanations, and disclaimer use. Retrieval supplies what the chatbot needs to know now: plan benefits, provider network status, authorizations, and claims information.
