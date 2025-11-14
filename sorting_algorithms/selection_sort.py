# selection sort a mano pk sono annoiato e non ho voglia di ascoltare la lezione di inglese

def selection_sort(li):
    if type(li) != list:
        raise TypeError("parameter 'list' must be of type 'list'")

    sorted = False

    min_item = li[0]
    min_index = 0
    index = 0

    while not sorted:
        sorted = True

        for i in range(index, len(li)):
            if li[i] < min_item:
                min_item = li[i]
                min_index = i
                sorted = False

        if not sorted:
            temp = li[index]
            li[index] = li[min_index]
            li[min_index] = temp

            index += 1
            min_item = li[index]
            min_index = index

    return li


import random
import time

my_list = [random.randint(0, 1000) for i in range(1000)]

start_time = time.time()
sorted_list = selection_sort(my_list)
end_time = time.time()

print(sorted_list)
print(end_time - start_time)
print(sorted(my_list) == sorted_list)
