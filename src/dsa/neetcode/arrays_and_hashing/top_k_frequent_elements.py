class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Pythonic
        # return [num for num, _ in Counter(nums).most_common(k)]

        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        return sorted(counter, key=lambda x: counter[x], reverse=True)[:k]
