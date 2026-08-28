class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]: 
        stack = []
        res = [0] * len(temps)
        
        for i in range(len(temps)-1,-1,-1):
            temp = temps[i]
            while stack and temps[stack[-1]] <= temp:
                stack.pop()
                
            if stack:
                res[i] = stack[-1] - i
                
            stack.append(i)
            
        return res
                