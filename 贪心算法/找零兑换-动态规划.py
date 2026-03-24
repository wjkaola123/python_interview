import time


# 动态规划中最主要思想是:
# 从最简单情况开始达到所需找零的循环
# 其每一步都依靠以前的最优解来得到本步骤的最优解， 直到得到答案

def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    # 从1分开始到change逐个计算最少硬币数
    for cents in range(1, change + 1):
        # 1.初始化一个最大值
        coinCount = cents
        newCoin = 1
        # 2.减去每个硬币，向后查最少硬币数， 同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        # 3. 找零当前cents值，需要的当前最少硬币数，记录到表中
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


if __name__ == '__main__':
    amnt = 63
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)
    start_time = time.time()
    print(dpMakeChange([1, 5, 10, 21, 25], amnt, coinCount, coinsUsed))
    print("spend time:", time.time() - start_time)
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("used list:")
    print(coinsUsed)
    print("min count:")
    print(coinCount)
