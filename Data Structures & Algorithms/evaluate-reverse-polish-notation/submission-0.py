class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) # Casting it to an int will do integer division + Round to Zero
            else: # c is a number
                stack.append(int(c))
                
        return stack[0]
                