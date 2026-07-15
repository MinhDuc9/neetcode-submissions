class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.t = [0] * (2 * self.n)
        # build
        for i in range(self.n):
            self.t[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.t[i] = self.t[i * 2] + self.t[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        i = index + self.n
        self.t[i] = val
        i //= 2
        while i >= 1:
            self.t[i] = self.t[i * 2] + self.t[i * 2 + 1]
            i //= 2

    # query sum on [l, r] inclusive
    def query(self, l: int, r: int) -> int:
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if (l % 2) == 1:
                res += self.t[l]
                l += 1
            if (r % 2) == 0:
                res += self.t[r]
                r -= 1
            l //= 2
            r //= 2
        return res
