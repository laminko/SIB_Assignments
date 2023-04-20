from typing import Tuple


def value_finder(coins: list[int], amount: int, found_coins: list[int]) -> int:
    """Find equality between summation of available coins and amount.

    Args:
        coins (list[int]): Available coins.
        amount (int): Input amount of money.
        found_coins (list[int]): Collection of found coins.

    Returns:
        int: equation result
    """
    result = -1
    if coins:
        found_coin = coins[-1]
        result = amount - found_coin
        # print(result, coins[:-1])
        if result >= 0:
            found_coins.append(found_coin)
            if result == 0:
                return result
            return value_finder(coins[:-1], result, found_coins)
        else:
            return value_finder(coins[:-1], amount, found_coins)
    return result


def calculate_LNC(coins: list[int], amount: int) -> Tuple[int, list[int]]:
    """Calculate Least Number of Coins (LNC)

    Args:
        coins (list[int]): Collection of available coins.
        amount (int): Amount of money owned by customer.

    Returns:
        (int, list[int]): LNC value and found coins
    """
    lnc: int = -1
    result: int = None
    found_coins: list[int] = []

    while True:
        # NOTE: reset found coins on every iteration
        found_coins = []
        result = value_finder(coins, amount, found_coins)
        if result == 0:
            break

        if coins:
            coins.pop()
        else:
            break

    if not result:
        lnc = len(found_coins)

    return (lnc, found_coins)
