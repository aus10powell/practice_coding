class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # a place to store keyed anagram strings
        str_hash = {}

        for key,s in enumerate(strs):
            anagram = ''.join(sorted(s))
            if key == 0:
                str_hash[anagram] = [s]
            else:
                if anagram in str_hash.keys():
                    str_hash[anagram].append(s)
                else:
                    pass
                    str_hash[anagram] = [s]


        return [v for k,v in str_hash.items()]
