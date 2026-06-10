class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == ')':
                if not stack:
                    return False
                curr = stack.pop()
                if curr != '(':
                    return False
            elif ch == ']':
                if not stack:
                    return False
                curr = stack.pop()
                if curr != '[':
                    return False
            elif ch == '}':
                if not stack:
                    return False
                curr = stack.pop()
                if curr != '{':
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0

                
