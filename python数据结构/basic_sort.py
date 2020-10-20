# # 冒泡排序(最大的在右边)
# def bubble_sort(seq):
#     n = len(seq)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if seq[j] > seq[j + 1]:
#                 seq[j], seq[j + 1] = seq[j + 1], seq[j]
#
#
# bubble_sort([1, 3, 6, 4, 2])
#
#
# # 选择排序（最小的在在左边）
# def select_sort(seq):
#     n = len(seq)
#     for i in range(n - 1):
#         min_idx = i
#         for j in range(i + 1, n):
#             if seq[j] < seq[min_idx]:
#                 min_idx = j
#             if min_idx != i:
#                 seq[i], seq[min_idx] = seq[min_idx], seq[i]
#
#
# # 插入排序
# def insertion_sort(seq):
#     n = len(seq)
#     for i in range(1, n):
#         value = seq[i]
#         pos = i
#         while pos > 0 and value < seq[pos - 1]:
#             seq[pos] = seq[pos - 1]
#             pos -= 1
#         seq[pos] = value
#
#
# insertion_sort([5, 3, 6, 4, 2])
#
#
# # 归并排序
#
# def _merge_sorted_list(sorted_a, sorted_b):
#     length_a, length_b = len(sorted_a), len(sorted_b)
#     a = b = 0
#     new_sorted_seq = list()
#
#     while a < length_a and b < length_b:
#         if sorted_a[a] < sorted_b[b]:
#             new_sorted_seq.append(sorted_a[a])
#             a += 1
#         else:
#             new_sorted_seq.append(sorted_b[b])
#             b += 1
#
#     while a < length_a:
#         new_sorted_seq.append(sorted_a[a])
#         a += 1
#
#     while b < length_b:
#         new_sorted_seq.append(sorted_b[b])
#         b += 1
#
#     return new_sorted_seq
#
#
# def merge_sort(seq):
#     if len(seq) <= 1:
#         return seq
#     else:
#         mid = int(len(seq) / 2)
#         left_half = merge_sort(seq[:mid])
#         right_half = merge_sort(seq[mid:])
#         # 合并两个有序数组
#         new_seq = _merge_sorted_list(left_half, right_half)
#         return new_seq
#
#
# print(merge_sort([5, 3, 6, 4, 2]))
#
#
# # 快速排序
# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot_index = 0
#         pivot = array[pivot_index]
#         less_port = [i for i in array[pivot_index + 1:] if i <= pivot]
#         great_port = [i for i in array[pivot_index + 1:] if i > pivot]
#         return quick_sort(less_port) + [pivot] + quick_sort(great_port)
#
#
# print(quick_sort([5, 3, 6, 4, 2, 7]))
#
#


# 原地快排
def quick_sort(array, left, right):
    if left >= right:
        return

    low = left
    high = right
    key = array[low]

    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]

    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


quick_sort([4, 2, 5, 6, 1, 5], 0, len([4, 2, 5, 6, 1, 5]) - 1)


def getLeastNumbers(self, arr, k):
    if not arr or k <= 0: return []
    if len(arr) < k: return arr

    self.quick_sort(arr, 0, len(arr) - 1, k)
    return arr[:k]


def quick_sort(arr, left, right, k):
    if left >= right:
        return

    low = left
    hight = right
    key = arr[low]

    while left < right:
        while left < right and arr[right] > key:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]

    arr[right] = key

    if k == left:
        return
    elif k > left:
        quick_sort(arr, low, left - 1, k)
        quick_sort(arr, left + 1, hight, k)
    else:
        quick_sort(arr, low, left - 1, k)


arr = [4, 1, 2, 1, 4, 5, 3, 7, 7, 8, 10, 2, 7, 8]

quick_sort(arr, 0, len(arr) - 1, 8)
