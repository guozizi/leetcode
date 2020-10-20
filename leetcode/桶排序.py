"""
input : [6, 3, 5, 3, 2, 10, 7]
bucket : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 1, 2, 0, 1, 1, 1, 0, 0, 1]
output : [2, 3, 3, 5, 6, 7, 10]
"""


def bucket_sort(array):
    if not array:
        return False
    max_len = max(array) + 1
    book = [0 for _ in range(0, max_len)]
    for i in array:
        book[i] += 1
    temp_list = []
    for i in range(0, max_len):
        for _ in range(0, book[i]):
            temp_list.append(i)
    return temp_list
    # return [i for i in range(0, max_len) for _ in range(0, book[i])]


if __name__ == '__main__':
    array = [6, 3, 5, 9, 3, 10, 7]
    print(bucket_sort(array))
