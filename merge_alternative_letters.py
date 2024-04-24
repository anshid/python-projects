class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=""
        for i in range(max(len(word1),len(word2))):
            try:
                merged+=word1[i]
            except:
                pass
            try:
                merged+=word2[i]
            except:
                pass
        return merged
