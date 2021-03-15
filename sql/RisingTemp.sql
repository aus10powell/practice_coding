Write an SQL query to find all dates' id with higher temperature compared to its previous dates (yesterday).

WITH
lagged AS (
    SELECT *
    , LAG(temperature,1) OVER (ORDER BY recordDate) AS temp_lag1
    , Lag(recordDate,1) OVER (ORDER BY recordDate) as date_lag1
    FROM Weather
    ORDER BY recordDate
    )

SELECT id from lagged
WHERE temp_lag1 < temperature
AND datediff(recordDate,date_lag1) = 1
