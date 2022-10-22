# Bubble Sort

def bubbleSort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j + 1]
        array[j + 1] = temp

# Selection Sort
def selectionSort(array, size):
    for step in range(size):
        minIdx = step
        for i in range(step + 1, size):
            if array[i] > array[minIdx]:
                minIdx = i
        (array[step], array[minIdx]) = (array[minIdx], array[step])


data = [75, 98, 19, 65, 50, 98, 32]



# Print Bubble Sort
bubbleSort(data)
print('(Bubble Sort) Sorted Array in Ascending Order:')
print(data)

print()

# Print Selection Sort
size = len(data)
selectionSort(data, size)
print('(Selection Sort) Sorted Array in Descending Order:')
print(data)
