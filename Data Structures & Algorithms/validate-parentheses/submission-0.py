class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for l in s:
            if l in "({[":
                stack.append(l)
            
            print(stack)

            if l in ")}]":
                if not stack:
                    return False
                
                closing = stack.pop()
                if mapping[l] != closing:
                    return False
    
        return not stack

        


        

        