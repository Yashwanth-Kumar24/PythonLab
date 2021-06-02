def knapsack(weights,prices,bagCapacity):
    l = list()
    for i in range(len(weights)):
        totalItems = dict()
        totalItems['weights'] = weights[i]
        totalItems['prices'] = prices[i]
        totalItems['cost'] = prices[i]/weights[i]
        l.append(totalItems)

    l = sorted(l, key=lambda k: k['cost'],reverse=True) 
    profit = 0
    for i in l:
        curWt = int(i['weights'])
        curVal = int(i['prices'])
        if bagCapacity - curWt >= 0:
                bagCapacity -= curWt
                profit += curVal
        else:
            fraction = bagCapacity / curWt
            profit += curVal * fraction
            bagCapacity = int(bagCapacity - (curWt * fraction))
            break
    return profit


weights =  [4,9,10,20,2,1]
prices = [400,1800,3500,4000,1000,200]
bagCapacity = 20

maximumProfit = knapsack(weights,prices,bagCapacity)
print("Maximum Profit is ",maximumProfit)
