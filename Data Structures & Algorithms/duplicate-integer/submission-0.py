class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for ele in nums:
            if ele in sett:
                return True
            else:
                sett.add(ele)
        return False           