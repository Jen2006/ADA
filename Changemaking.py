def coin_change_min(coins, amount):
    # Create DP array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Example
coins = [1, 2,4,5]
amount = 4
print("Minimum coins required:", coin_change_min(coins, amount))