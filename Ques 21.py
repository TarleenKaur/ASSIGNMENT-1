def count1(lst, x):
    count = 0
    for i in lst:
        if (i == x):
            count = count + 1
    return count
lst = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]
x = 2
print('{} has occurred {} times'.format(x, count1(lst, x)))