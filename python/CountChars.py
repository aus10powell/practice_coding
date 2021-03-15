class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        def check_word(word,chars):
            
            chars = list(chars)
            for char in word:
                if char in chars:
                    chars.remove(char)
                else:
                    return 0
                
            # if end of loop reached then it is a success
            return len(word)
        
        # Iterate through words to check
        chars_count = 0
        for word in words:
            chars_count += check_word(word=word,chars=chars)
        
        return chars_count

