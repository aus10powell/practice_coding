##########################################################
# Runtime: 916 ms, faster than 78.64% of MySQL online submissions for Sales Analysis I
# Solution: Mine
##########################################################

WITH MaxSales AS (
    SELECT seller_id, SUM(price) AS total_sales FROM Sales
    GROUP BY seller_id
    ORDER BY total_sales DESC
    LIMIT 1
)


SELECT seller_id FROM (
    SELECT seller_id, SUM(price) AS total_sales FROM Sales
    GROUP BY seller_id
    HAVING total_sales IN (
                          SELECT total_sales FROM MaxSales
                          )
) T
