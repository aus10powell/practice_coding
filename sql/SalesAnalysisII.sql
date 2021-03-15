# Write your MySQL query statement below

## Assumptions:
##    * There is only one product ID for the phones. E.g. product_id 1 is always
##    equivalent to S8
WITH S8Sales AS (
    SELECT buyer_id FROM Sales
    WHERE product_id IN
        (SELECT distinct product_id FROM Product
        WHERE product_name = 'S8')
)
,iPhoneSales AS (
    SELECT buyer_id FROM Sales
    WHERE product_id IN (
                        SELECT DISTINCT product_id FROM Product
                        WHERE product_name = 'iPhone')
)
, BothPhones AS (
SELECT S8Sales.buyer_id FROM S8Sales
    INNER JOIN iPhoneSales ON S8Sales.buyer_id = iPhoneSales.buyer_id
)

# Query for buyer_ids who bought both
SELECT distinct buyer_id FROM Sales
WHERE buyer_id IN (SELECT distinct buyer_id FROM S8Sales)
AND buyer_id NOT IN (SELECT distinct buyer_id FROM BothPhones)
