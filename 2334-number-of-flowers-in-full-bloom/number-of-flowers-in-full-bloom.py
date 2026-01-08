class Solution:
    def fullBloomFlowers(self, flowers, people):
        from collections import defaultdict
        import bisect

        events = defaultdict(int)

        for s, e in flowers:
            events[s] += 1
            events[e + 1] -= 1

        times = sorted(events.keys())

        bloom = []
        curr = 0
        for t in times:
            curr += events[t]
            bloom.append(curr)


        ans = []
        for p in people:
            idx = bisect.bisect_right(times, p) - 1
            if idx >= 0:
                ans.append(bloom[idx])
            else:
                ans.append(0)

        return ans
