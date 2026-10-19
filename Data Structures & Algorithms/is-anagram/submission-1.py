class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict = {}
        for ele in s:
            if ele not in s_dict.keys():
                s_dict[ele] = 1
            else:
                s_dict[ele]+=1    
        for ele in t:
            if ele in s_dict.keys():
                if s_dict[ele]==1:
                    del s_dict[ele]
                else:
                    s_dict[ele]-=1    
            else:
                return False
        return True        
