WITH kids AS 
(
    SELECT * FROM Content
    WHERE kids_content = 'Y'
    and content_type='Movies'
)
, dates AS
(
SELECT * FROM TVProgram
    WHERE MONTH(program_date) = 6 AND YEAR(program_date) = 2020
)

SELECT distinct  A.title AS TITLE  From kids A
INNER JOIN dates B ON A.content_id = B.content_id
WHERE A.title is not null
