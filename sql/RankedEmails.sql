## Edge-Cases
-- Nulls

## Approach

# Write your MySQL query statement below
WITH RANKED AS
(
    SELECT email
    ,id
    ,RANK() OVER (PARTITION BY email order by id) as email_rank
    FROM Person
)

SELECT distinct email from Ranked
WHERE email_rank >= 2
