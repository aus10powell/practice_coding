################################################################################
# TopThreeSalaries
# Focuses on clarity of Query
################################################################################

###############
# My Solution
# Beats 88% of the submissions
###############
# Write your MySQL query statement below
With customTable AS
-- assumptions: Therea is a Department name for each Department ID in the Employee Table
(
    SELECT D.Name AS Department
    ,E.Name As Employee
    ,E.Salary
    FROM Employee E
    LEFT JOIN Department D ON D.ID = E.DepartmentId
    ORDER BY D.Name, E.Salary
)

SELECT FinalTable.Department
,FinalTable.Employee
,FinalTable.Salary
 FROM (
    SELECT *
    ,DENSE_RANK() OVER (Partition by C.Department ORDER BY Salary DESC) AS SalaryRank
    FROM customTable C
) FinalTable
WHERE SalaryRank <= 3
AND Department IS NOT NULL
ORDER BY Department, Salary

##############
# Provided Solution
# Faster than 19% of the queries
##############
# Write your MySQL query statement below

#############
# Inner query
#############
SELECT
e1.Name AS 'Employee'
,d.Name AS 'Department'
,e1.Salary
FROM Employee e1
JOIN Department D ON D.Id = e1.DepartmentId
WHERE 3 > (
           SELECT COUNT(DISTINCT e2.Salary)
           FROM Employee e2
           WHERE e2.Salary > e1.Salary --
           AND e1.DepartmentId = e2.DepartmentId
          );
