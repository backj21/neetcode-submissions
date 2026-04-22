class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for temp in strs:
            cnt = [0] * 26
            for c in temp:
                cnt[ord(c) - ord("a")] += 1
            res[tuple(cnt)].append(temp)
        return res.values()