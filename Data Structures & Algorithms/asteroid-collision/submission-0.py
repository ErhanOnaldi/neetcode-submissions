class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            alive = True

            while stack and stack[-1] > 0 and ast < 0:
                if abs(stack[-1]) < abs(ast):
                    stack.pop()
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break

            if alive:
                stack.append(ast)

        return stack