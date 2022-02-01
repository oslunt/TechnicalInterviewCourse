# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
#
# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Input: s1 = “this apple is sweet”, s2 = “this apple is sour”
# Output: [“sweet”, “sour”]
#
# Input: s1 = “apple apple”, s2 = “banana”
# Output: [“banana”]

def uncommonWords(one, two):
    dct = {}
    together = one + ' ' + two
    words = together.split(' ')
    for word in words:
        if word in dct:
            dct[word] += 1
        else:
            dct[word] = 1
    
    retval = []

    for k,v in dct.items():
        if v == 1:
            retval.append(k)
    
    return retval

s1 = 'this apple is sweet'
s2 = 'this apple is sour'

s3 = 'apple apple'
s4 = 'banana'

print(uncommonWords(s1,s2))
print(uncommonWords(s3,s4))