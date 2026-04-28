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
