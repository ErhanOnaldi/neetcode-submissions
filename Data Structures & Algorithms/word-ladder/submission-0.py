from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_adjacent(s1: str, s2: str) -> bool:
            length = len(s1)
            same = 0
            for c1, c2 in zip(s1,s2):
                if c1 == c2:
                    same += 1

            return True if abs(length - same) == 1 else False
        
        q = deque()
        visited = set()
        for s in wordList:
            if is_adjacent(beginWord, s):
                q.append(s)
                visited.add(s)
        
        transformation_count = 0
        while q:
            level = len(q)
            transformation_count += 1
            
            for _ in range(level):
                processing_string = q.popleft()
                if processing_string == endWord:
                    return transformation_count + 1
                for s in wordList:
                    if s in visited:
                        continue
                    
                    if is_adjacent(processing_string, s):
                        q.append(s)
                        visited.add(s)

        return 0 

    

