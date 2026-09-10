"""
Array in Python

"""
a = [1, 2, 3, 4, 5]
# Accessing elements
print(a[0])  # 1
print(a[1])  # 2

# Length of array
print(len(a))  # 5

# Adding elements
# O(1) time complexity
a.append(6)
print(a)  # [1, 2, 3, 4, 5, 6]

# Removing elements
# O(1) time complexity
a.pop()
print(a)  # [1, 2, 3, 4, 5]

# Inserting elements
# O(n) time complexity
a.insert(1, 7)
print(a)  # [1, 7, 2, 3, 4, 5]

# Removing elements
# O(n) time complexity
a.remove(7)
print(a)  # [1, 2, 3, 4, 5]

# Slicing
# O(n) time complexity
print(a[1:3])  # [2, 3]
print(a[:3])  # [1, 2, 3]
print(a[1:])  # [2, 3, 4, 5]

# Copying
# O(n) time complexity
b = a.copy()
print(b)  # [1, 2, 3, 4, 5]

# Reversing
# O(n) time complexity
a.reverse()
print(a)  # [5, 4, 3, 2, 1]

# Sorting
# O(nlogn) time complexity
a.sort()
print(a)  # [1, 2, 3, 4, 5]

# Clearing
a.clear()
print(a)  # []

# Array of arrays
a = [[1, 2], [3, 4], [5, 6]]
print(a[0][0])  # 1
print(a[1][1])  # 4
print(a[2][0])  # 5

# Array of arrays of arrays
a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(a[0][0][0])  # 1
print(a[1][1][1])  # 8
print(a[1][0][1])  # 6

# Array of arrays of arrays of arrays
a = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print(a[0][0][0][0])  # 1
print(a[1][1][1][1])  # 16
print(a[1][0][1][0])  # 11


