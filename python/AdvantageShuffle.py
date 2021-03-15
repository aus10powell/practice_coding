import itertools

## Approach:

## Edge-cases
# - A's arrangement already qualifies
# - There is no arrangemento for A that qualifies

## Discussion:
"""
- Brute force would be to find all permutations of A and test against B
- Is it alright to use a library for permutations?
- Can we assume that there is always going to be a solution?
"""

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        
        def count_advantage(A,B):
            counts = 0
            for idx in range(len(B)):
                if A[idx] > B[idx]:
                    counts += 1
            return counts
        
        
        perms = itertools.permutations(A,r=len(A)) 
        
        answer = A
        best_count = count_advantage(A=A,B=B)
        
        for p in perms:
            current_count = count_advantage(A=p,B=B)
            if current_count > best_count:
                best_count = current_count
                answer = list(p)
                
        return answer
        
class Solution(object):
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]
