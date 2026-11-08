class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                a = int(stack.pop())
                b = int(stack.pop())

                if t == "+":
                    stack.append(a + b)
                if t == "-":
                    stack.append(b - a)
                if t == "*":
                    stack.append(a * b)
                if t == "/":
                    stack.append(b / a)
            else:
                stack.append(int(t))
        
        return int(stack[-1])