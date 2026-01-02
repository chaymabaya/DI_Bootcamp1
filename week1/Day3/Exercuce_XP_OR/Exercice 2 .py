def somme(X):
    X = str(X)
    result = int(X) + int(X*2) + int(X*3) + int(X*4)
    return result
num = input("Enter a number: ")
print(somme(num))4