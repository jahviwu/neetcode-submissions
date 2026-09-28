class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curNum = 0

        for c in tokens:
            if c not in ["+","-","*","/"]:
                stack.append(int(c))
            else:
                a = stack.pop()
                b = stack.pop()
                if c == "+":
                    curNum = a+b
                elif c == "-":
                    curNum = b - a 
                elif c == "*":
                    curNum = a * b
                else: # Division
                    curNum = int(b/a)    
                
                stack.append(curNum)
            
        return stack[-1]
                