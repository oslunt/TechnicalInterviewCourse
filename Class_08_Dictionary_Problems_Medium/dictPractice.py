# list to dictionary

from os import removedirs


def dictToList(input_array):
    #retval = {}
    #for i in input_array:
        #retval[i[0]] = i[1]
    
    return dict(input_array)


tups = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
print(dictToList(tups))


# reverse dictionary key order

def reverseDict(dct):
    retval = {v: k for k, v in dct.items()}
    #for k, v in dct.items():
        #retval[v] = k
    return retval

test_dict = {'B' : 4, 'Y' : 2, 'U' : 5}
print(reverseDict(test_dict))


# write a program to sort nested keys by value

def sortByValues(myDict):
    return {k:dict(sorted(v.items(),key= lambda kv:kv[1])) for k,v in myDict.items()}


test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

print(sortByValues(test_dict))


# program to remove duplicate values across dictionary values

def removeDups(dct):
    nums = []
    for k,v in dct.items():
        i = 0
        while i < len(v):
            if v[i] in nums:
                v.pop(i)
            else:
                nums.append(v[i])
                i += 1
    
    return dct

test_dict = {'Manjeet' : [1, 4, 5, 6],
			'Akash' : [1, 8, 9],
			'Nikhil': [10, 22, 4],
			'Akshat': [5, 11, 22]}

print(removeDups(test_dict))