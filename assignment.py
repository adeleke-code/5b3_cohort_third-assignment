
# list = []
# n = int(input("Enter number of elements : "))
# print(f'Enter the {n} numbers below')


# for x in range(0, n):
#     number = int(input(':> '))
#     list.append(number)
# def avg(x):
#     avg = sum(x)/len(x)
#     return round(avg,2)
# print('Solution 1')
# print(f'# The mean is {avg(list)}')
# print('')
# print('Solution 2')


# def median(x):
#     list_2 = list.sort()
#     if n%2 != 0:

#         median = int(((n+1)/2)-1)
#         return list[median]
#     else:
#         median1 = int((n/2)-1)
#         median2 = int(n/2)
    
#         return (list[median1] + list[median2])/2

# print(f'# The median is {median(list)}')
# print('')
# print('Solution 3')

# def variance(x):

#     variance = sum((i-avg(list))**2 for i in list)/(len(list)-1)
#     return round(variance,4)
# print(f'# The variance is {variance(list)}')
# print('')
# print('Solution 4')



# def std(x):

#     std = (variance(list))**0.5
#     return round(std,4)
# print(f'# The standard deviation is {std(list)}')
# print('')
# print('Solution 5')


# def skew():
#     skew = 3*(avg(list) - median(list)) / std(list)
#     return skew
# print(f'# The Skewness is {skew()}')
# print('')


