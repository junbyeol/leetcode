class PriorityQueue:
    def __init__(self, k: int):
        self.heap = [0]
    
    def push(self, num: int):
        self.heap.append(num)
        it = len(self.heap) - 1
        
        while it != 1:
            if self.heap[it // 2] < self.heap[it]:
                break
            tmp = self.heap[it // 2]
            self.heap[it // 2] = self.heap[it]
            self.heap[it] = tmp
            it = it // 2

        # print(self.heap)

    def pop(self):
        it = 1
        self.heap[1] = self.heap[-1]
        self.heap.pop(-1)

        while 2 * it < len(self.heap): #자식이 없을 때 까지
            to_change = None

            if 2 * it + 1 == len(self.heap): # 자식이 하나
                if self.heap[it] > self.heap[2 * it]:
                    to_change = 2 * it
            else: # 자식이 둘
                if self.heap[it] < self.heap[2*it] and self.heap[it] < self.heap[2*it+1]:
                    break

                if self.heap[2 * it] <= self.heap[2 * it + 1]:
                    to_change = 2 * it
                else:
                    to_change = 2 * it + 1

            if to_change is None:
                break
            tmp = self.heap[it]
            self.heap[it] = self.heap[to_change]
            self.heap[to_change] = tmp
            it = to_change

        # print(self.heap)

    def size(self):
        return len(self.heap) - 1
            
    def top(self):
        return self.heap[1]



class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.pq = PriorityQueue(k)

        for num in nums:
            self.pq.push(num)

        while self.pq.size() > self.k:
            self.pq.pop()

    def add(self, val: int) -> int:
        # print(f"push {val}")
        self.pq.push(val)

        if self.pq.size() > self.k:
            # print(f"pop")
            self.pq.pop()

        return self.pq.top()

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = KthLargest(k, nums)
        
        return kth.pq.top()
        