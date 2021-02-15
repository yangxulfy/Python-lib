#eg. Dynamic programming. There are 3 kinds of tokens with values of 1, 5 11 dollars.
# You want to use them to pay n=15 dollars bill.
# What is the minimum number of tokens to use?
# time complexity is O(n)
n = 15
f = [0]
tokens = []
plans = [[]]

for i in range(1, n+1):
    cost = 1000
    if i - 1 >= 0:
        if cost > f[i-1] + 1:
            cost = f[i-1]  + 1
            x = 1
            plan = plans[i-1]+[1]
        # cost = min(cost, f[i-1] + 1)
    if i - 5 >= 0:
        # cost = min(cost, f[i-5] + 1)
        if cost > f[i-5] + 1:
            cost = f[i - 5] + 1
            x = 5
            plan = plans[i-5]+[5]
    if i - 11 >=0:
        # cost = min(cost, f[i-11] + 1)
        if cost > f[i-11] + 1:
            cost = f[i - 11] + 1
            x = 11
            plan = plans[i-11]+[11]
    f.append(cost)
    tokens.append(x)
    plans.append(plan)
print ("cost is ", cost)
print ("your plan of paying is ", plan)


