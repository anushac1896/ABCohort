# Structured SQL Queries

## Query 1: What's the deductible on the Gold PPO plan?

### SQL


query = """
SELECT annual_deductible
FROM plans
WHERE plan_name = 'Gold PPO';
"""
pd.read_sql(query, conn)

### Output
annual_deductible
0	2000

### query2 Which plans have a monthly premium under $400?
query = """
SELECT plan_name,monthly_premium 
FROM plans 
WHERE monthly_premium<400
"""
pd.read_sql(query, conn)
### o/p
plan_name	monthly_premium
0	Silver HMO	300
1	Bronze HMO	150

### A JOIN between claims and plans - 
query = """
SELECT
    c.claim_id,
    p.plan_name,
    c.claim_amount
FROM claims AS c
JOIN plans AS p
ON c.plan_id = p.plan_id;
"""

pd.read_sql(query, conn)

### o/p
claim_id	plan_name	claim_amount
0	C1001	Gold PPO	250
1	C1002	Gold PPO	1200
2	C1003	Silver HMO	150
3	C1004	Silver HMO	900
4	C1005	Bronze HMO	50


### A top-N query - Which procedures are claimed the most?

query= """
SELECT
    procedure,
    COUNT(*) AS total_claims
FROM claims
GROUP BY procedure
ORDER BY total_claims DESC
LIMIT 5;
"""

pd.read_sql(query, conn)

### o/p

procedure	total_claims
0	X-ray	3
1	Surgery	2

