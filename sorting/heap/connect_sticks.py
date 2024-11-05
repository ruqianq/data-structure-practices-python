def connectSticks(self, sticks: List[int]) -> int:
        # algo: mini heap
            # brute force: O(N^3)
            # transform-conquer 
        # edge case: only one elemenet
        if len(sticks) == 1: return 0
        import heapq
        heapq.heapify(sticks)
        total_cost = 0
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            cum = first + second
            total_cost += cum
            # Push the combined stick back into the heap
            heapq.heappush(sticks, cum)
        return total_cost
