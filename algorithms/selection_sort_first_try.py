import time

# order_list = [3, 1, 4, 6, 5, 2]
order_list = [44, 22, 34, 123, 98, 56]
start = time.time()
for i in range(len(order_list) - 1):
    min_index = i
    for j in range(i + 1, len(order_list)):
        if order_list[min_index] > order_list[j]:
            min_index = j

    order_list[i], order_list[min_index] = order_list[min_index], order_list[i]
stop = time.time()
print(order_list)
print('Start:', start, "Stop:", stop)