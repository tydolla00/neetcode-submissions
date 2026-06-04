class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        resS = {}
        resT = {}
        for l in s:
            resS[l] = resS.get(l, 0) + 1

        for l in t:
            resT[l] = resT.get(l, 0) + 1

        return resS == resT