accounts = [[1,5],[7,3],[3,5]]

def richest(accounts):
    money = []
    for i in range(len(accounts)):
        money.append(sum(accounts[i]))
    return max(money)


print(richest(accounts))