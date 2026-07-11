class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()
    
        print(cars)

        stack = []
        for i in range(len(cars) - 1, -1, -1):
            time = (target - cars[i][0]) / cars[i][1]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)