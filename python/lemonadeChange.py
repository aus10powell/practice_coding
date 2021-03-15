#######################################################
# Best Solution O(n)
#######################################################
def lemonadeChange(self, bills):
	five=ten=0
	for i in bills:
	  if i==5: five+=1
	  elif i==10: five,ten = five-1, ten+1
	  elif ten>0: five,ten = five-1, ten-1
	  else: five-=3
	  if five<0: return False
	return True
    
#######################################################
# Mine: Faster than 18%
#######################################################

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        # Starting cash reserves
        cash_on_hand = {5:0,10:0,20:0}

        # Response to return
        answer = True

        # Iterate through customers
        for idx, bill in enumerate(bills):
            print(bill)

            if bill == 5:
                cash_on_hand[bill] += 1

            # Bill is either a $10 or a $20 bill
            else:
                # Won't have enough cash on hand
                if idx == 0:
                    answer = False
                    break
                else:
                    if cash_on_hand[5] > 0:
                        if bill == 10:
                            cash_on_hand[5] -= 1
                            cash_on_hand[10] += 1
                            # Assum that the only other option is a $20 bill
                        else:
                            if cash_on_hand[10] > 0:
                                cash_on_hand[5] -= 1
                                cash_on_hand[10] -= 1
                                cash_on_hand[20] += 1
                            elif cash_on_hand[5] >=3:
                                cash_on_hand[5] -= 3
                                cash_on_hand[20] += 1
                            else:
                                answer = False
                                break
                    else:
                        answer = False
                        break
            print(cash_on_hand)
        return answer
