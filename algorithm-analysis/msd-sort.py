# Python implementation of MSD Radix Sort of MSD Radix Sort using counting sort() 
# Idea taken from https://www.geeksforgeeks.org/msd-most-significant-digit-radix-sort/?ref=lbp

import math
import time 

def print_arr(arr):
    for i in arr:
        print(i, end=" ")
    print()
 
def digit_at(x, d):
    return (int)(x / pow(10, d - 1)) % 10
 
def MSD_sort(arr, lo, hi, d):
    if (hi - lo) < 2 or d < 1:
      return
 
    counts = [0] * 10
    temp = [0] * (hi - lo)
 
    # Store occurrences of most significant character from each integer in count[]
    for i in range(lo, hi):
      digit = digit_at(arr[i], d)
      counts[digit] += 1
 
    # Change count[] so that count[] now contains actual position of this digits in temp[]
    index = 0
    for i, count in enumerate(counts):
      counts[i] = index
      index += count
 
    # Build the temp
    for i in range(lo, hi):
      digit = digit_at(arr[i], d)
      temp[counts[digit]] = arr[i]
      counts[digit] += 1
 
    # Copy all integers of temp to arr[], so that arr[] now contains partially sorted integers
    for i in range(lo, hi):
      arr[i] = temp[i - lo]
 
    # Recursively MSD_sort() on each partially sorted integers set to sort them by their next digit
    counts.insert(0,0)
    for i in range(len(counts) - 1):
      MSD_sort(arr, lo + counts[i], lo + counts[i + 1], d - 1)
 
# Function to find the largest integer
def getMax(arr):
    mx = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > mx:
            mx = arr[i]
    return mx
 
# Main function to call MSD_sort
def radixsort(arr):
    # Find the maximum number to know number of digits
    m = getMax(arr)
 
    # Get the length of the largest integer
    d = math.floor(math.log10(abs(m))) + 1
 
    # Function call
    MSD_sort(arr, 0, len(arr) - 1, d)
 
    return arr
 
 

if __name__ == '__main__':

    from random import randint
    for i in range(50):

        arr=[randint(1000,9999) for i in range(100)] 

        start_time = time.time()
        arr = radixsort(arr)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
