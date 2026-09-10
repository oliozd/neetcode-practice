class Solution:
    def isValid(self, s: str) -> bool:
        v_stack = []
        b_dict = {'}': '{', ']': '[', ')': '('} # Mapping brackets together

        if s[0] in b_dict.keys():
            return False # Return False when starting with a closed bracket
        
        for p in s:
            if p in b_dict.values(): # Opening Brackets
                v_stack.append(p)
            elif p in b_dict.keys(): # Closing Brackets
                if v_stack and v_stack[-1] == b_dict[p]: # Checking if brackets match and if stack is empty to avoid pop() error
                    v_stack.pop()
                else:
                    return False
            else: # if character in s is invalid
                return False
        
        if not v_stack: # if v_stack is empty
            return True
        else: # if remaining unmatched brackets
            return False

        