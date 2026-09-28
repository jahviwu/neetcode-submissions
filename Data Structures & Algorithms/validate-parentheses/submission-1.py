class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen: # This means c is a CLOSING parentheses

                # if stack is not empty AND the last added value [-1] matches the specific closing parentheses "c"
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # we can pop them and move on 
                else:
                    return False

            else: # This means c is an OPENING parentheses
                stack.append(c) # add to stack

        if not stack: # if the stack is empty aka everything has a pair 
            return True
        else: 
            return False
