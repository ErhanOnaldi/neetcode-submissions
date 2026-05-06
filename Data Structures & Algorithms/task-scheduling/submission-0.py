from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        maxFreq = max(freq.values())
        maxFreqTaskCount = sum(1 for count in freq.values() if count == maxFreq)

        frame = (maxFreq - 1) * (n + 1) + maxFreqTaskCount

        return max(len(tasks), frame)