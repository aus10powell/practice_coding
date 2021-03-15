# Write your MySQL query statement below
# Assumption (right now is that there are no nulls for either accepter or requester)

###########################################################
-- MINE (Doesn't work)
##########################################################
SELECT
T1.requester_id
,T2.accepter_id
,T1.num_request
,T2.num_accept
FROM
(
    SELECT requester_id, COUNT(*) as "num_request" FROM  request_accepted
    GROUP BY requester_id
) T1
INNER JOIN (
    SELECT accepter_id, COUNT(*) as "num_accept" FROM request_accepted
    GROUP BY accepter_id
) T2
WHERE T1.requester_id = T2.accepter_id
;

select ids as id, cnt as num
from
(
select ids, count(*) as cnt
   from
   (
        select requester_id as ids from request_accepted
        union all
        select accepter_id from request_accepted
    ) as tbl1
   group by ids
   ) as tbl2
order by cnt desc
limit 1
;
