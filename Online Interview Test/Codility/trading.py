def solution(prices, buyIndicator, sellIndicator):
    price_len = len(prices)
    position_list = [0] * price_len
    position = 0
    if buyIndicator == sellIndicator:
        return position
    increase_decrease_list = [0]
    for i in range(1, price_len):
        if prices[i - 1] < prices[i]:
            increase_decrease_list.append(1)
        elif prices[i - 1] > prices[i]:
            increase_decrease_list.append(-1)
        else:
            increase_decrease_list.append(0)
    print(increase_decrease_list)
    buy_index, sell_index = 1, 1
    buyIndicator_len, sellIndicator_len = len(buyIndicator), len(sellIndicator)
    temp = []
    while buy_index < price_len:
        buy_indicator_index = 0
        buy_index_temp = buy_index
        while buy_indicator_index < buyIndicator_len:
            if increase_decrease_list[buy_index_temp] == 0:
                buy_index_temp += 1
            elif increase_decrease_list[buy_index_temp] == buyIndicator[buy_indicator_index]:
                buy_index_temp += 1
                buy_indicator_index += 1
                if buy_indicator_index == buyIndicator_len:
                    position += 1
                    position_list[buy_index_temp] = position
                    break
            else:
                break
        buy_index += 1

    print(position_list)


# buying

# selling


input_list = [[51, 56, 56, 58, 60, 59, 54, 57, 52, 48], [1, 1], [-1, -1, 1]]

solution(*input_list)
