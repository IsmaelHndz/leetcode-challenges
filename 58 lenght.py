class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for letter in reversed(s):
            if letter != " ":
                c += 1
            elif letter == " " and c>=1:
                return c
        return c


if __name__ == '__main__':
    sentence = 'hello world '
    solution = Solution()
    print(solution.lengthOfLastWord(sentence))