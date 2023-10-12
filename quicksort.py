import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = []
    right = []
    for element in arr[:-1]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    n = random.randint(30,50)
    arr = []
    for i in range (n):
        random_integer=random.randint(1,100)
        arr.append(random_integer)
    sorted_arr = quick_sort(arr)
    print("정렬된 리스트:", sorted_arr)
