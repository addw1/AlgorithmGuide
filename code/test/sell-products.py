def maximize_trading_profit(rates, strategy, k):
    """
    rates:    list of positive integers
    strategy: list of integers in {-1, 0, 1}
    k:        even integer
    Returns the maximum possible profit after optionally applying
    one modification on exactly k consecutive days.
    """

    n = len(rates)
    # 1) Build profitDelta array and compute oldProfit
    profitDelta = [0] * n
    for i in range(n):
        if strategy[i] == 1:
            profitDelta[i] = rates[i]
        elif strategy[i] == -1:
            profitDelta[i] = -rates[i]
        else:
            profitDelta[i] = 0

    oldProfit = sum(profitDelta)

    # 2) Build prefix sums for profitDelta and for rates
    prefixProfitDelta = [0] * (n + 1)
    prefixRates = [0] * (n + 1)
    for i in range(n):
        prefixProfitDelta[i + 1] = prefixProfitDelta[i] + profitDelta[i]
        prefixRates[i + 1] = prefixRates[i] + rates[i]

    # 3) Compute the maximum Delta(L)
    best_delta = float("-inf")
    half_k = k // 2  # k is guaranteed to be even
    for L in range(n - k + 1):
        old_range_profit = prefixProfitDelta[L + k] - prefixProfitDelta[L]
        new_range_profit = prefixRates[L + k] - prefixRates[L + half_k]
        delta = new_range_profit - old_range_profit
        if delta > best_delta:
            best_delta = delta
    # 4) Decide whether to apply the modification or not
    # If best_delta is negative or zero, it's better not to modify.
    if best_delta <= 0:
        return oldProfit
    else:
        return oldProfit + best_delta


# ----------------- EXAMPLE -----------------
if __name__ == "__main__":
    rates = [5, 7, 9, 3, 6, 10, 11]
    strategy = [-1, 0, 1, -1, -1, 1, 0]
    k = 4  # must be even

    print(maximize_trading_profit(rates, strategy, k))
