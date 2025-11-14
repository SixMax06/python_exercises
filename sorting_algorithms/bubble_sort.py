# bubble sort a mano pk sono annoiato e non ho voglia di ascoltare la lezione di sistemi

def bubble_sort(li):
    if type(li) != list:
        raise TypeError("parameter 'list' must be of type 'list'")

    sorted = False

    while not sorted:
        sorted = True

        for value in range(len(li) - 1):
            if li[value] > li[value + 1]:
                temp = li[value]
                li[value] = li[value + 1]
                li[value + 1] = temp

                sorted = False

    return li


import random
import time

my_list = [random.randint(0, 1000) for i in range(1000)]

start_time = time.time()
sorted_list = bubble_sort(my_list)
end_time = time.time()

print(sorted_list)
print(end_time - start_time)
print(sorted(my_list) == sorted_list)
