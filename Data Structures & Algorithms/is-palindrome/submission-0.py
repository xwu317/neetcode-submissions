class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = [char.lower() for char in s if char.isalnum()]
        
        start = 0
        end = len(cleaned_string) - 1

        while start < end:
            if cleaned_string[start] != cleaned_string[end]:
                return False
            
            start += 1
            end -= 1
        
        return True

'''
Approach:

Beginning Pointer = 0
End Pointer = len(s) - 1

s.lower()
s.replace(" ","") # removes all white spaces

while BP < EP:
    compare BP and EP:
        if BP == EP:
            increment BP
            decrement EP
        if EP != BP:
            return False
        
return True
'''
        