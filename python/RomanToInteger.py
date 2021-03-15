class Solution:
    mapper = {'I':1,'V':5,'X':10, 'L':50,'C':100,'D':500,'M':1000}
    def romanToInt(self, s: str) -> int:


        # convert to characters for checks
        chars = [c for c in s if c in mapper.keys()]

        del s # conserve memory

        # assertion to satisfy constraints
        assert len(chars) >= 1 and len(chars) <= 15

        answer = []
        idx = 0
        while idx < len(chars) - 1:
            if mapper[chars[idx]] < mapper[chars[idx + 1]]:
                answer.append(mapper[chars[idx + 1]] - mapper[chars[idx]])
                idx += 2
            else:
                answer.append(mapper[chars[idx]])
                idx += 1

        if idx == len(chars) - 1:
            answer.append(mapper[chars[idx]])

        return sum(answer)


def main():
    s = Solution()
    user_input = input("Please enter a roman numeral: \n")

    print('You entered: {}'.format(user_input))
    try:
        assert [s in s.mapper.keys() for s in user_input]
        solution = s.romanToInt(user_input)
    except (AttributeError, TypeError):
        raise AssertionError('Input variables should be strings')

    print(solution)


if __name__ == '__main__':
    main()
