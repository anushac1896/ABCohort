
What is my deductible?
structured
--------------------------------------------------
Is physical therapy covered?
unstructured
--------------------------------------------------
Show my claim status
structured
--------------------------------------------------
Is my knee surgery covered after I meet my deductible?
both
--------------------------------------------------
Explain prior authorization
unstructured
--------------------------------------------------
[(2000,)]
(.venv) anushachennu@anushas-MacBook-Air ABCohort % /Users/anushachennu/projects/coverage-chatbot-api/.venv/bin/python /Users/anushachennu/projects/cov
erage-chatbot-api/ABCohort/test_rag.py
What is my deductible?
structured
--------------------------------------------------
Is physical therapy covered?
unstructured
--------------------------------------------------
Show my claim status
structured
--------------------------------------------------
Is my knee surgery covered after I meet my deductible?
both
--------------------------------------------------
Explain prior authorization
unstructured
--------------------------------------------------
[(2000,)]
================================================================================
TEST 1
================================================================================
Question: What is my deductible?

Route selected: structured
Final Answer:
Based on the information provided in the SQL results (2000), it appears that your deductible amount is 2000. However, I don't have any additional context to confirm or explain what this deduction might refer to in a specific insurance policy or financial context without further details from the member. If you need clarification on how this applies to your situation or if there's more information available, it would be best for the member to contact support for a detailed explanation.

================================================================================
TEST 2
================================================================================
Question: What's my copay?

Route selected: structured
Final Answer:
I don't have enough information from the provided context to determine what your copay is. Please contact a healthcare professional for accurate advice regarding your insurance coverage and payments.

================================================================================
TEST 3
================================================================================
Question: What is my premium?

Route selected: structured
Final Answer:
Based on the given context, there is no information provided about your premium. Please contact customer service for assistance with that matter.

================================================================================
TEST 4
================================================================================
Question: Show my claim status.

Route selected: structured
Final Answer:
According to the SQL results provided, here are the current claim statuses:

- C1001: Pending
- C1002: Approved
- C1003: Denied
- C1004: Approved
- C1005: Pending

Each claim has a status of either "Pending," "Approved," or "Denied."

================================================================================
TEST 5
================================================================================
Question: Is physical therapy covered?

Route selected: unstructured
Final Answer:
Yes, physical therapy is covered by the plan. The policy states that "Rehabilitation services (physical therapy) may apply." However, there are specific limitations: 60 visits/condition per year combined with physical and speech therapy, and no charge for outpatient. It's important to ask your provider if the services needed are preventive to determine what coverage will be applied.

================================================================================
TEST 6
================================================================================
Question: What services are excluded?

Route selected: unstructured
Final Answer:
The excluded services in this plan include:

• Acupuncture
• Glasses (Child)
• Non-emergency care when traveling outside the U.S.
• Cosmetic surgery
• Hearing aids
• Routine foot care
• Dental care (Adult & Child)
• Long-term care
• Weight loss programs

These services are not covered by the insurance plan and do not have a copayment or coinsurance.

================================================================================
TEST 7
================================================================================
Question: Explain prior authorization.

Route selected: unstructured
Final Answer:
Prior authorization is required when a medical treatment or service requires approval from the insurance provider before it can be covered. This ensures that only necessary and medically appropriate treatments are paid for. Prior authorization may include requirements such as referrals to specialists, pre-examinations, or obtaining a prescription from a doctor. Without prior authorization, the cost of the treatment may not be covered by the insurance plan.

================================================================================
TEST 8
================================================================================
Question: Does the plan cover emergency room visits?

Route selected: unstructured
Final Answer:
Yes, the plan covers emergency room visits. They are classified as out-of-network emergency use and will be paid at the same rate as inpatient emergency care, which includes a $100 copay/visit.

================================================================================
TEST 9
================================================================================
Question: Is my knee surgery covered after I meet my deductible?

Route selected: both
Final Answer:
Yes, your knee surgery would be covered after you meet your deductible.

================================================================================
TEST 10
================================================================================
Question: Can I receive physical therapy after paying my deductible?

Route selected: both
Final Answer:
Yes, you can receive physical therapy after paying your deductible. The policy covers physical therapy services up to a copay of $40 per visit.

