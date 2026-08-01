import json
from openai import OpenAI
from tool_schemas import tools

from tool_functions import (
    check_coverage,
    get_claim_status,
    get_plan_details,
    estimate_out_of_pocket_cost
)

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

SYSTEM_PROMPT = """
You are a professional and supportive health insurance assistant.
Answer only using the provided tool results.
"""

question = "Is physical therapy covered under the Silver plan?"

# REAL API CALL
response = client.chat.completions.create(
    model="qwen2.5-coder:3b",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ],
    tools=tools
)

# Parse tool request
tool_request = json.loads(response.choices[0].message.content)

tool_name = tool_request["name"]
arguments = tool_request["arguments"]

print(tool_name)
print(arguments)

# Execute tool
if tool_name == "check_coverage":
    tool_result = check_coverage(**arguments)

elif tool_name == "get_claim_status":
    tool_result = get_claim_status(**arguments)

elif tool_name == "get_plan_details":
    tool_result = get_plan_details(**arguments)

elif tool_name == "estimate_out_of_pocket_cost":
    tool_result = estimate_out_of_pocket_cost(**arguments)

print(tool_result)