class Solution:
    def isPalindrome(self, s:str):
        cleaned = ""
        p = s.lower()
        t = p.replace(" ","")
        for char in t:
            if char.isalnum():
                cleaned+=char

        return cleaned == cleaned[::-1]
