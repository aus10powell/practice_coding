## Approach:
# - 1) Sort boxes in order from those containing largest units, to the least
# - 2) Use double for loop to 

## Questions
# Are the box unit sizes pre-sorted?

# 

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # sort by number of units per box
        boxTypes.sort(key=lambda x: x[1], reverse=True) 

        num_units = 0
        total_boxes = 0
        for i in range(len(boxTypes)):
            
            # Two conditions to keep adding boxes
            # 1) The next boxtype has to have at least one box left
            # 2) The number boxes is not already at the limit
            
            num_boxes = boxTypes[i][0]
            while (num_boxes > 0) and (total_boxes < truckSize ):

                num_units += boxTypes[i][1]
                total_boxes += 1
                
                num_boxes -= 1

        return num_units
                
        
        


