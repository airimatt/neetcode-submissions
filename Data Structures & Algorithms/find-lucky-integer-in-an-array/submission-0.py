class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        freqMap = defaultdict(int)
        for n in arr:
            freqMap[n] += 1
        
        res = -1
        for n, freq in freqMap.items():
            if freq == n:
                res = max(res, n)
            
        return res if res != -1 else -1