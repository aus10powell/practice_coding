## Assumptions/Edge Cases
# - No negative numbers
# - Unique numbers in list (no multiples of min/max)

## Approach
# - Don't use Python libraries

## My Solution:  Beats 90.92% of Python3 online 

class Solution:
    def average(self, salary: List[int]) -> float:

        # min salary
        min_salary = None
        # max salary
        max_salary = None

        for idx in range(len(salary)):
            if idx == 0:
                min_salary = max_salary = salary[idx]
                continue

            if salary[idx] < min_salary:
                min_salary = salary[idx]

            elif salary[idx] > max_salary:
                max_salary = salary[idx]

            else:
                continue


        salary.remove(min_salary)
        salary.remove(max_salary)

        return sum(salary) / len(salary)
