# Fine-Tune Comparison

## Evaluation method

I evaluated the base model and LoRA fine-tuned model using the same five held-out questions from `fine_tune_test.jsonl`. The held-out examples were not used during training.

Scores use a 1–5 scale, where 5 is best.

- **Tone:** empathetic, calm, and helpful.
- **Correctness:** accurate general coverage guidance without invented plan facts.
- **Disclaimer usage:** acknowledges that plan-specific benefits and costs can vary.
- **Terminology clarity:** insurance language is explained plainly.

## Question 1: What if I received care before my coverage started?

| Criterion | Base model | LoRA model | Notes |
|---|---:|---:|---|
| Tone | 2 | 1 | The base answer is generic; the LoRA answer contains only exclamation marks. |
| Correctness | 1 | 1 | The base answer does not clearly explain that services before the effective date may not be covered. |
| Disclaimer usage | 1 | 1 | Neither gives an appropriate plan-specific coverage disclaimer. |
| Terminology clarity | 2 | 1 | The base answer is understandable but unfocused; the LoRA answer is unusable. |

## Question 2: How long does a claim take to process?

| Criterion | Base model | LoRA model | Notes |
|---|---:|---:|---|
| Tone | 2 | 1 | The base answer is neutral but not especially supportive. |
| Correctness | 1 | 1 | The base answer gives unsupported processing-time claims, including “within 24 hours.” |
| Disclaimer usage | 1 | 1 | Neither appropriately directs the user to current claim status or member services. |
| Terminology clarity | 2 | 1 | The base answer uses a numbered list but includes confusing and unsupported details. |

## Question 3: Can someone help me understand my benefits?

| Criterion | Base model | LoRA model | Notes |
|---|---:|---:|---|
| Tone | 2 | 1 | The base answer is polite but does not provide a clear next step. |
| Correctness | 2 | 1 | The base answer lists general insurance concepts, but it does not answer how the user can get help with their specific benefits. |
| Disclaimer usage | 1 | 1 | Neither clearly states that current benefit details depend on the plan. |
| Terminology clarity | 2 | 1 | The base answer explains some terms but is not focused on the user’s question. |

## Question 4: What is a coverage determination?

| Criterion | Base model | LoRA model | Notes |
|---|---:|---:|---|
| Tone | 1 | 1 | Neither response provides helpful, user-centered communication. |
| Correctness | 2 | 1 | The base answer partially describes an insurance decision, but includes inaccurate concepts such as compensation and maximum liability. |
| Disclaimer usage | 1 | 1 | Neither response appropriately explains that the decision depends on plan rules and medical information. |
| Terminology clarity | 2 | 1 | The base answer is lengthy and uses confusing language; the LoRA output is unusable. |

## Question 5: What should I do if I cannot afford my prescription?

| Criterion | Base model | LoRA model | Notes |
|---|---:|---:|---|
| Tone | 2 | 1 | The base answer is somewhat supportive; the LoRA output is unusable. |
| Correctness | 3 | 1 | The base answer suggests reviewing coverage, contacting the insurer, and exploring assistance programs. |
| Disclaimer usage | 1 | 1 | The base answer does not clearly state that prescription coverage and costs depend on the user’s plan. |
| Terminology clarity | 3 | 1 | The base answer is generally understandable but cuts off before giving a complete response. |

## Conclusion

The LoRA fine-tuned model did not meaningfully improve consistency in this experiment. Although training completed successfully, the fine-tuned adapter generated only exclamation marks for every held-out question. This is a failed fine-tuning result and should not be used in a coverage chatbot.

The base model produced readable responses, but several were generic, incomplete, or factually unreliable. It also frequently missed the desired disclaimer and did not consistently explain insurance terms clearly.

For this use case, stronger prompting and retrieval would provide more value with less effort than this fine-tuning run. Retrieval remains necessary for current plan-specific facts such as copays, deductibles, network status, claim status, and coverage rules. A future LoRA attempt would need debugging and revised training settings before it could be evaluated as a useful improvement.