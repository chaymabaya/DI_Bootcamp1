#exercice 1
import numpy as np
arr = np.arange(10)

#exercice 2

lst = [3.14, 2.17, 0, 1, 2]
arr = np.array(lst, dtype=int)
print(arr)

#exrcice 3

arr = np.arange(1, 10).reshape(3, 3)
print(arr)

#exercice 4
arr = np.random.rand(4, 5)
print(arr)

#exercie 5 
array = np.array([[21,22,23,22,22],[20, 21, 22, 23, 24],[21,22,23,22,22]])
array[2]

#exercice 6

array= np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
array[::-1]

#exericice 7
I = np.identity(4)

#exercice 8
arr = np.array([1, 2, 3, 4, 5])
somme = np.sum(arr)
moyenne = np.mean(arr)
print(f" la somme est {somme} , la moyenne est {moyenne}")

#exercice 9
arr = np.arange(1, 21)
matrix = arr.reshape(4, 5)

#exercice 10 
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_numbers = arr[arr % 2 != 0]

