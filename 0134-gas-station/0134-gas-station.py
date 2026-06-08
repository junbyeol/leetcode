class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        net_cost = [g - c for (g,c) in zip(gas, cost)]

        min_val = net_cost[0]
        min_index = 0

        s = 0
        for i, net in enumerate(net_cost):
            s = s + net
            if min_val > s:
                min_val = s
                min_index = i

        s = 0
        for i in range(0, n):
            idx = (i + min_index + 1) % n
            s = s + net_cost[idx]
            if s < 0:
                return -1

        return (min_index + 1)%n