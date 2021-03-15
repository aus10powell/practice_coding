# Write your MySQL query statement below

# Edge-cases:
# - No ads


## Approach 1
# - Create a table sum up click
# - Create 2nd table and join to first

With views As
(Select ad_id
 ,sum(case when action='Viewed' then 1 else 0 end) as total_views
 FROM ads
 Group By ad_id
)
, clicks As 
(
Select ad_id
 ,Sum(Case When action='Clicked' Then 1 Else 0 end) as total_clicks
 FROM ads
 Group By ad_id
)
,combined AS (
SELECT A.total_views, B.* FROM views A
LEFT JOIN clicks B on A.ad_id = B.ad_id
)

SELECT 
ad_id
,CASE
    WHEN total_clicks + total_views = 0 THEN 0.00
    ELSE round(total_clicks / (total_clicks + total_views) * 100.0,2)
END AS ctr
FROM combined
ORDER BY CTR DESC, ad_id ASC




