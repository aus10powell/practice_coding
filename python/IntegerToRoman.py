import math
######### Convert integer to Roman
# Approach:
# - Write Int to Roman Character dict
# - Iterate through the digits in the input with a while loop

T = {1000:'M',500:'D',100:"C",50:"L",5:"V",1:"I"}

def IntToRoman(num):
    num = int(num)
    keys = list(T.keys())
    keys.sort(reverse=True)


    RomanNumber = ''
    print(num)
    while num > 0:
        #print(num)
        for idx in range(len(keys)):
            if num / keys[idx] >= 1.0:
                if (idx != 0) and num / (keys[idx-1] - keys[idx]) >= 1:
                    if (keys[idx-1] - keys[idx]) != keys[idx]:
                        pass
                    else:
                        ns = math.floor(num/keys[idx])
                        num = num - ns * keys[idx]
                        RomanNumber += T[keys[idx]] * ns
                        print(RomanNumber,num)
                else:
                    pass
            else:
                    ns = math.floor(num/keys[idx])
                    num = num - ns* keys[idx]
                    RomanNumber += T[keys[idx]] * ns
                    print(RomanNumber,num)
    return RomanNumber


if __name__ == '__main__':
    print('Answer: ',IntToRoman(254))
    print(IntToRoman(100))
