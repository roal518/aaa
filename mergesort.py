def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 리스트를 반으로 나눕니다.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 각 부분 리스트를 재귀적으로 정렬합니다.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 정렬된 부분 리스트를 병합합니다.
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    # 두 부분 리스트를 비교하여 작은 값을 결과 리스트에 추가합니다.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # 남은 요소들을 결과 리스트에 추가합니다.
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

# 테스트를 위한 예제
if __name__ == "__main__":
    arr = [12, 6,7,11,3, 13, 5, 6, 7,124,1,23,40,50,10002,404]
    sorted_arr = merge_sort(arr)
    print("정렬된 리스트:", sorted_arr)
