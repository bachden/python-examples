#!/usr/bin/python
# -*- coding: utf-8 -*-

# fibonaccy
def fib(n):
    if n < 0:
        raise Exception('Invalid argument, n must be >= 0')
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print ("FIBONNACY")    
print (fib(10))

# bubble sort 
print ("BUBBLE SORT")
from random import randint
def generateRandomArray(length):
    arr = [];
    for i in range(0, length):  # @UnusedVariable
        arr.append(randint(0, 100))
    return arr;

def bubbleSort(arr):
    lenArr = len(arr)
    for i in range(0, lenArr - 1):
        for j in range(i, lenArr):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                
arr = generateRandomArray(20)
print ("origin arr: ")
print (','.join([str(a) for a in arr]))
bubbleSort(arr)
print ("sorted arr: ")
print (','.join([str(a) for a in arr]))

# find sub string indexes
import re
print ("Sub String indexes finding")
def findSubStringIndexes(sampString, subString):
    return [m.start() for m in re.finditer(subString, sampString)]

sampStr = "Thông tin giảm giá hàng tháng trở nên quen thuộc với khách hàng Việt từ khoảng nửa cuối 2016. Thậm chí sang 2017, trào lưu này dồn dập tới mức, các hãng xây dựng kế hoạch cho hàng tháng, thông tin đưa tới cho khách hàng từ ngày đầu tiên của mỗi tháng. Không chỉ vậy, các đại lý còn ngầm hiểu với nhau tự giảm giá dù không có chính sách từ hãng. Với đại lý, lợi nhuận bán xe có thể giảm, hòng lấy doanh số, tìm lợi nhuận bù từ dịch vụ."
subStr = "tháng"
indexes = findSubStringIndexes(sampStr, subStr)

print ("index for '" + subStr + "' in sample string: " + str(indexes))

# Multi Threading
