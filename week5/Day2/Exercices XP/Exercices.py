#exercice 1 
import numpy as np

A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

det_A = np.linalg.det(A)
print(f"Déterminant de A : {det_A}")
inv_A = np.linalg.inv(A)
print(f'Inverse de A : {inv_A}')

I = np.dot(A, inv_A)
print(f"A × A⁻¹ ={I}")

#exercice 2
arry = np.random.rand(50)
moyenne = np.mean(arry)
mediane = np.median(arry)
ecart_type = np.std(arry)
print(f'moyenne : {moyenne} , Médiane : {mediane} , Écart type : {ecart_type}')

#exercice 3 
dates = np.arange(
    np.datetime64('2023-01-01'),
    np.datetime64('2023-02-01')
)
dates_formattees = np.datetime_as_string(dates, unit='D')

#exercice 4
import pandas as pd
data = np.random.rand(5 , 4)
df = pd.DataFrame(data , columns= ["A","B","C","D"])
df[df > 0.5]
df.sum()
df.mean()
#exercice 5
import matplotlib.pyplot as plt
image = np.array([
    [0, 50, 100, 150, 200],
    [10, 60, 110, 160, 210],
    [20, 70, 120, 170, 220],
    [30, 80, 130, 180, 230],
    [40, 90, 140, 190, 255]
], dtype=np.uint8)
plt.imshow(image, cmap='gray')

#exercice 6
np.random.seed(0)
productivity_before = np.random.normal(loc=50, scale=10, size=30)
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)
mean_before = np.mean(productivity_before)
mean_after = np.mean(productivity_after)
std_before = np.std(productivity_before, ddof=1)  # échantillon
std_after = np.std(productivity_after, ddof=1)
diff = mean_after - mean_before

#exercice 7
a = np.array([10, 25, 30, 45, 50])
b = np.array([15, 20, 35, 40, 50])
a > b

#exercice 8

dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
values = np.random.randint(10, 100, size=len(dates))
ts = pd.DataFrame({
    "Date": dates,
    "Valeur": values
})
ts.set_index("Date", inplace=True)
ts.head()
jan_mar = ts["2023-01-01":"2023-03-31"]
apr_jun = ts["2023-04-01":"2023-06-30"]
jul_sep = ts["2023-07-01":"2023-09-30"]
oct_dec = ts["2023-10-01":"2023-12-31"]

#exercice 9

array_np = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

df = pd.DataFrame(
    array_np,
    columns=["A", "B", "C"]
)

#exrcice 10 


import matplotlib.pyplot as plt

x = np.arange(0, 10)                 
y = np.random.randint(0, 100, 10)    

plt.plot(x, y)
plt.xlabel("Index")
plt.ylabel("Valeurs")
plt.title("Graphique linéaire avec des données aléatoires")
plt.show()