# ข้อ 1: 1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21
print("ข้อ 1:")
i = 1
count = 0
while i <= 21:
    print(i, end=', ' if i < 21 else '')
    if count == 0:
        count += 1
    else:
        i += 2
print("\n")

# ข้อ 2: 2, 2, 5, 8, 11, 13, 14, 17
print("ข้อ 2:")
nums = [2, 2, 5, 8, 11, 13, 14, 17]
i = 0
while i < len(nums):
    print(nums[i], end=', ' if i < len(nums) - 1 else '')
    i += 1
print("\n")

# ข้อ 3: 100, 90, ..., -100
print("ข้อ 3:")
i = 100
while i >= -100:
    print(i, end=', ' if i > -100 else '')
    i -= 10
print("\n")

# ข้อ 4: -30, -20, ..., 30
print("ข้อ 4:")
i = -30
while i <= 30:
    print(i, end=', ' if i < 30 else '')
    i += 10
print("\n")

# ข้อ 5: 15, 23, 31, 39, 47, 55
print("ข้อ 5:")
i = 15
while i <= 55:
    print(i, end=', ' if i < 55 else '')
    i += 8
print()
