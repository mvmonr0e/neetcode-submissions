class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def subtract(stack, x):
            if not stack:
                return x
            
            x -= subtract(stack, stack.pop())

        stack = []

        for t in tokens:    
            if t == "+":
                adder = stack.pop()
                adder += stack.pop()
                stack.append(adder)
            elif t == "*":
                product = stack.pop()
                product *= stack.pop()
                stack.append(product)
            elif t == '-':
                sub = stack.pop()
                sub = stack.pop() - sub
                stack.append(sub)
            elif t == '/':
                div = stack.pop()
                div = stack.pop() / div
                stack.append(int(div))
            else:
                stack.append(int(t))
            print(stack)

        print(stack)
        return stack[-1]
