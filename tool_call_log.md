======================================================================
TEST 1
======================================================================
Question:
Is physical therapy covered under the Silver plan?

Model Response:
{"name": "check_coverage", "arguments": {"plan_id": "Silver", "procedure": "Physical Therapy"}}

======================================================================
TEST 2
======================================================================
Question:
What is the status of claim C1002?

Model Response:
{"name":"get_claim_status","arguments":{"claim_id":"C1002"}}

======================================================================
TEST 3
======================================================================
Question:
What is my deductible for the Silver plan?

Model Response:
{ functionName: get_plan_details, arguments: { plan_id: "Silver" } }

======================================================================
TEST 4
======================================================================
Question:
Estimate my out-of-pocket cost for an MRI under the Gold plan.

Model Response:
```json
{
  "name": "estimate_out_of_pocket_cost",
  "arguments": {
    "procedure": "MRI",
    "plan_id": "Gold"
  }
}
```

======================================================================
TEST 5
======================================================================
Question:
Is knee replacement covered under the Bronze plan?

Model Response:
{"function": "check_coverage", "arguments": {"plan_id":"Bronze","procedure":"Knee replacement"}}

======================================================================
TEST 6
======================================================================
Question:
Hello, how are you today?

Model Response:
I am an AI language model and do not have feelings, but I am here to help with your queries. How can I assist you today?

