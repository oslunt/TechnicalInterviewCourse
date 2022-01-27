# Given two strings s and t, return true if t is an anagram of s, and false otherwise. Use a dictionary.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s, t):
    dictS = {}
    dictT = {}

    for i in range(len(s)):
        if s[i] in dictS:
            dictS[s[i]] += 1
        else:
            dictS[s[i]] = 1
    
    for i in range(len(t)):
        if t[i] in dictT:
            dictT[t[i]] += 1
        else:
            dictT[t[i]] = 1
    
    return dictS == dictT

s = 'anagram'
t = 'nagaram'

print(isAnagram(s,t))