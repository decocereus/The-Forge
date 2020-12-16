#finding the smallest number

num = None

for i in (4, 8, 15, 16, 23, 42):
    if num is None:
        num = i
    if i < num:
        num = i
print('The smallest number is',num)
