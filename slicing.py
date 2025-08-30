#What is Slicing?

#Slicing means extracting a part (subsequence) of a string, list, or tuple using the index range.
#Slicing with Strings

text = "PYTHON"

print(text[0:3])   # 'PYT' (from index 0 to 2)
print(text[:4])    # 'PYTH' (from beginning to index 3)
print(text[2:])    # 'THON' (from index 2 to end)
print(text[:])     # 'PYTHON' (whole string)

#🔹 Negative Indexing
#Python allows negative indices (counting from end).

text = "PYTHON"

print(text[-1])    # 'N' (last element)
print(text[-3:])   # 'HON'
print(text[:-2])   # 'PYTH' (except last 2)

#🔹 Step Value
#You can control the gap between elements.

text = "PYTHON"

print(text[::2])   # 'PTO' (every 2nd character)
print(text[1::2])  # 'YHN'
print(text[::-1])  # 'NOHTYP' (reverse string)

#🔹 Slicing with Lists

nums = [10, 20, 30, 40, 50]

print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[::2])   # [10, 30, 50]
print(nums[::-1])  # [50, 40, 30, 20, 10] (reverse list)