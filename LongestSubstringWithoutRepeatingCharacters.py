"""
In this problem I have learnt about the sliding window technique which is used to solve the problems in sequences with ease.

Also when don't want duplicates we should use a set instead of a list.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s:str) -> int:
        # if len(s) == 0:
        #     return 0
        # if len(s) == 1:
        #     return 1
        
        # arr =[]
        # lendict = {}
        
        # for i in range(len(s)):
        #     if s[i] not in arr:
        #         if i == len(s)-1:
        #             arr.append(s[i])
        #             temp_str = ''.join(arr)
        #             lendict[temp_str] = len(temp_str)
        #             arr = []
        #         arr.append(s[i])
                
        #     else:
        #         temp_str = ''.join(arr)
        #         lendict[temp_str] = len(temp_str)
        #         arr = []
        #         arr.append(s[i])
        
        # for _,v in lendict.items():
        #     if v == max(lendict.values()):
        #         return v
        
        l = 0 #left pointer
        longest = 0 #longest substring
        charSet =set()
        n = len(s)
        
        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            w = r-l+1
            longest = max(longest, w)
            charSet.add(s[r])
        return longest
        
#example usage
s = "dvdf"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))