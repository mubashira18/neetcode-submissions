class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for ele in s:
            if ele not in s_dict.keys():
                s_dict[ele] = 1
            else:
                s_dict[ele]+=1
        for ele in t:
            if ele not in t_dict.keys():
                t_dict[ele] = 1
            else:
                t_dict[ele]+=1                
        if dict(sorted(s_dict.items())) == dict(sorted(t_dict.items())) :
            return True
        else:
            return False           