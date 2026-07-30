# Prompt Variants Comparison

## Variant A – Strict / Formal

### Characteristics
- Professional and policy-focused
- Answers only from retrieved context
- Quotes policy wording when available
- Refuses medical advice

### Pros
- Highly accurate
- Reduces hallucinations
- Good for compliance-sensitive environments

### Cons
- Can sound robotic
- Less conversational

---

## Variant B – Warm / Empathetic

### Characteristics
- Friendly and supportive tone
- Explains policy in simple language
- Acknowledges member concerns
- Redirects medical questions to healthcare providers

### Pros
- Better customer experience
- Easier for users to understand

### Cons
- May be slightly less formal

---

## Variant C – Few-Shot Prompting

### Characteristics
- Includes example questions and answers
- Demonstrates expected response style
- Includes an example medical disclaimer

### Pros
- Produces consistent responses
- Improves formatting and answer quality

### Cons
- Longer prompt
- Uses more tokens

---

## Variant D – Internal Verification

### Characteristics
- Instructs the model to verify retrieved context before answering
- Does not expose internal reasoning
- Returns only the final answer

### Pros
- Encourages accurate responses
- Helps reduce unsupported answers

### Cons
- Slightly longer prompt

---

## Variant E – Hybrid (Selected)

### Combines

- Formal grounding from Variant A
- Friendly tone from Variant B
- Few-shot examples from Variant C
- Internal verification from Variant D
- Standard closing disclaimer

### Advantages

- Uses only retrieved context
- Produces consistent answers
- Friendly yet professional
- Handles missing information safely
- Refuses medical advice appropriately
- Suitable for a production health insurance chatbot

---

# Selected Production Prompt

Variant E has been selected as the production system prompt because it provides the best balance of accuracy, consistency, user friendliness, and safety while remaining grounded in the retrieved policy documents.