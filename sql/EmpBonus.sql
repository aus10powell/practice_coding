##########################################################
#
#
# 84% solution
##########################################################
SELECT A.name, B.bonus FROM Employee A
LEFT JOIN Bonus B ON A.empID=B.empID -- Need left join because the employee may not have a bonus
WHERE B.bonus < 1000
OR B.bonus IS NULL -- Possible that they don't have bonus but it is still entered
