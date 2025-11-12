def even(i):
    evens = []
    for item in i :
        if item % 2 != 0 :
            evens.append(item)
    return max(evens)

print(even( [1 , 2 , 100 ,123]))