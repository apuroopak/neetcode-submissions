class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        
        for l in s:
            if l in hash_s:
                hash_s[l] += 1
            else:
                hash_s[l] = 1
            
        for l in t:
            if l in hash_t:
                hash_t[l] += 1
            else:
                hash_t[l] = 1

        return hash_s == hash_t
        