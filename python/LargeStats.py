## Notes/Assumptions:
# - Each "count" list is 255 long
# - min and max are easy since 
# - We're not counting the 0s
# - Challenge is getting the 
# - Round mean to 10^-5

## Edge-cases:
# - No nans
# - list is made up of all 0s
# - the median is betwen one number and the other

## Approach 
# - Turn the list into a dictionary where the keys are the "k"
# - Iterate through dictionary in order to calculate stats 


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        
        # Turn into dictionary
        counts_dict = {}
        for idx in range(len(count)):
            if count[idx] != 0: counts_dict[idx] = count[idx]
            else: pass
        
        minimum = 255
        maximum = 0
        mean = 0 
        median = 0
        
        
        mode = 0
        num_mode = 0
        
        total = 0
        N = 0
        
        # k - is the number itself
        # v - is how many times k appears
        
        ## For the median
        counts_dict_sorted = sorted(counts_dict.items(), key = lambda kv: kv[1])
        counts_dict_sorted = dict(counts_dict_sorted)

        for k,v in counts_dict_sorted.items():
            total += k*v
            N += v    
            
        
        if N % 2 == 0:
            is_even = True
        else:
            is_even = False
            
        middle_idx = int(round(N/2))

            
        # count for the middle
        v_cumsum = 0
        first_pass = True
        median_final = False
        for k,v in counts_dict_sorted.items():
            k_new = k
            if first_pass:
                k_old = k_new
                first_pass = False
            

            if (v_cumsum + v) == middle_idx:
                
                if is_even:
                    median = round((k_new + k_old)/2,5)     
                    median_final = True
                else:
                    median = round(k,5)
            else:
                median = round(k,5)
            
            v_cumsum += v
            
            # Min and maxium
            if k < minimum:
                minimum = k
            if k > maximum:
                maximum = k
                
            # mode
            if v > num_mode:
                mode = k
            
            k_old = k_new
            
        # calculate mean (TBD)
        mean = round(total/N*1.0,5)
        

            
        
        return [minimum, maximum, mean, median, mode]
