class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans_dict = []

        overlapped = []

        for interval in intervals:
            print(overlapped)
            if len(overlapped) == 0 and interval[0] <= newInterval[0] <= interval[1]:
                # start overlapping
                overlapped.append(interval[0])

            if len(overlapped) == 0 and newInterval[0] <= interval[0]:
                # start overlapping
                overlapped.append(newInterval[0])

            if len(overlapped) == 1 and interval[0] <= newInterval[1] <= interval[1]:
                # end overlapping
                overlapped.append(interval[1])
                ans_dict.append(overlapped)
                continue

            if len(overlapped) == 1 and newInterval[1] <= interval[0]:
                # end overlapping
                overlapped.append(newInterval[1])
                ans_dict.append(overlapped)

            if len(overlapped) != 1:
                ans_dict.append(interval)

        if len(overlapped) == 1:
            overlapped.append(newInterval[1])
            ans_dict.append(overlapped)
        
        if len(overlapped) == 0:
            ans_dict.append(newInterval)

        return ans_dict
        