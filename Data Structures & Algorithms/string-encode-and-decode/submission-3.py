class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStrs = ""
        # Combine every string with the num of characters and delimiter $
        for s in strs:
            encodedStrs += "|" + str(len(s)) + "|" + s
        return encodedStrs
            
    def decode(self, s: str) -> List[str]:
        
        strList, i = [], 0  # Initialize the result list and pointer

        while i < len(s):
            # Find the start of the length (first delimiter "|")
            while s[i] != "|":
                i += 1
            
            i += 1  # Move past the starting "|"

            # Extract the number (length of the string)
            numStart = i
            while s[i] != "|":  # Find the next delimiter "|"
                i += 1
            print(s[numStart:i])
            numOfChars = int(s[numStart:i])  # Convert the numeric substring to an integer
            i += 1  # Move past the closing "|"

            # Extract the actual string of length `numOfChars`
            stChar = i
            lastChar = i + numOfChars
            sepStr = s[stChar:lastChar]
            strList.append(sepStr)

            # Move the pointer past the extracted string
            i = lastChar

        return strList
            
