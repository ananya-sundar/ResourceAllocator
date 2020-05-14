# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:45:10 2020

@author: Ananya
"""

INF = 1000000

# cost[] initial cost array including unavailable packet 
# W capacity of bag 
def MinimumCost(region,cost,cap, n, W, hrs): 

    machine =['Large','XLarge','2XLarge','4XLarge','8XLarge','10XLarge']
    price = list() 
    load= list() 
    mach = list()
    # traverse the original cost[] array and skip 
    # unavailable packets and make price[] and load[] 
    # array. size variable tells the available number 
    # of distinct weighted packets. 
    size = 0
    for i in range(n): 
        if (cost[i] != -1): 
            price.append(cost[i]) 
            load.append(cap[i])
            mach.append(machine[i])
            size += 1
            
    
    n = size 
    min_cost = [[0 for i in range(W+1)] for j in range(n+1)] 

    # fill 0th row with infinity 
    for i in range(W+1): 
        min_cost[0][i] = INF 

    # fill 0th column with 0 
    for i in range(1, n+1): 
        min_cost[i][0] = 0

    # now check for each machine one by one and fill the 
    # matrix according to the condition 
    for i in range(1, n+1): 
        for j in range(1, W+1): 
            # load[i-1]>j means reqd capacity is 
            # less than capacity of item 
            if (load[i-1] > j): 
                min_cost[i][j] = min_cost[i-1][j] 

            # here we check we get minimum cost either 
            # by including it or excluding it 
            else: 
                min_cost[i][j] = min(min_cost[i-1][j], 
                    min_cost[i][j-load[i-1]] + price[i-1]) 
                
    while(min_cost[n][W]==INF):
        W-=1
    #print(min_cost[n][W]*hrs,W)
    x = len(price)
    y = W
    count = [0]*len(mach)
    while (x > 0 and y > 0):
        if (min_cost[x][y] == min_cost[x - 1][y]):
            x-=1
        elif (min_cost[x - 1][y] <= min_cost[x][y - load[x - 1]] + price[x - 1]): 
            x-=1
        else:
            # print("including load ", load[x - 1] ," with value " ,price[x - 1])
            count[x-1]+=1
            y -= load[x - 1]
    m = list(zip(mach,count))
    m = [m[i] for i in range(len(count)) if count[i]!=0]
    m.reverse()
    
    out = {"region":region, "total_cost":"$"+str(min_cost[n][W]*hrs), "machines":m}
    return out 


capacity = [10,20,40,80,160,320]
ny = [120,230,450,774,1400,2820]
india = [140,-1,413,890,1300,2970]
china = [110,200,-1,670,1180,-1]
W = int(input(" No. of units required "))
hrs = int(input("No. of hours the machine is required to run "))
#capacity = [cap*hrs for cap in capacity]
n = len(capacity) 

ans = {
    "Output" : []
}
ans['Output'].append(MinimumCost("New York", ny,capacity, n, W, hrs))
ans['Output'].append(MinimumCost("India",india,capacity, n, W, hrs)) 
ans['Output'].append(MinimumCost("China", china,capacity, n, W, hrs))  
print(ans)
