class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string: filter out non-alphanumeric characters and convert to lowercase
        cleaned_str = ''.join(filter(str.isalnum, s)).lower()
        if(len(cleaned_str) == 1):
            return True
        # Find the midpoint
        mid = len(cleaned_str) // 2
        # Get the first half and the reversed second half
        first_half = cleaned_str[:mid] # takes idices 0 - (mid-1)
        second_half = cleaned_str[-mid:][::-1]  # Reverse the second half
        # Check if the first half equals the reversed second half
        return first_half == second_half



        