weights = [3,4,2,1]
values = [5,9,3,2]
W = 5
dp = [[0] * (W + 1) for i in range(len(weights) + 1)]
for i in range(1, len(weights) + 1):
    for w in range(W + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i - 1][w],
                            values[i - 1] + dp[i - 1][w - weights[i - 1]])
        else:
            dp[i][w] = dp[i - 1][w]
print(dp[len(weights)][W])
print("DP Table:")
for row in dp:
    print(row)
                                                                                                                                                     
