## Assumptions/Edge Cases
#  - Nulls:
#    - No product ids. Assuming returning nulls

# Write your MySQL query statement below

WITH joined AS (
                SELECT A.*,B.name FROM Invoice A
                LEFT JOIN Product B ON A.product_id=B.product_id
                )
SELECT name
        ,SUM(rest) AS rest
        ,SUM(paid) AS paid
        ,SUM(canceled) AS canceled
        ,SUM(refunded) AS refunded
        FROM joined
        GROUP BY product_id
        ORDER BY name
