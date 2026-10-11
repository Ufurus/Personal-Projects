import time
order_list = [21, 34, 11, 56, 79, 32] #
# print(sorted(order_list))
# sorted command - start:     1791501110.6624317  stop: 1791501110.6624317
# my algorithm -    start:    1791504356.3394165 stop: 1791504356.3394165
# selection sort    Start:    1791513587.7768033 Stop: 1791513587.7768033
# print('start:', start, ' end:', end)
start = time.time()
for star in range(len(order_list)): # start: 0 num: 3 len: 6 chosen number to order
    for end in range(len(order_list) - 1): # 0 + 1 = 1 len: 6 # parsing through the list and comparing
            if order_list[end] > order_list[end + 1]:
                frst_num = order_list[end]; second_num = order_list[end + 1]
                order_list[end] = second_num
                order_list[end + 1] = frst_num

stop = time.time()
print(order_list)
print('start:', start, 'stop:', stop)