import timeit

# Набір монет для решти
COINS = [50, 25, 10, 5, 2, 1]


# Жадібний алгоритм (обирає найбільші доступні номінали)
def find_coins_greedy(amount):

    change = {}
    remaining_amount = amount
    
    for coin in COINS:
        count = remaining_amount // coin
        if count > 0:
            change[coin] = count
            remaining_amount -= coin * count
            
    return change


# Алгоритм динамічного програмування
def find_min_coins(amount):

    # min_coins[i] зберігає мінімальну кількість монет
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    
    # last_coin_used[i] зберігає останню додану монету
    last_coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in COINS:
            if i >= coin:
                # Якщо поточна монета дозволяє отримати меншу кількість монет
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    last_coin_used[i] = coin
    
    # Якщо неможливо сформувати суму
    if min_coins[amount] == float('inf'):
        return {}

    # Відновлюємо склад монет у зворотньому напрямку
    change = {}
    current_sum = amount
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        if coin in change:
            change[coin] += 1
        else:
            change[coin] = 1
        current_sum -= coin
        
    return change


if __name__ == '__main__':
    
    # Тестова сума
    test_amount = 113
    
    print(f"\nСума: {test_amount}")
    print("Greedy:", find_coins_greedy(test_amount))
    print("DP    :", find_min_coins(test_amount))

    # Порівняння продуктивності
    large_amount = 10000
    
    print(f"\nТестування продуктивності на сумі: {large_amount} (середнє за 10 разів) ")
    
    greedy_time = timeit.timeit(lambda: find_coins_greedy(large_amount), number=10)
    dp_time = timeit.timeit(lambda: find_min_coins(large_amount), number=10)
    
    print(f"Greedy: {greedy_time:.6f} сек")
    print(f"DP    : {dp_time:.6f} сек")
