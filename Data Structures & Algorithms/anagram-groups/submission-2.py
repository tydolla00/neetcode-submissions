class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        arr = []
        for word in strs:
            sorted_str = "".join(sorted(word))
            temp = res.get(sorted_str, [])
            temp.append(word)
            res[sorted_str] = temp
        for key, val in res.items():
            arr.append(val)
        return arr