class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26

        for task in tasks:
            count[ord(task) - ord('A')] +=1
        
        f_max = max(count)

        k = count.count(f_max)

        minimum_cycles = (f_max - 1) * (n + 1) + k

        return max(minimum_cycles,len(tasks))