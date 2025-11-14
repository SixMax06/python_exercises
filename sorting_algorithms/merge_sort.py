# merge sort a mano pk sono annoiato e non ho voglia di ascoltare la lezione di informatica

def merge_sort(li):
    def merge_lists(list1, list2):
        merged_list = []
        ind1, ind2 = 0, 0

        for i in range(len(list1) + len(list2)):
            if ind1 >= len(list1):
                for j in range(ind2, len(list2)):
                    merged_list.append(list2[j])

                break

            if ind2 >= len(list2):
                for j in range(ind1, len(list1)):
                    merged_list.append(list1[j])

                break

            if list1[ind1] < list2[ind2]:
                merged_list.append(list1[ind1])
                ind1 += 1

            else:
                merged_list.append(list2[ind2])
                ind2 += 1

        return merged_list

    if type(li) != list and type(li) != tuple:
        raise TypeError("Please provide a list or tuple")

    divided_li = []
    ind = 0

    for i in range(len(li) // 2):
        divided_li.append([li[i + ind], li[i + ind + 1]])
        ind += 1

    if len(li) % 2 != 0:
        divided_li.append([li[len(li) - 1]])

    for couple in divided_li:
        if type(couple) == list and len(couple) == 2:
            if couple[0] > couple[1]:
                couple[0], couple[1] = couple[1], couple[0]

    sorted_li = divided_li
    divided_li = []

    for _ in range((len(sorted_li) // 2) + (len(sorted_li) % 2)):
        ind = 0
        for i in range((len(sorted_li) // 2) + (len(sorted_li) % 2)):
            if i + ind + 1 >= len(sorted_li):
                divided_li.append(sorted_li[i + ind])
            else:
                divided_li.append(merge_lists(sorted_li[i + ind], sorted_li[i + ind + 1]))

            ind += 1

        sorted_li = divided_li
        divided_li = []

    sorted_li = sorted_li[0]
    return sorted_li


import random
import time

my_list = [random.randint(0, 1000) for i in range(1000)]

start_time = time.time()
sorted_list = merge_sort(my_list)
end_time = time.time()

print(sorted_list)
print(end_time - start_time)
print(sorted(my_list) == sorted_list)