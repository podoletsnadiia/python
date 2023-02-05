
#Generate 100 random numbers between 0 and 1000
#import random
#randomlist = random.sample(range(0, 1000), 100)
#print(randomlist)

#Sort list from min to max (using bubbleSort)
#Step 1) Create a flag variable that monitors if any swapping has occurred in the inner loop
#Step 2) If the values have swapped positions, continue to the next iteration
#Step 3) If the benefits have not swapped positions, terminate the inner loop, and continue with the outer loop.
# def bubbleSort(theSeq):
#     n = len(theSeq)
#     for i in range(n - 1):
#         flag = 0
#         for j in range(n - 1):
#             if theSeq[j] > theSeq[j + 1]:
#                 tmp = theSeq[j]
#                 theSeq[j] = theSeq[j + 1]
#                 theSeq[j + 1] = tmp
#                 flag = 1
#         if flag == 0:
#             break
#     return theSeq
# el = [112, 247, 944, 45, 792, 395, 158, 221, 266, 812, 632, 971, 17, 968, 161, 860, 419, 897, 208, 487, 236, 614, 62, 159, 446, 474, 125, 939, 259, 111, 341, 311, 11, 288, 688, 147, 561, 508, 631, 516, 730, 895, 545, 941, 702, 22, 592, 313, 94, 799, 70, 682, 0, 447, 381, 82, 645, 283, 47, 921, 920, 34, 383, 765, 386, 640, 344, 654, 512, 835, 750, 828, 698, 524, 116, 179, 414, 515, 770, 467, 886, 603, 930, 145, 427, 364, 203, 777, 169, 411, 671, 453, 978, 667, 961, 384, 985, 535, 338, 541]
# result = bubbleSort(el)
# print(result)

# Python program to count Even
# and Odd numbers in a List
# list1 = [112, 247, 944, 45, 792, 395, 158, 221, 266, 812, 632, 971, 17, 968, 161, 860, 419, 897, 208, 487, 236, 614, 62, 159, 446, 474, 125, 939, 259, 111, 341, 311, 11, 288, 688, 147, 561, 508, 631, 516, 730, 895, 545, 941, 702, 22, 592, 313, 94, 799, 70, 682, 0, 447, 381, 82, 645, 283, 47, 921, 920, 34, 383, 765, 386, 640, 344, 654, 512, 835, 750, 828, 698, 524, 116, 179, 414, 515, 770, 467, 886, 603, 930, 145, 427, 364, 203, 777, 169, 411, 671, 453, 978, 667, 961, 384, 985, 535, 338, 541]
# even_count, odd_count = 0, 0
# # iterating each number in list
# for num in list1:
#     # checking condition
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)

