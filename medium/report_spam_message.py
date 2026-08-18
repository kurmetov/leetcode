class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        banset = set(bannedWords)

        for msg in message:
            if msg in banset:
                count += 1
            if count >= 2:
                return True
            

        return False