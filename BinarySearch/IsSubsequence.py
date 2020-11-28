# Given a string s and a string t, check if s is subsequence of t.
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, t: str, s: str) -> bool:
        si=0
        ti=0
        while ti < len(t):
            c = t[ti]
            while si < len(s) and s[si] != c:
                si+=1
            ti = ti+1 if si < len(s) else ti
            si+=1
            if si >= len(s):
                break

        if ti == len(t):
            return True
