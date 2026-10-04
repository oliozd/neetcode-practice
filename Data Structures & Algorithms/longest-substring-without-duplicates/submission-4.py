class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        curr_sub = []
        curr_set = set()
        max_len = 0
        curr_len = 0
        lp = 0
        for rp, char in enumerate(s):

            while char in curr_set:
                curr_set.remove(s[lp])
                lp += 1

            curr_set.add(char)
            curr_len = rp - lp + 1
            max_len = max(max_len, curr_len)
        
        return max_len



        