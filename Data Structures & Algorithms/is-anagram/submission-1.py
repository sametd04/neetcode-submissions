class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 0
        t_dict = dict()
        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 0
        for (key,val) in s_dict.items():
            if not(key in t_dict and t_dict[key] == val):
                return False
        for (key,val) in t_dict.items():
            if not(key in s_dict and s_dict[key] == val):
                return False
        return True
        