from collections import deque
## Problem
# # j1
# # j2
# # j3
#  |i1| |i2| |i3| || || ||  
#

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # create deque (both for clarity)
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        rotations_count = 0
        while (len(students) > 0) and (rotations_count < len(students)):
        
            # Check if student at front of the line likes the sandwich at top of stack
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                rotations_count = 0
                
            # Student at the front of the line gets bumped to back of the line
            else:
                front = students.popleft()
                students.append(front)
                
                # count number of times we've rotated students
                rotations_count += 1
                
        return len(students)

