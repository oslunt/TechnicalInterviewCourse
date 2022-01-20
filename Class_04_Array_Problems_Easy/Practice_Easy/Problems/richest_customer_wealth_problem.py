# You are given an m x n integer grid accounts where accounts[i][j]
# is the amount of money the ith customer has in the jth bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

def richest(input_accounts):
    total = 0
    max = -1
    for i in range(len(input_accounts)):
        for j in range(len(input_accounts[i])):
            total = total + input_accounts[i][j]
        if total > max:
            max = total
        total = 0
    
    return max

def better_rich(input_accounts):
    length = len(input_accounts)
    width = len(input_accounts[0])
    maxlength = length * width
    total = 0
    max = -1
    pastrow = 0
    for i in range(maxlength):
        row = i/width
        col = i%width
        total = total + input_accounts[row][col]


input_accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(richest(input_accounts))
# Output: 17