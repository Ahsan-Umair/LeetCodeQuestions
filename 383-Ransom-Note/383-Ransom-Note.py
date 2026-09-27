class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)

        for character in ransomNote:
            if character in mag:
                mag.remove(character)
            else:
                return False
        return True