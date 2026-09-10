class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack : list[int] = [] 
        pos_stack: list[int] = []
        output: list[int] = len(temperatures)*[0] # Populate with fillers so that inserts work correctly
  
        for i, temp in enumerate(temperatures):
            
            # If current temp > top of stack: POP temp and record days
            if stack:
                while(temp > stack[-1]):
                    stack.pop()
                    return_index = pos_stack.pop()
                    output.insert(return_index, i - return_index) # Insert() inserts before the input index hence + 1 
                    output.pop(return_index + 1) # Remves the filler 0

                    if not stack:
                        break
            
         
            stack.append(temp)
            pos_stack.append(i) 
    
            
            #print(temp, stack, pos_stack )    
         

        return output

                