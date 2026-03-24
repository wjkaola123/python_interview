import time


def recMC(coinValueList, change, knowResults):
    minCoins = change

    if change in coinValueList:
        knowResults[change] = 1  # 记录最优解
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]  # 查表成功，直接返回最优解
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i, knowResults)

            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change] = minCoins  # 找到最优解，记录到表中

    return minCoins


if __name__ == '__main__':
    start_time = time.time()
    print(recMC([1, 5, 10, 25], 63, [0] * 64))
    print(time.time() - start_time)
