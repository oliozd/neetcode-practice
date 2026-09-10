class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for token in tokens:
            # Take 2 previous values from the stack if operator encountered in tokens
            if token in {"+", "-", "*", "/"}:
                a = int(stack.pop())
                b = int(stack.pop())
            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(b-a)
            elif token == "*":
                stack.append(a*b)
            elif token == "/":
                stack.append(int(b/a))
            # If token is not an operand then it must be a value so push onto the stack for calc
            else:
                stack.append(int(token))
        return stack[-1]
            
            
            
        