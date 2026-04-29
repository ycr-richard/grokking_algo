def findSmallest(arr):
    # 預設index=0是最小的
    smallest = arr[0]
    smallest_index = 0
    # 建立for loop，當發現下一個比現有的smallest大，替換
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


nums = [-1, 2, 1, 5, -3, 0]
print(findSmallest(nums))


# Select Sort
def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)  # copy array before mutating
    for i in range(len(copiedArr)):
        smallest_index = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest_index))
    return newArr


print(selectionSort(nums))


# In-place version (O(1) space)
# Optimized for space
def selection_sort(arr):
    n = len(arr)
    # 外層：決定現在要填入「第幾小」的值
    for i in range(n):
        min_idx = i
        # 內層：從剩餘的裡面找最小值
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 關鍵：原地交換 (Swap)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
