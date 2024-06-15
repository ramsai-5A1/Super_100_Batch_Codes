class Solution(object):
    def isValid(self, s):
        stack = []
        openBrackets = ["(", "{", "["]
        for ele in s:
            if ele in openBrackets:
                stack.append(ele)
            else:
                if len(stack) == 0:
                    return False 
                elif ele == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif ele == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif ele == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True 
        return False
        
